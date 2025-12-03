# ARQUIVO 3: test_llm_documentation_generator.py
# Copie todo este código abaixo:

"""
Testes para o módulo LLM Documentation Generator.

Suite de testes unitários e de integração para validar a geração
de documentação usando modelos de linguagem.

Autor: Paulo César Mendes de Sousa Júnior
Data: 2024-11-27
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any

from src.llm_documentation_generator import (
    LLMDocumentationGenerator,
    LLMConfig,
    TableDocumentation,
    ColumnDocumentation,
    create_documentation_generator
)


@pytest.fixture
def mock_llm_config():
    """Fixture para configuração mock do LLM."""
    return LLMConfig(
        provider="openai",
        model="gpt-4",
        temperature=0.3,
        api_key="test_api_key"
    )


@pytest.fixture
def sample_table_schema():
    """Fixture para schema de tabela exemplo."""
    return {
        "name": "users",
        "columns": [
            {
                "name": "id",
                "type": "INTEGER",
                "nullable": False,
                "default": None
            },
            {
                "name": "username",
                "type": "VARCHAR(50)",
                "nullable": False,
                "default": None
            },
            {
                "name": "email",
                "type": "VARCHAR(100)",
                "nullable": False,
                "default": None
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "nullable": False,
                "default": "CURRENT_TIMESTAMP"
            }
        ],
        "primary_keys": ["id"],
        "foreign_keys": [],
        "indexes": [
            {
                "name": "idx_username",
                "columns": ["username"]
            },
            {
                "name": "idx_email",
                "columns": ["email"]
            }
        ]
    }


@pytest.fixture
def sample_column_info():
    """Fixture para informação de coluna exemplo."""
    return {
        "name": "email",
        "type": "VARCHAR(100)",
        "nullable": False,
        "default": None,
        "constraints": ["UNIQUE", "NOT NULL"]
    }


class TestLLMConfig:
    """Testes para a classe LLMConfig."""
    
    def test_default_config(self):
        """Testa valores default da configuração."""
        config = LLMConfig()
        
        assert config.provider == "openai"
        assert config.model == "gpt-4"
        assert config.temperature == 0.3
        assert config.max_tokens == 2000
        assert config.api_key is None
    
    def test_custom_config(self):
        """Testa configuração customizada."""
        config = LLMConfig(
            provider="anthropic",
            model="claude-3",
            temperature=0.5,
            api_key="custom_key"
        )
        
        assert config.provider == "anthropic"
        assert config.model == "claude-3"
        assert config.temperature == 0.5
        assert config.api_key == "custom_key"


class TestLLMDocumentationGenerator:
    """Testes para a classe LLMDocumentationGenerator."""
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    def test_initialization_openai(self, mock_openai, mock_llm_config):
        """Testa inicialização com provider OpenAI."""
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        assert generator.config == mock_llm_config
        mock_openai.assert_called_once()
    
    @patch('src.llm_documentation_generator.ChatAnthropic')
    def test_initialization_anthropic(self, mock_anthropic):
        """Testa inicialização com provider Anthropic."""
        config = LLMConfig(
            provider="anthropic",
            model="claude-3",
            api_key="test_key"
        )
        
        generator = LLMDocumentationGenerator(config)
        
        assert generator.config == config
        mock_anthropic.assert_called_once()
    
    def test_invalid_provider(self):
        """Testa erro com provider inválido."""
        config = LLMConfig(provider="invalid_provider")
        
        with pytest.raises(ValueError) as exc_info:
            LLMDocumentationGenerator(config)
        
        assert "Provider não suportado" in str(exc_info.value)
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    @patch('src.llm_documentation_generator.LLMChain')
    def test_generate_table_documentation(
        self,
        mock_chain,
        mock_openai,
        mock_llm_config,
        sample_table_schema
    ):
        """Testa geração de documentação de tabela."""
        # Mock do resultado do LLM
        mock_result = """
{
    "table_name": "users",
    "purpose": "Armazena informações de usuários do sistema",
    "business_context": "Tabela central para autenticação e perfil de usuários",
    "relationships": ["Relaciona-se com orders através de user_id"],
    "usage_examples": ["SELECT * FROM users WHERE email = 'user@example.com'"]
}
"""
        mock_chain.return_value.run.return_value = mock_result
        
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        result = generator.generate_table_documentation(sample_table_schema)
        
        assert isinstance(result, TableDocumentation)
        assert result.table_name == "users"
        assert "usuários" in result.purpose.lower()
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    @patch('src.llm_documentation_generator.LLMChain')
    def test_generate_column_documentation(
        self,
        mock_chain,
        mock_openai,
        mock_llm_config,
        sample_column_info
    ):
        """Testa geração de documentação de coluna."""
        mock_result = """
{
    "column_name": "email",
    "business_name": "Endereço de E-mail",
    "description": "Endereço de email único do usuário para autenticação",
    "business_rules": ["Deve ser único no sistema", "Formato válido de email"],
    "data_quality_notes": "Validação de formato obrigatória"
}
"""
        mock_chain.return_value.run.return_value = mock_result
        
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        result = generator.generate_column_documentation(sample_column_info)
        
        assert isinstance(result, ColumnDocumentation)
        assert result.column_name == "email"
        assert "email" in result.business_name.lower()
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    @patch('src.llm_documentation_generator.LLMChain')
    def test_generate_database_overview(
        self,
        mock_chain,
        mock_openai,
        mock_llm_config
    ):
        """Testa geração de visão geral do banco."""
        mock_result = "Este banco de dados gerencia informações de usuários e pedidos."
        mock_chain.return_value.run.return_value = mock_result
        
        database_schema = {
            "name": "ecommerce_db",
            "tables": [
                {"name": "users", "foreign_keys": []},
                {"name": "orders", "foreign_keys": [{"column": "user_id"}]}
            ]
        }
        
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        result = generator.generate_database_overview(database_schema)
        
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_format_columns(self, mock_llm_config, sample_table_schema):
        """Testa formatação de colunas para prompt."""
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        result = generator._format_columns(sample_table_schema["columns"])
        
        assert "id" in result
        assert "username" in result
        assert "INTEGER" in result
        assert "NOT NULL" in result
    
    def test_format_foreign_keys(self, mock_llm_config):
        """Testa formatação de chaves estrangeiras."""
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        foreign_keys = [
            {
                "column": "user_id",
                "referenced_table": "users",
                "referenced_column": "id"
            }
        ]
        
        result = generator._format_foreign_keys(foreign_keys)
        
        assert "user_id" in result
        assert "users.id" in result
    
    def test_format_indexes(self, mock_llm_config):
        """Testa formatação de índices."""
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        indexes = [
            {
                "name": "idx_email",
                "columns": ["email"]
            }
        ]
        
        result = generator._format_indexes(indexes)
        
        assert "idx_email" in result
        assert "email" in result
    
    def test_count_relationships(self, mock_llm_config):
        """Testa contagem de relacionamentos."""
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        database_schema = {
            "tables": [
                {"foreign_keys": [{"column": "fk1"}]},
                {"foreign_keys": [{"column": "fk2"}, {"column": "fk3"}]},
                {"foreign_keys": []}
            ]
        }
        
        result = generator._count_relationships(database_schema)
        
        assert result == 3


class TestFactoryFunction:
    """Testes para a função factory."""
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    def test_create_documentation_generator_defaults(self, mock_openai):
        """Testa criação com valores default."""
        generator = create_documentation_generator()
        
        assert isinstance(generator, LLMDocumentationGenerator)
        assert generator.config.provider == "openai"
        assert generator.config.model == "gpt-4"
    
    @patch('src.llm_documentation_generator.ChatAnthropic')
    def test_create_documentation_generator_custom(self, mock_anthropic):
        """Testa criação com parâmetros customizados."""
        generator = create_documentation_generator(
            provider="anthropic",
            model="claude-3",
            api_key="custom_key"
        )
        
        assert isinstance(generator, LLMDocumentationGenerator)
        assert generator.config.provider == "anthropic"
        assert generator.config.model == "claude-3"
        assert generator.config.api_key == "custom_key"


class TestErrorHandling:
    """Testes para tratamento de erros."""
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    @patch('src.llm_documentation_generator.LLMChain')
    def test_table_documentation_error(
        self,
        mock_chain,
        mock_openai,
        mock_llm_config,
        sample_table_schema
    ):
        """Testa tratamento de erro na geração de documentação de tabela."""
        mock_chain.return_value.run.side_effect = Exception("API Error")
        
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        with pytest.raises(Exception) as exc_info:
            generator.generate_table_documentation(sample_table_schema)
        
        assert "API Error" in str(exc_info.value)
    
    @patch('src.llm_documentation_generator.ChatOpenAI')
    @patch('src.llm_documentation_generator.LLMChain')
    def test_column_documentation_error(
        self,
        mock_chain,
        mock_openai,
        mock_llm_config,
        sample_column_info
    ):
        """Testa tratamento de erro na geração de documentação de coluna."""
        mock_chain.return_value.run.side_effect = Exception("API Error")
        
        generator = LLMDocumentationGenerator(mock_llm_config)
        
        with pytest.raises(Exception) as exc_info:
            generator.generate_column_documentation(sample_column_info)
        
        assert "API Error" in str(exc_info.value)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])