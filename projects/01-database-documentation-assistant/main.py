# ARQUIVO 2: main.py
# Copie todo este código abaixo:

"""
Database Documentation Assistant - Aplicação Principal.

Script principal que orquestra todo o fluxo de extração, análise e
geração de documentação de banco de dados usando IA.

Autor: Paulo César Mendes de Sousa Júnior
Data: 2024-11-27
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional
import yaml
from datetime import datetime

from src.database_connector import DatabaseConnector, ConnectionConfig
from src.schema_extractor import SchemaExtractor
from src.llm_documentation_generator import (
    create_documentation_generator,
    LLMConfig
)

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('documentation_generation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class DocumentationAssistant:
    """
    Assistente principal para geração de documentação de banco de dados.
    
    Coordena todas as etapas do processo: conexão, extração, análise e geração.
    """
    
    def __init__(self, config_path: str):
        """
        Inicializa o assistente com arquivo de configuração.
        
        Args:
            config_path: Caminho para arquivo YAML de configuração
            
        Raises:
            FileNotFoundError: Se arquivo de configuração não existir
            ValueError: Se configuração for inválida
        """
        self.config = self._load_config(config_path)
        self.output_dir = Path(self.config.get('output_dir', 'output'))
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Documentation Assistant inicializado com config: {config_path}")
    
    def _load_config(self, config_path: str) -> dict:
        """
        Carrega e valida arquivo de configuração.
        
        Args:
            config_path: Caminho para arquivo YAML
            
        Returns:
            Dicionário com configurações
            
        Raises:
            FileNotFoundError: Se arquivo não existir
            ValueError: Se YAML for inválido
        """
        config_file = Path(config_path)
        
        if not config_file.exists():
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado: {config_path}"
            )
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            # Validar campos obrigatórios
            required_fields = ['database', 'llm']
            for field in required_fields:
                if field not in config:
                    raise ValueError(f"Campo obrigatório ausente no config: {field}")
            
            return config
            
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao parsear YAML: {e}")
    
    def run(self):
        """
        Executa o fluxo completo de geração de documentação.
        
        Etapas:
        1. Conecta ao banco de dados
        2. Extrai schema completo
        3. Gera documentação com LLM
        4. Salva resultados em arquivos
        
        Raises:
            Exception: Se houver erro em qualquer etapa
        """
        try:
            logger.info("=" * 80)
            logger.info("INICIANDO GERAÇÃO DE DOCUMENTAÇÃO DE BANCO DE DADOS")
            logger.info("=" * 80)
            
            # Etapa 1: Conectar ao banco de dados
            logger.info("\n[1/4] Conectando ao banco de dados...")
            connector = self._create_database_connector()
            
            # Etapa 2: Extrair schema
            logger.info("\n[2/4] Extraindo schema do banco de dados...")
            schema = self._extract_schema(connector)
            
            # Etapa 3: Gerar documentação com LLM
            logger.info("\n[3/4] Gerando documentação com IA...")
            documentation = self._generate_documentation(schema)
            
            # Etapa 4: Salvar resultados
            logger.info("\n[4/4] Salvando documentação...")
            self._save_documentation(documentation, schema)
            
            logger.info("\n" + "=" * 80)
            logger.info("✓ DOCUMENTAÇÃO GERADA COM SUCESSO!")
            logger.info(f"✓ Arquivos salvos em: {self.output_dir.absolute()}")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error(f"\n✗ ERRO FATAL: {str(e)}")
            raise
    
    def _create_database_connector(self) -> DatabaseConnector:
        """
        Cria conector de banco de dados baseado na configuração.
        
        Returns:
            Instância de DatabaseConnector conectada
        """
        db_config = self.config['database']
        
        conn_config = ConnectionConfig(
            db_type=db_config['type'],
            host=db_config.get('host', 'localhost'),
            port=db_config.get('port'),
            database=db_config['database'],
            username=db_config['username'],
            password=db_config['password']
        )
        
        connector = DatabaseConnector(conn_config)
        connector.connect()
        
        logger.info(f"✓ Conectado a {db_config['type']}: {db_config['database']}")
        
        return connector
    
    def _extract_schema(self, connector: DatabaseConnector) -> dict:
        """
        Extrai schema completo do banco de dados.
        
        Args:
            connector: Conector de banco de dados ativo
            
        Returns:
            Dicionário com schema completo
        """
        extractor = SchemaExtractor(connector)
        
        # Extrair schema completo
        schema = extractor.extract_full_schema()
        
        # Estatísticas
        table_count = len(schema.get('tables', []))
        total_columns = sum(
            len(table.get('columns', [])) 
            for table in schema.get('tables', [])
        )
        
        logger.info(f"✓ Schema extraído: {table_count} tabelas, {total_columns} colunas")
        
        return schema
    
    def _generate_documentation(self, schema: dict) -> dict:
        """
        Gera documentação usando LLM.
        
        Args:
            schema: Schema do banco de dados
            
        Returns:
            Dicionário com documentação gerada
        """
        llm_config = self.config['llm']
        
        generator = create_documentation_generator(
            provider=llm_config.get('provider', 'openai'),
            model=llm_config.get('model', 'gpt-4'),
            api_key=llm_config.get('api_key')
        )
        
        documentation = {
            'database_overview': None,
            'tables': []
        }
        
        # Gerar visão geral do banco
        logger.info("  → Gerando visão geral do banco de dados...")
        documentation['database_overview'] = generator.generate_database_overview(schema)
        
        # Gerar documentação de cada tabela
        tables = schema.get('tables', [])
        for idx, table in enumerate(tables, 1):
            logger.info(f"  → Tabela {idx}/{len(tables)}: {table['name']}")
            
            table_doc = generator.generate_table_documentation(
                table_schema=table,
                database_context=schema.get('name')
            )
            
            documentation['tables'].append({
                'schema': table,
                'documentation': table_doc
            })
        
        logger.info(f"✓ Documentação gerada para {len(tables)} tabelas")
        
        return documentation
    
    def _save_documentation(self, documentation: dict, schema: dict):
        """
        Salva documentação em arquivos.
        
        Args:
            documentation: Documentação gerada
            schema: Schema original
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Salvar visão geral
        overview_file = self.output_dir / f"database_overview_{timestamp}.md"
        with open(overview_file, 'w', encoding='utf-8') as f:
            f.write("# Visão Geral do Banco de Dados\n\n")
            f.write(documentation['database_overview'])
        
        logger.info(f"  ✓ Visão geral: {overview_file.name}")
        
        # Salvar documentação de tabelas
        tables_file = self.output_dir / f"tables_documentation_{timestamp}.md"
        with open(tables_file, 'w', encoding='utf-8') as f:
            f.write("# Documentação de Tabelas\n\n")
            
            for table_info in documentation['tables']:
                table_name = table_info['schema']['name']
                doc = table_info['documentation']
                
                f.write(f"## {table_name}\n\n")
                f.write(f"**Propósito:** {doc.purpose}\n\n")
                f.write(f"**Contexto de Negócio:** {doc.business_context}\n\n")
                
                if doc.relationships:
                    f.write("**Relacionamentos:**\n")
                    for rel in doc.relationships:
                        f.write(f"- {rel}\n")
                    f.write("\n")
                
                if doc.usage_examples:
                    f.write("**Exemplos de Uso:**\n")
                    for example in doc.usage_examples:
                        f.write(f"- {example}\n")
                    f.write("\n")
                
                f.write("---\n\n")
        
        logger.info(f"  ✓ Tabelas: {tables_file.name}")
        
        # Salvar schema raw (backup)
        schema_file = self.output_dir / f"schema_raw_{timestamp}.yaml"
        with open(schema_file, 'w', encoding='utf-8') as f:
            yaml.dump(schema, f, allow_unicode=True, default_flow_style=False)
        
        logger.info(f"  ✓ Schema raw: {schema_file.name}")


def main():
    """Função principal - entry point da aplicação."""
    
    parser = argparse.ArgumentParser(
        description='Database Documentation Assistant - Gera documentação inteligente de bancos de dados',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  # Usando arquivo de configuração padrão
  python main.py
  
  # Especificando arquivo de configuração customizado
  python main.py --config meu_config.yaml
  
  # Com nível de log detalhado
  python main.py --config config.yaml --verbose

Autor: Paulo César Mendes de Sousa Júnior
        """
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='config.yaml',
        help='Caminho para arquivo de configuração YAML (default: config.yaml)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Ativa modo verbose (DEBUG level)'
    )
    
    args = parser.parse_args()
    
    # Ajustar nível de log se verbose
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Modo verbose ativado")
    
    try:
        # Criar e executar assistente
        assistant = DocumentationAssistant(args.config)
        assistant.run()
        
        return 0
        
    except KeyboardInterrupt:
        logger.warning("\n✗ Operação cancelada pelo usuário")
        return 1
        
    except Exception as e:
        logger.error(f"\n✗ Erro fatal: {str(e)}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())