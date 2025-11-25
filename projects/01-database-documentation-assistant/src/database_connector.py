"""
Módulo de Conexão com Bancos de Dados para Documentação Automática.

Este módulo fornece uma classe robusta para gerenciar conexões com bancos de dados
PostgreSQL e MySQL, incluindo connection pooling, retry logic e context managers.

Classes:
    DatabaseConnectionError: Exception customizada para erros de conexão.
    DatabaseConnector: Classe principal para gerenciamento de conexões.

Exemplo de uso:
    >>> from database_connector import DatabaseConnector
    >>> 
    >>> config = {
    ...     'db_type': 'postgresql',
    ...     'host': 'localhost',
    ...     'port': 5432,
    ...     'database': 'mydb',
    ...     'username': 'user',
    ...     'password': 'pass'
    ... }
    >>> 
    >>> connector = DatabaseConnector(config)
    >>> if connector.test_connection():
    ...     with connector.get_connection() as conn:
    ...         result = conn.execute("SELECT * FROM users")
    ...         for row in result:
    ...             print(row)

Autor: Paulo César Mendes de Sousa Júnior
Data: 2025
"""

import logging
import time
from contextlib import contextmanager
from typing import Dict, Optional, Any, Generator
from urllib.parse import quote_plus

from sqlalchemy import create_engine, inspect, text, pool
from sqlalchemy.engine import Engine, Inspector, Connection
from sqlalchemy.exc import SQLAlchemyError, OperationalError


# Configuração de logging estruturado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DatabaseConnectionError(Exception):
    """
    Exception customizada para erros de conexão com banco de dados.
    
    Attributes:
        message (str): Mensagem descritiva do erro.
        original_exception (Exception): Exception original que causou o erro.
    
    Exemplo:
        >>> try:
        ...     raise DatabaseConnectionError("Falha na conexão", ValueError("Port inválida"))
        ... except DatabaseConnectionError as e:
        ...     print(f"Erro: {e.message}")
        ...     print(f"Causa: {e.original_exception}")
    """
    
    def __init__(self, message: str, original_exception: Optional[Exception] = None):
        """
        Inicializa a exception com mensagem e exception original.
        
        Args:
            message: Mensagem descritiva do erro.
            original_exception: Exception original que causou o erro (opcional).
        """
        self.message = message
        self.original_exception = original_exception
        super().__init__(self.message)
        
        if original_exception:
            logger.error(
                f"DatabaseConnectionError: {message}",
                exc_info=original_exception
            )


class DatabaseConnector:
    """
    Classe para gerenciamento robusto de conexões com bancos de dados.
    
    Suporta PostgreSQL e MySQL com connection pooling, retry logic automático
    e context managers para gerenciamento seguro de conexões.
    
    Attributes:
        db_type (str): Tipo do banco de dados ('postgresql' ou 'mysql').
        host (str): Endereço do servidor de banco de dados.
        port (int): Porta do servidor de banco de dados.
        database (str): Nome do banco de dados.
        username (str): Nome de usuário para autenticação.
        engine (Engine): Engine SQLAlchemy para conexões.
        _is_connected (bool): Flag indicando se há conexão ativa.
    
    Exemplo:
        >>> config = {
        ...     'db_type': 'postgresql',
        ...     'host': 'localhost',
        ...     'port': 5432,
        ...     'database': 'mydb',
        ...     'username': 'user',
        ...     'password': 'password',
        ...     'pool_size': 5,
        ...     'max_overflow': 10
        ... }
        >>> 
        >>> connector = DatabaseConnector(config)
        >>> connector.connect()
        >>> inspector = connector.get_inspector()
        >>> tables = inspector.get_table_names()
        >>> print(f"Tabelas encontradas: {tables}")
        >>> connector.disconnect()
    """
    
    # Configurações padrão para connection pooling
    DEFAULT_POOL_SIZE = 5
    DEFAULT_MAX_OVERFLOW = 10
    DEFAULT_POOL_TIMEOUT = 30
    DEFAULT_POOL_RECYCLE = 3600
    
    # Configurações para retry logic
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # segundos
    BACKOFF_MULTIPLIER = 2
    
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa o conector com configurações fornecidas.
        
        Args:
            config: Dicionário com configurações de conexão contendo:
                - db_type (str): Tipo do banco ('postgresql' ou 'mysql').
                - host (str): Endereço do servidor.
                - port (int): Porta do servidor.
                - database (str): Nome do banco de dados.
                - username (str): Usuário para autenticação.
                - password (str): Senha para autenticação.
                - pool_size (int, opcional): Tamanho do pool de conexões.
                - max_overflow (int, opcional): Máximo de conexões extras.
                - pool_timeout (int, opcional): Timeout para obter conexão do pool.
                - pool_recycle (int, opcional): Tempo para reciclar conexões.
        
        Raises:
            DatabaseConnectionError: Se configurações obrigatórias estiverem faltando.
            ValueError: Se db_type não for suportado.
        
        Exemplo:
            >>> config = {'db_type': 'postgresql', 'host': 'localhost', 
            ...           'port': 5432, 'database': 'test', 
            ...           'username': 'user', 'password': 'pass'}
            >>> connector = DatabaseConnector(config)
        """
        # Validação de configurações obrigatórias
        required_fields = ['db_type', 'host', 'port', 'database', 'username', 'password']
        missing_fields = [field for field in required_fields if field not in config]
        
        if missing_fields:
            raise DatabaseConnectionError(
                f"Configurações obrigatórias faltando: {', '.join(missing_fields)}"
            )
        
        self.db_type: str = config['db_type'].lower()
        self.host: str = config['host']
        self.port: int = int(config['port'])
        self.database: str = config['database']
        self.username: str = config['username']
        self._password: str = config['password']
        
        # Configurações de pool
        self.pool_size: int = config.get('pool_size', self.DEFAULT_POOL_SIZE)
        self.max_overflow: int = config.get('max_overflow', self.DEFAULT_MAX_OVERFLOW)
        self.pool_timeout: int = config.get('pool_timeout', self.DEFAULT_POOL_TIMEOUT)
        self.pool_recycle: int = config.get('pool_recycle', self.DEFAULT_POOL_RECYCLE)
        
        # Validação do tipo de banco
        if self.db_type not in ['postgresql', 'mysql']:
            raise ValueError(
                f"Tipo de banco '{self.db_type}' não suportado. "
                "Use 'postgresql' ou 'mysql'."
            )
        
        self.engine: Optional[Engine] = None
        self._is_connected: bool = False
        
        logger.info(
            f"DatabaseConnector inicializado para {self.db_type} "
            f"em {self.host}:{self.port}/{self.database}"
        )
    
    def _build_connection_string(self) -> str:
        """
        Constrói a string de conexão SQLAlchemy.
        
        Returns:
            String de conexão formatada para o tipo de banco especificado.
        
        Raises:
            ValueError: Se o tipo de banco não for suportado.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> conn_string = connector._build_connection_string()
            >>> print(conn_string)
            postgresql://user:***@localhost:5432/mydb
        """
        # Codifica senha para tratar caracteres especiais
        encoded_password = quote_plus(self._password)
        
        if self.db_type == 'postgresql':
            driver = 'postgresql+psycopg2'
        elif self.db_type == 'mysql':
            driver = 'mysql+pymysql'
        else:
            raise ValueError(f"Tipo de banco '{self.db_type}' não suportado")
        
        connection_string = (
            f"{driver}://{self.username}:{encoded_password}"
            f"@{self.host}:{self.port}/{self.database}"
        )
        
        # Log sem expor a senha
        safe_log = connection_string.replace(encoded_password, '***')
        logger.debug(f"Connection string construída: {safe_log}")
        
        return connection_string
    
    def connect(self) -> None:
        """
        Estabelece conexão com o banco de dados com retry logic.
        
        Cria um engine SQLAlchemy com connection pooling configurado e tenta
        estabelecer conexão com retry automático em caso de falha.
        
        Raises:
            DatabaseConnectionError: Se não conseguir conectar após todas as tentativas.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> connector.connect()
            >>> print("Conexão estabelecida com sucesso!")
        """
        if self._is_connected:
            logger.warning("Já existe uma conexão ativa. Ignorando nova tentativa.")
            return
        
        connection_string = self._build_connection_string()
        
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                logger.info(
                    f"Tentativa {attempt}/{self.MAX_RETRIES} de conexão com "
                    f"{self.db_type} em {self.host}:{self.port}"
                )
                
                # Criação do engine com pooling
                self.engine = create_engine(
                    connection_string,
                    poolclass=pool.QueuePool,
                    pool_size=self.pool_size,
                    max_overflow=self.max_overflow,
                    pool_timeout=self.pool_timeout,
                    pool_recycle=self.pool_recycle,
                    echo=False,  # Set True para debug SQL
                    pool_pre_ping=True  # Verifica conexões antes de usar
                )
                
                # Testa a conexão
                with self.engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                
                self._is_connected = True
                logger.info(
                    f"Conexão estabelecida com sucesso com {self.db_type} "
                    f"em {self.host}:{self.port}/{self.database}"
                )
                return
                
            except OperationalError as e:
                delay = self.RETRY_DELAY * (self.BACKOFF_MULTIPLIER ** (attempt - 1))
                
                if attempt < self.MAX_RETRIES:
                    logger.warning(
                        f"Falha na tentativa {attempt}. "
                        f"Tentando novamente em {delay} segundos..."
                    )
                    time.sleep(delay)
                else:
                    raise DatabaseConnectionError(
                        f"Falha ao conectar após {self.MAX_RETRIES} tentativas",
                        e
                    )
                    
            except SQLAlchemyError as e:
                raise DatabaseConnectionError(
                    f"Erro SQLAlchemy ao conectar: {str(e)}",
                    e
                )
            except Exception as e:
                raise DatabaseConnectionError(
                    f"Erro inesperado ao conectar: {str(e)}",
                    e
                )
    
    def disconnect(self) -> None:
        """
        Fecha a conexão com o banco de dados e libera recursos.
        
        Dispõe o engine SQLAlchemy e todas as conexões do pool.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> connector.connect()
            >>> # ... realizar operações ...
            >>> connector.disconnect()
            >>> print("Conexão encerrada com sucesso!")
        """
        if not self._is_connected:
            logger.warning("Não há conexão ativa para desconectar.")
            return
        
        try:
            if self.engine:
                self.engine.dispose()
                logger.info("Engine SQLAlchemy descartado e conexões fechadas")
            
            self._is_connected = False
            self.engine = None
            
            logger.info("Desconexão realizada com sucesso")
            
        except Exception as e:
            logger.error(f"Erro ao desconectar: {str(e)}", exc_info=True)
            raise DatabaseConnectionError(
                "Erro ao desconectar do banco de dados",
                e
            )
    
    def get_engine(self) -> Engine:
        """
        Retorna o engine SQLAlchemy.
        
        Returns:
            Engine SQLAlchemy configurado.
        
        Raises:
            DatabaseConnectionError: Se não houver conexão ativa.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> connector.connect()
            >>> engine = connector.get_engine()
            >>> print(f"Engine: {engine}")
        """
        if not self._is_connected or self.engine is None:
            raise DatabaseConnectionError(
                "Não há conexão ativa. Chame connect() primeiro."
            )
        
        return self.engine
    
    def get_inspector(self) -> Inspector:
        """
        Retorna um Inspector SQLAlchemy para reflexão do schema.
        
        O Inspector permite explorar a estrutura do banco de dados
        (tabelas, colunas, constraints, etc.) sem executar queries.
        
        Returns:
            Inspector SQLAlchemy configurado para o banco conectado.
        
        Raises:
            DatabaseConnectionError: Se não houver conexão ativa.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> connector.connect()
            >>> inspector = connector.get_inspector()
            >>> 
            >>> # Listar tabelas
            >>> tables = inspector.get_table_names()
            >>> print(f"Tabelas: {tables}")
            >>> 
            >>> # Inspecionar colunas de uma tabela
            >>> columns = inspector.get_columns('users')
            >>> for col in columns:
            ...     print(f"{col['name']}: {col['type']}")
        """
        engine = self.get_engine()
        
        try:
            inspector = inspect(engine)
            logger.debug("Inspector SQLAlchemy criado com sucesso")
            return inspector
            
        except Exception as e:
            raise DatabaseConnectionError(
                "Erro ao criar Inspector SQLAlchemy",
                e
            )
    
    @contextmanager
    def get_connection(self) -> Generator[Connection, None, None]:
        """
        Context manager para gerenciamento seguro de conexões.
        
        Retorna uma conexão do pool que é automaticamente devolvida
        ao pool ao sair do contexto, garantindo liberação de recursos.
        
        Yields:
            Connection SQLAlchemy do pool.
        
        Raises:
            DatabaseConnectionError: Se não houver conexão ativa ou erro ao obter conexão.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> connector.connect()
            >>> 
            >>> with connector.get_connection() as conn:
            ...     result = conn.execute(text("SELECT * FROM users WHERE id = :id"), 
            ...                          {"id": 1})
            ...     for row in result:
            ...         print(row)
            >>> 
            >>> # Conexão automaticamente devolvida ao pool
        """
        engine = self.get_engine()
        
        connection = None
        try:
            connection = engine.connect()
            logger.debug("Conexão obtida do pool")
            yield connection
            
        except SQLAlchemyError as e:
            logger.error(f"Erro SQLAlchemy na conexão: {str(e)}", exc_info=True)
            raise DatabaseConnectionError(
                "Erro ao executar operação no banco de dados",
                e
            )
            
        except Exception as e:
            logger.error(f"Erro inesperado na conexão: {str(e)}", exc_info=True)
            raise DatabaseConnectionError(
                "Erro inesperado ao usar conexão",
                e
            )
            
        finally:
            if connection:
                connection.close()
                logger.debug("Conexão devolvida ao pool")
    
    def test_connection(self) -> bool:
        """
        Testa a conectividade com o banco de dados.
        
        Executa uma query simples para verificar se a conexão está funcional.
        Útil para health checks e validação de configurações.
        
        Returns:
            True se a conexão está funcional, False caso contrário.
        
        Exemplo:
            >>> connector = DatabaseConnector(config)
            >>> 
            >>> if connector.test_connection():
            ...     print("Banco de dados acessível!")
            ... else:
            ...     print("Falha ao acessar banco de dados.")
        """
        try:
            # Tenta conectar se ainda não estiver conectado
            if not self._is_connected:
                self.connect()
            
            # Executa query de teste
            with self.get_connection() as conn:
                result = conn.execute(text("SELECT 1"))
                result.fetchone()
            
            logger.info("Teste de conexão: SUCESSO")
            return True
            
        except DatabaseConnectionError as e:
            logger.error(f"Teste de conexão: FALHA - {e.message}")
            return False
            
        except Exception as e:
            logger.error(f"Teste de conexão: FALHA - {str(e)}", exc_info=True)
            return False
    
    def __enter__(self):
        """
        Permite usar a classe como context manager.
        
        Exemplo:
            >>> config = {...}
            >>> with DatabaseConnector(config) as connector:
            ...     inspector = connector.get_inspector()
            ...     tables = inspector.get_table_names()
            ...     print(tables)
            >>> # Conexão automaticamente fechada
        """
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Fecha conexão ao sair do contexto."""
        self.disconnect()
    
    def __repr__(self) -> str:
        """Representação string do objeto."""
        status = "conectado" if self._is_connected else "desconectado"
        return (
            f"DatabaseConnector(db_type='{self.db_type}', "
            f"host='{self.host}', port={self.port}, "
            f"database='{self.database}', status='{status}')"
        )


# Exemplo de uso do módulo
if __name__ == "__main__":
    """
    Exemplo de uso do DatabaseConnector.
    
    Este bloco demonstra os principais casos de uso do módulo.
    """
    
    # Configuração de exemplo (substituir com valores reais)
    example_config = {
        'db_type': 'postgresql',
        'host': 'localhost',
        'port': 5432,
        'database': 'example_db',
        'username': 'example_user',
        'password': 'example_password',
        'pool_size': 5,
        'max_overflow': 10
    }
    
    try:
        # Exemplo 1: Uso básico
        print("\n=== Exemplo 1: Uso Básico ===")
        connector = DatabaseConnector(example_config)
        connector.connect()
        
        if connector.test_connection():
            print("✅ Conexão testada com sucesso!")
        
        inspector = connector.get_inspector()
        tables = inspector.get_table_names()
        print(f"📊 Tabelas encontradas: {tables}")
        
        connector.disconnect()
        
        # Exemplo 2: Context manager
        print("\n=== Exemplo 2: Context Manager ===")
        with DatabaseConnector(example_config) as conn:
            with conn.get_connection() as db_conn:
                result = db_conn.execute(text("SELECT version()"))
                version = result.fetchone()
                print(f"🔢 Versão do banco: {version[0]}")
        
        print("✅ Exemplos executados com sucesso!")
        
    except DatabaseConnectionError as e:
        print(f"❌ Erro de conexão: {e.message}")
        if e.original_exception:
            print(f"   Causa: {e.original_exception}")
    
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")