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