# ARQUIVO 1: llm_documentation_generator.py
# Copie todo este código abaixo:

"""
Módulo de Geração de Documentação com LLM.

Este módulo utiliza LangChain e modelos de linguagem para gerar
documentação inteligente e contextualizada de esquemas de banco de dados.

Autor: Paulo César Mendes de Sousa Júnior
Data: 2024-11-27
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging
from pathlib import Path

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TableDocumentation(BaseModel):
    """Modelo de documentação de tabela."""
    
    table_name: str = Field(description="Nome da tabela")
    purpose: str = Field(description="Propósito e uso da tabela")
    business_context: str = Field(description="Contexto de negócio")
    relationships: List[str] = Field(
        description="Relacionamentos com outras tabelas",
        default_factory=list
    )
    usage_examples: List[str] = Field(
        description="Exemplos de uso e queries comuns",
        default_factory=list
    )


class ColumnDocumentation(BaseModel):
    """Modelo de documentação de coluna."""
    
    column_name: str = Field(description="Nome da coluna")
    business_name: str = Field(description="Nome de negócio amigável")
    description: str = Field(description="Descrição detalhada")
    business_rules: List[str] = Field(
        description="Regras de negócio aplicáveis",
        default_factory=list
    )
    data_quality_notes: Optional[str] = Field(
        description="Notas sobre qualidade de dados",
        default=None
    )


@dataclass
class LLMConfig:
    """Configuração do modelo LLM."""
    
    provider: str = "openai"  # "openai" ou "anthropic"
    model: str = "gpt-4"
    temperature: float = 0.3
    max_tokens: int = 2000
    api_key: Optional[str] = None


class LLMDocumentationGenerator:
    """
    Gerador de documentação usando LLM.
    
    Utiliza modelos de linguagem avançados para gerar documentação
    contextualizada e inteligente de esquemas de banco de dados.
    """
    
    def __init__(self, config: LLMConfig):
        """
        Inicializa o gerador de documentação.
        
        Args:
            config: Configuração do modelo LLM
            
        Raises:
            ValueError: Se a configuração for inválida
        """
        self.config = config
        self.llm = self._initialize_llm()
        
        logger.info(
            f"LLM Documentation Generator inicializado com "
            f"provider={config.provider}, model={config.model}"
        )
    
    def _initialize_llm(self):
        """
        Inicializa o modelo LLM baseado na configuração.
        
        Returns:
            Instância do modelo LLM configurado
            
        Raises:
            ValueError: Se o provider não for suportado
        """
        if self.config.provider == "openai":
            return ChatOpenAI(
                model=self.config.model,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
                api_key=self.config.api_key
            )
        elif self.config.provider == "anthropic":
            return ChatAnthropic(
                model=self.config.model,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
                api_key=self.config.api_key
            )
        else:
            raise ValueError(
                f"Provider não suportado: {self.config.provider}. "
                f"Use 'openai' ou 'anthropic'."
            )
    
    def generate_table_documentation(
        self,
        table_schema: Dict[str, Any],
        database_context: Optional[str] = None
    ) -> TableDocumentation:
        """
        Gera documentação completa para uma tabela.
        
        Args:
            table_schema: Schema da tabela incluindo colunas e constraints
            database_context: Contexto adicional sobre o banco de dados
            
        Returns:
            Documentação estruturada da tabela
            
        Raises:
            Exception: Se houver erro na geração da documentação
        """
        try:
            logger.info(f"Gerando documentação para tabela: {table_schema.get('name')}")
            
            # Parser para estruturar a saída
            parser = PydanticOutputParser(pydantic_object=TableDocumentation)
            
            # Template do prompt
            template = """
Você é um especialista em documentação de bancos de dados e modelagem de dados.

Analise o seguinte schema de tabela e gere documentação completa e profissional em português:

Nome da Tabela: {table_name}
Colunas: {columns}
Chaves Primárias: {primary_keys}
Chaves Estrangeiras: {foreign_keys}
Índices: {indexes}

{context}

Gere documentação estruturada incluindo:
1. Propósito e uso da tabela
2. Contexto de negócio
3. Relacionamentos com outras tabelas
4. Exemplos de uso e queries comuns

{format_instructions}
"""
            
            prompt = PromptTemplate(
                template=template,
                input_variables=[
                    "table_name", "columns", "primary_keys", 
                    "foreign_keys", "indexes", "context"
                ],
                partial_variables={
                    "format_instructions": parser.get_format_instructions()
                }
            )
            
            # Chain para processamento
            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            # Preparar contexto
            context = f"Contexto do Banco: {database_context}" if database_context else ""
            
            # Executar geração
            result = chain.run(
                table_name=table_schema.get("name", "Desconhecida"),
                columns=self._format_columns(table_schema.get("columns", [])),
                primary_keys=", ".join(table_schema.get("primary_keys", [])),
                foreign_keys=self._format_foreign_keys(
                    table_schema.get("foreign_keys", [])
                ),
                indexes=self._format_indexes(table_schema.get("indexes", [])),
                context=context
            )
            
            # Parse da resposta
            documentation = parser.parse(result)
            
            logger.info(
                f"Documentação gerada com sucesso para: "
                f"{table_schema.get('name')}"
            )
            
            return documentation
            
        except Exception as e:
            logger.error(
                f"Erro ao gerar documentação da tabela "
                f"{table_schema.get('name')}: {str(e)}"
            )
            raise
    
    def generate_column_documentation(
        self,
        column_info: Dict[str, Any],
        table_context: Optional[str] = None
    ) -> ColumnDocumentation:
        """
        Gera documentação detalhada para uma coluna.
        
        Args:
            column_info: Informações da coluna (nome, tipo, constraints)
            table_context: Contexto da tabela à qual a coluna pertence
            
        Returns:
            Documentação estruturada da coluna
            
        Raises:
            Exception: Se houver erro na geração da documentação
        """
        try:
            logger.info(f"Gerando documentação para coluna: {column_info.get('name')}")
            
            parser = PydanticOutputParser(pydantic_object=ColumnDocumentation)
            
            template = """
Você é um especialista em dicionário de dados e governança de dados.

Analise a seguinte coluna e gere documentação profissional em português:

Nome da Coluna: {column_name}
Tipo de Dados: {data_type}
Nullable: {is_nullable}
Default: {default_value}
Constraints: {constraints}

{context}

Gere documentação incluindo:
1. Nome de negócio amigável
2. Descrição detalhada e propósito
3. Regras de negócio aplicáveis
4. Notas sobre qualidade de dados

{format_instructions}
"""
            
            prompt = PromptTemplate(
                template=template,
                input_variables=[
                    "column_name", "data_type", "is_nullable",
                    "default_value", "constraints", "context"
                ],
                partial_variables={
                    "format_instructions": parser.get_format_instructions()
                }
            )
            
            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            context = f"Contexto da Tabela: {table_context}" if table_context else ""
            
            result = chain.run(
                column_name=column_info.get("name", "Desconhecida"),
                data_type=column_info.get("type", "Desconhecido"),
                is_nullable="Sim" if column_info.get("nullable", True) else "Não",
                default_value=str(column_info.get("default", "Nenhum")),
                constraints=", ".join(column_info.get("constraints", [])),
                context=context
            )
            
            documentation = parser.parse(result)
            
            logger.info(
                f"Documentação gerada com sucesso para coluna: "
                f"{column_info.get('name')}"
            )
            
            return documentation
            
        except Exception as e:
            logger.error(
                f"Erro ao gerar documentação da coluna "
                f"{column_info.get('name')}: {str(e)}"
            )
            raise
    
    def generate_database_overview(
        self,
        database_schema: Dict[str, Any]
    ) -> str:
        """
        Gera visão geral do banco de dados completo.
        
        Args:
            database_schema: Schema completo do banco de dados
            
        Returns:
            Documentação em texto da visão geral do banco
            
        Raises:
            Exception: Se houver erro na geração
        """
        try:
            logger.info("Gerando visão geral do banco de dados")
            
            template = """
Você é um arquiteto de dados experiente.

Analise o schema completo do banco de dados e gere uma visão geral executiva em português:

Nome do Banco: {database_name}
Número de Tabelas: {table_count}
Tabelas Principais: {main_tables}
Relacionamentos: {relationships_count}

Gere um documento executivo incluindo:
1. Propósito geral do banco de dados
2. Principais áreas funcionais
3. Arquitetura de dados (padrões identificados)
4. Considerações de qualidade e governança
5. Recomendações de melhoria

Use linguagem técnica mas acessível.
"""
            
            prompt = PromptTemplate(
                template=template,
                input_variables=[
                    "database_name", "table_count",
                    "main_tables", "relationships_count"
                ]
            )
            
            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            tables = database_schema.get("tables", [])
            main_tables = ", ".join([t.get("name") for t in tables[:5]])
            
            result = chain.run(
                database_name=database_schema.get("name", "Desconhecido"),
                table_count=len(tables),
                main_tables=main_tables,
                relationships_count=self._count_relationships(database_schema)
            )
            
            logger.info("Visão geral gerada com sucesso")
            
            return result
            
        except Exception as e:
            logger.error(f"Erro ao gerar visão geral do banco: {str(e)}")
            raise
    
    def _format_columns(self, columns: List[Dict[str, Any]]) -> str:
        """Formata lista de colunas para o prompt."""
        if not columns:
            return "Nenhuma coluna disponível"
        
        formatted = []
        for col in columns:
            col_str = (
                f"- {col.get('name')} ({col.get('type')}) "
                f"{'NOT NULL' if not col.get('nullable', True) else 'NULL'}"
            )
            formatted.append(col_str)
        
        return "\n".join(formatted)
    
    def _format_foreign_keys(self, foreign_keys: List[Dict[str, Any]]) -> str:
        """Formata chaves estrangeiras para o prompt."""
        if not foreign_keys:
            return "Nenhuma chave estrangeira"
        
        formatted = []
        for fk in foreign_keys:
            fk_str = (
                f"- {fk.get('column')} -> "
                f"{fk.get('referenced_table')}.{fk.get('referenced_column')}"
            )
            formatted.append(fk_str)
        
        return "\n".join(formatted)
    
    def _format_indexes(self, indexes: List[Dict[str, Any]]) -> str:
        """Formata índices para o prompt."""
        if not indexes:
            return "Nenhum índice"
        
        formatted = []
        for idx in indexes:
            idx_str = (
                f"- {idx.get('name')}: "
                f"{', '.join(idx.get('columns', []))}"
            )
            formatted.append(idx_str)
        
        return "\n".join(formatted)
    
    def _count_relationships(self, database_schema: Dict[str, Any]) -> int:
        """Conta total de relacionamentos no banco."""
        count = 0
        for table in database_schema.get("tables", []):
            count += len(table.get("foreign_keys", []))
        return count


def create_documentation_generator(
    provider: str = "openai",
    model: str = "gpt-4",
    api_key: Optional[str] = None
) -> LLMDocumentationGenerator:
    """
    Factory function para criar gerador de documentação.
    
    Args:
        provider: Provider do LLM ("openai" ou "anthropic")
        model: Nome do modelo a ser usado
        api_key: Chave da API (opcional, usa variável de ambiente se None)
        
    Returns:
        Instância configurada do gerador
        
    Example:
        >>> generator = create_documentation_generator(
        ...     provider="openai",
        ...     model="gpt-4"
        ... )
        >>> doc = generator.generate_table_documentation(table_schema)
    """
    config = LLMConfig(
        provider=provider,
        model=model,
        api_key=api_key
    )
    
    return LLMDocumentationGenerator(config)