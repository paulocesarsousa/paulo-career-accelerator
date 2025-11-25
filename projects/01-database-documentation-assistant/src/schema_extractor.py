"""
Módulo de Extração de Schema de Bancos de Dados.

Este módulo extrai metadados completos de bancos de dados PostgreSQL e MySQL,
incluindo tabelas, colunas, tipos de dados, constraints, índices e relacionamentos.

Classes:
    SchemaExtractor: Classe principal para extração de schema.

Exemplo de uso:
    >>> from database_connector import DatabaseConnector
    >>> from schema_extractor import SchemaExtractor
    >>> 
    >>> config = {'db_type': 'postgresql', 'host': 'localhost', ...}
    >>> connector = DatabaseConnector(config)
    >>> connector.connect()
    >>> 
    >>> extractor = SchemaExtractor(connector)
    >>> schema = extractor.extract_full_schema()
    >>> print(f"Tabelas encontradas: {len(schema['tables'])}")
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict

from sqlalchemy.engine import Inspector

from database_connector import DatabaseConnector


# Configuração de logging
logger = logging.getLogger(__name__)


@dataclass
class ColumnInfo:
    """
    Informações de uma coluna do banco de dados.
    
    Attributes:
        name: Nome da coluna
        type: Tipo de dado da coluna
        nullable: Se aceita valores NULL
        default: Valor padrão da coluna
        autoincrement: Se é auto-incremento
        comment: Comentário/descrição da coluna
    """
    name: str
    type: str
    nullable: bool
    default: Optional[Any] = None
    autoincrement: Optional[bool] = False
    comment: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte para dicionário."""
        return asdict(self)


@dataclass
class ForeignKeyInfo:
    """
    Informações de chave estrangeira.
    
    Attributes:
        name: Nome da constraint
        constrained_columns: Colunas da tabela atual
        referred_table: Tabela referenciada
        referred_columns: Colunas referenciadas
    """
    name: Optional[str]
    constrained_columns: List[str]
    referred_table: str
    referred_columns: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte para dicionário."""
        return asdict(self)


@dataclass
class IndexInfo:
    """
    Informações de índice.
    
    Attributes:
        name: Nome do índice
        column_names: Colunas do índice
        unique: Se é índice único
    """
    name: str
    column_names: List[str]
    unique: bool
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte para dicionário."""
        return asdict(self)


@dataclass
class TableInfo:
    """
    Informações completas de uma tabela.
    
    Attributes:
        name: Nome da tabela
        schema: Schema da tabela
        columns: Lista de colunas
        primary_keys: Chaves primárias
        foreign_keys: Chaves estrangeiras
        indexes: Índices da tabela
        comment: Comentário da tabela
    """
    name: str
    schema: Optional[str] = None
    columns: List[ColumnInfo] = field(default_factory=list)
    primary_keys: List[str] = field(default_factory=list)
    foreign_keys: List[ForeignKeyInfo] = field(default_factory=list)
    indexes: List[IndexInfo] = field(default_factory=list)
    comment: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte para dicionário com nested conversions."""
        return {
            'name': self.name,
            'schema': self.schema,
            'columns': [col.to_dict() for col in self.columns],
            'primary_keys': self.primary_keys,
            'foreign_keys': [fk.to_dict() for fk in self.foreign_keys],
            'indexes': [idx.to_dict() for idx in self.indexes],
            'comment': self.comment
        }


class SchemaExtractor:
    """
    Extrator de schema de bancos de dados.
    
    Utiliza SQLAlchemy Inspector para extrair metadados completos
    de bancos de dados PostgreSQL e MySQL.
    
    Attributes:
        connector: Instância de DatabaseConnector
        inspector: Inspector SQLAlchemy
    
    Exemplo:
        >>> connector = DatabaseConnector(config)
        >>> connector.connect()
        >>> 
        >>> extractor = SchemaExtractor(connector)
        >>> schema = extractor.extract_full_schema()
        >>> 
        >>> # Acessar informações
        >>> for table in schema['tables']:
        ...     print(f"Tabela: {table['name']}")
        ...     for col in table['columns']:
        ...         print(f"  - {col['name']}: {col['type']}")
    """
    
    def __init__(self, connector: DatabaseConnector):
        """
        Inicializa o extrator com um conector de banco.
        
        Args:
            connector: Instância conectada de DatabaseConnector
        
        Raises:
            ValueError: Se o connector não estiver conectado
        """
        if not connector._is_connected:
            raise ValueError("DatabaseConnector deve estar conectado")
        
        self.connector = connector
        self.inspector: Inspector = connector.get_inspector()
        
        logger.info(
            f"SchemaExtractor inicializado para {connector.db_type}"
        )
    
    def extract_table_names(self, schema: Optional[str] = None) -> List[str]:
        """
        Extrai lista de nomes de tabelas.
        
        Args:
            schema: Schema específico (opcional)
        
        Returns:
            Lista de nomes de tabelas
        
        Exemplo:
            >>> tables = extractor.extract_table_names()
            >>> print(tables)
            ['users', 'orders', 'products']
        """
        try:
            tables = self.inspector.get_table_names(schema=schema)
            logger.info(f"Encontradas {len(tables)} tabelas")
            return tables
        except Exception as e:
            logger.error(f"Erro ao extrair nomes de tabelas: {e}")
            return []
    
    def extract_columns(
        self, 
        table_name: str, 
        schema: Optional[str] = None
    ) -> List[ColumnInfo]:
        """
        Extrai informações de colunas de uma tabela.
        
        Args:
            table_name: Nome da tabela
            schema: Schema da tabela (opcional)
        
        Returns:
            Lista de ColumnInfo
        
        Exemplo:
            >>> columns = extractor.extract_columns('users')
            >>> for col in columns:
            ...     print(f"{col.name}: {col.type}")
        """
        try:
            raw_columns = self.inspector.get_columns(
                table_name, 
                schema=schema
            )
            
            columns = []
            for col in raw_columns:
                column_info = ColumnInfo(
                    name=col['name'],
                    type=str(col['type']),
                    nullable=col.get('nullable', True),
                    default=col.get('default'),
                    autoincrement=col.get('autoincrement', False),
                    comment=col.get('comment')
                )
                columns.append(column_info)
            
            logger.debug(
                f"Extraídas {len(columns)} colunas da tabela {table_name}"
            )
            return columns
            
        except Exception as e:
            logger.error(
                f"Erro ao extrair colunas de {table_name}: {e}"
            )
            return []
    
    def extract_primary_keys(
        self, 
        table_name: str, 
        schema: Optional[str] = None
    ) -> List[str]:
        """
        Extrai chaves primárias de uma tabela.
        
        Args:
            table_name: Nome da tabela
            schema: Schema da tabela (opcional)
        
        Returns:
            Lista de nomes de colunas que são chaves primárias
        
        Exemplo:
            >>> pk = extractor.extract_primary_keys('users')
            >>> print(pk)
            ['id']
        """
        try:
            pk_constraint = self.inspector.get_pk_constraint(
                table_name, 
                schema=schema
            )
            
            pk_columns = pk_constraint.get('constrained_columns', [])
            logger.debug(
                f"Chaves primárias de {table_name}: {pk_columns}"
            )
            return pk_columns
            
        except Exception as e:
            logger.error(
                f"Erro ao extrair chaves primárias de {table_name}: {e}"
            )
            return []
    
    def extract_foreign_keys(
        self, 
        table_name: str, 
        schema: Optional[str] = None
    ) -> List[ForeignKeyInfo]:
        """
        Extrai chaves estrangeiras de uma tabela.
        
        Args:
            table_name: Nome da tabela
            schema: Schema da tabela (opcional)
        
        Returns:
            Lista de ForeignKeyInfo
        
        Exemplo:
            >>> fks = extractor.extract_foreign_keys('orders')
            >>> for fk in fks:
            ...     print(f"{fk.constrained_columns} -> "
            ...           f"{fk.referred_table}.{fk.referred_columns}")
        """
        try:
            raw_fks = self.inspector.get_foreign_keys(
                table_name, 
                schema=schema
            )
            
            foreign_keys = []
            for fk in raw_fks:
                fk_info = ForeignKeyInfo(
                    name=fk.get('name'),
                    constrained_columns=fk['constrained_columns'],
                    referred_table=fk['referred_table'],
                    referred_columns=fk['referred_columns']
                )
                foreign_keys.append(fk_info)
            
            logger.debug(
                f"Extraídas {len(foreign_keys)} FKs de {table_name}"
            )
            return foreign_keys
            
        except Exception as e:
            logger.error(
                f"Erro ao extrair FKs de {table_name}: {e}"
            )
            return []
    
    def extract_indexes(
        self, 
        table_name: str, 
        schema: Optional[str] = None
    ) -> List[IndexInfo]:
        """
        Extrai índices de uma tabela.
        
        Args:
            table_name: Nome da tabela
            schema: Schema da tabela (opcional)
        
        Returns:
            Lista de IndexInfo
        
        Exemplo:
            >>> indexes = extractor.extract_indexes('users')
            >>> for idx in indexes:
            ...     print(f"{idx.name}: {idx.column_names}")
        """
        try:
            raw_indexes = self.inspector.get_indexes(
                table_name, 
                schema=schema
            )
            
            indexes = []
            for idx in raw_indexes:
                index_info = IndexInfo(
                    name=idx['name'],
                    column_names=idx['column_names'],
                    unique=idx.get('unique', False)
                )
                indexes.append(index_info)
            
            logger.debug(
                f"Extraídos {len(indexes)} índices de {table_name}"
            )
            return indexes
            
        except Exception as e:
            logger.error(
                f"Erro ao extrair índices de {table_name}: {e}"
            )
            return []
    
    def extract_table_info(
        self, 
        table_name: str, 
        schema: Optional[str] = None
    ) -> TableInfo:
        """
        Extrai informações completas de uma tabela.
        
        Args:
            table_name: Nome da tabela
            schema: Schema da tabela (opcional)
        
        Returns:
            TableInfo com todos os metadados
        
        Exemplo:
            >>> table = extractor.extract_table_info('users')
            >>> print(f"Tabela: {table.name}")
            >>> print(f"Colunas: {len(table.columns)}")
            >>> print(f"PKs: {table.primary_keys}")
        """
        try:
            # Extrair comment da tabela (se disponível)
            comment = None
            try:
                comment = self.inspector.get_table_comment(
                    table_name, 
                    schema=schema
                ).get('text')
            except:
                pass
            
            table_info = TableInfo(
                name=table_name,
                schema=schema,
                columns=self.extract_columns(table_name, schema),
                primary_keys=self.extract_primary_keys(table_name, schema),
                foreign_keys=self.extract_foreign_keys(table_name, schema),
                indexes=self.extract_indexes(table_name, schema),
                comment=comment
            )
            
            logger.info(f"Extraídas informações completas de {table_name}")
            return table_info
            
        except Exception as e:
            logger.error(
                f"Erro ao extrair informações de {table_name}: {e}",
                exc_info=True
            )
            raise
    
    def extract_full_schema(
        self, 
        schema: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Extrai schema completo do banco de dados.
        
        Args:
            schema: Schema específico (opcional)
        
        Returns:
            Dicionário com todas as tabelas e metadados
        
        Exemplo:
            >>> schema = extractor.extract_full_schema()
            >>> print(f"Database: {schema['database']}")
            >>> print(f"Tabelas: {len(schema['tables'])}")
            >>> 
            >>> # Salvar como JSON
            >>> import json
            >>> with open('schema.json', 'w') as f:
            ...     json.dump(schema, f, indent=2)
        """
        logger.info("Iniciando extração completa do schema")
        
        try:
            table_names = self.extract_table_names(schema)
            
            tables = []
            for table_name in table_names:
                try:
                    table_info = self.extract_table_info(table_name, schema)
                    tables.append(table_info.to_dict())
                except Exception as e:
                    logger.warning(
                        f"Pulando tabela {table_name} devido a erro: {e}"
                    )
                    continue
            
            full_schema = {
                'database': self.connector.database,
                'db_type': self.connector.db_type,
                'schema': schema,
                'table_count': len(tables),
                'tables': tables
            }
            
            logger.info(
                f"Schema extraído com sucesso: "
                f"{len(tables)} tabelas processadas"
            )
            
            return full_schema
            
        except Exception as e:
            logger.error(
                f"Erro ao extrair schema completo: {e}",
                exc_info=True
            )
            raise


# Exemplo de uso
if __name__ == "__main__":
    """Exemplo de uso do SchemaExtractor."""
    
    from database_connector import DatabaseConnector
    
    # Configuração de exemplo
    config = {
        'db_type': 'postgresql',
        'host': 'localhost',
        'port': 5432,
        'database': 'example_db',
        'username': 'user',
        'password': 'password'
    }
    
    try:
        # Conectar ao banco
        print("Conectando ao banco de dados...")
        connector = DatabaseConnector(config)
        connector.connect()
        
        # Extrair schema
        print("Extraindo schema...")
        extractor = SchemaExtractor(connector)
        schema = extractor.extract_full_schema()
        
        # Mostrar resultados
        print(f"\n✅ Database: {schema['database']}")
        print(f"✅ Tipo: {schema['db_type']}")
        print(f"✅ Tabelas: {schema['table_count']}")
        
        print("\n📊 Tabelas encontradas:")
        for table in schema['tables']:
            print(f"\n  📋 {table['name']}")
            print(f"     Colunas: {len(table['columns'])}")
            print(f"     PKs: {table['primary_keys']}")
            print(f"     FKs: {len(table['foreign_keys'])}")
            print(f"     Índices: {len(table['indexes'])}")
        
        # Salvar como JSON
        import json
        with open('database_schema.json', 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        print("\n✅ Schema salvo em 'database_schema.json'")
        
        connector.disconnect()
        print("✅ Desconectado")
        
    except Exception as e:
        print(f"❌ Erro: {e}")