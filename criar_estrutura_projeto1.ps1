<#
.SYNOPSIS
    Cria estrutura completa do Projeto 1 - Database Documentation Assistant
    
.DESCRIPTION
    Script para criar toda a estrutura de pastas e arquivos base do primeiro
    projeto do portfolio de transicao de carreira.
    
.AUTHOR
    Paulo Cesar Mendes de Sousa Junior
    
.DATE
    November 2025
#>

# Configuracoes
$ErrorActionPreference = "Stop"
$RootPath = "C:\projetos\paulo_sousa\paulo-career-accelerator"
$ProjectPath = Join-Path $RootPath "projects\01-database-documentation-assistant"

# Funcoes para output colorido (usando caracteres ASCII seguros)
function Write-Success { 
    param($Message) 
    Write-Host "[OK] $Message" -ForegroundColor Green 
}

function Write-Info { 
    param($Message) 
    Write-Host "[>>] $Message" -ForegroundColor Cyan 
}

function Write-Warning { 
    param($Message) 
    Write-Host "[!] $Message" -ForegroundColor Yellow 
}

function Write-ErrorMsg { 
    param($Message) 
    Write-Host "[X] $Message" -ForegroundColor Red 
}

# Banner
Write-Host ""
Write-Host "===============================================================" -ForegroundColor Blue
Write-Host "  DATABASE DOCUMENTATION ASSISTANT - ESTRUTURA DO PROJETO" -ForegroundColor Blue
Write-Host "===============================================================" -ForegroundColor Blue
Write-Host ""

# Verificar se esta na raiz correta
Write-Info "Verificando diretorio raiz..."
if (-not (Test-Path $RootPath)) {
    Write-ErrorMsg "Diretorio raiz nao encontrado: $RootPath"
    exit 1
}
Set-Location $RootPath
Write-Success "Diretorio raiz confirmado: $RootPath"

# Estrutura de pastas a criar
Write-Info "Definindo estrutura de pastas..."
$Folders = @(
    "projects",
    "projects\01-database-documentation-assistant",
    "projects\01-database-documentation-assistant\src",
    "projects\01-database-documentation-assistant\tests",
    "projects\01-database-documentation-assistant\examples",
    "projects\01-database-documentation-assistant\data",
    "projects\01-database-documentation-assistant\output",
    "projects\01-database-documentation-assistant\docs"
)

# Criar pastas
Write-Info "Criando estrutura de pastas..."
foreach ($Folder in $Folders) {
    $FullPath = Join-Path $RootPath $Folder
    if (Test-Path $FullPath) {
        Write-Warning "Pasta ja existe: $Folder"
    } else {
        New-Item -Path $FullPath -ItemType Directory -Force | Out-Null
        Write-Success "Criado: $Folder"
    }
}

# Funcao para criar arquivo se nao existir
function New-FileIfNotExists {
    param(
        [string]$Path,
        [string]$Content = "",
        [string]$Description
    )
    
    if (Test-Path $Path) {
        Write-Warning "Arquivo ja existe: $Description"
    } else {
        # Garante criação do diretório pai se não existir
        $ParentDir = Split-Path -Parent $Path
        if (-not (Test-Path $ParentDir)) {
            New-Item -Path $ParentDir -ItemType Directory -Force | Out-Null
        }
        [System.IO.File]::WriteAllText($Path, $Content, [System.Text.UTF8Encoding]::new($false))
        Write-Success "Criado: $Description"
    }
}

# Criar arquivos __init__.py
Write-Info "Criando arquivos __init__.py..."
$InitContent = @'
"""
Database Documentation Assistant Package
Author: Paulo Cesar Mendes de Sousa Junior
"""

__version__ = '0.1.0'
'@

New-FileIfNotExists -Path "$ProjectPath\src\__init__.py" -Content $InitContent -Description "src/__init__.py"
New-FileIfNotExists -Path "$ProjectPath\tests\__init__.py" -Content $InitContent -Description "tests/__init__.py"

# Criar .gitkeep para pastas vazias
Write-Info "Criando .gitkeep para pastas de dados..."
New-FileIfNotExists -Path "$ProjectPath\data\.gitkeep" -Content "" -Description "data/.gitkeep"
New-FileIfNotExists -Path "$ProjectPath\output\.gitkeep" -Content "" -Description "output/.gitkeep"

# Criar requirements.txt
Write-Info "Criando requirements.txt do projeto..."
$RequirementsContent = @'
# Database Documentation Assistant - Requirements
# Python 3.11+

# Database Connectivity
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pymysql==1.1.0

# LLM Integration
langchain==0.1.0
langchain-openai==0.0.2
openai==1.6.1

# Data Processing
pandas==2.1.4
pydantic==2.5.3
python-dotenv==1.0.0
pyyaml==6.0.1

# CLI & UI
streamlit==1.29.0
click==8.1.7
rich==13.7.0

# Testing
pytest==7.4.3
pytest-cov==4.1.0
pytest-mock==3.12.0

# Code Quality
black==23.12.1
flake8==7.0.0
mypy==1.8.0
'@
New-FileIfNotExists -Path "$ProjectPath\requirements.txt" -Content $RequirementsContent -Description "requirements.txt"

# Criar .env.example
Write-Info "Criando .env.example..."
$EnvContent = @'
# Database Configuration
DATABASE_TYPE=postgresql
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=your_database
DATABASE_USER=your_username
DATABASE_PASSWORD=your_password

# LLM Configuration
OPENAI_API_KEY=your_openai_api_key_here
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2000

# Application Settings
LOG_LEVEL=INFO
OUTPUT_FORMAT=markdown
OUTPUT_DIR=./output
'@
New-FileIfNotExists -Path "$ProjectPath\.env.example" -Content $EnvContent -Description ".env.example"

# Criar config.yaml.example
Write-Info "Criando config.yaml.example..."
$ConfigContent = @'
# Database Documentation Assistant Configuration

database:
  type: postgresql
  host: localhost
  port: 5432
  name: your_database
  
llm:
  provider: openai
  model: gpt-4-turbo-preview
  temperature: 0.3
  max_tokens: 2000
  
documentation:
  include_indexes: true
  include_constraints: true
  include_foreign_keys: true
  include_sample_data: false
  detect_pii: true
  
output:
  format: markdown
  directory: ./output
  include_diagram: true
  
logging:
  level: INFO
  file: ./logs/app.log
'@
New-FileIfNotExists -Path "$ProjectPath\config.yaml.example" -Content $ConfigContent -Description "config.yaml.example"

# Criar README.md basico (usando @' para evitar problemas com backticks)
Write-Info "Criando README.md basico..."
$ReadmeContent = @'
# Database Documentation Assistant

> AI-powered automatic database documentation generator

## Overview

Automated tool that connects to PostgreSQL/MySQL databases, extracts schema information, and generates comprehensive documentation using LLMs (Large Language Models).

## Features

- Multi-database support (PostgreSQL, MySQL)
- Automatic schema extraction
- AI-powered documentation generation
- PII detection
- Export to Markdown
- Interactive Streamlit UI

## Tech Stack

- **Python 3.11+**
- **SQLAlchemy** - Database connectivity
- **LangChain** - LLM orchestration
- **OpenAI GPT-4** - Documentation generation
- **Streamlit** - Web interface

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials

# Run Streamlit app
streamlit run app.py
```
'@
New-FileIfNotExists -Path "$ProjectPath\README.md" -Content $ReadmeContent -Description "README.md"

Write-Host ""
Write-Success "Estrutura do projeto criada com sucesso!"
Write-Host ""
Write-Info "Proximo passo: Configure o arquivo .env com suas credenciais"
Write-Host ""