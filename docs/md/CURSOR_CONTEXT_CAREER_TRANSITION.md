# 🤖 CONTEXTO COMPLETO PARA CURSOR AI - TRANSIÇÃO DE CARREIRA DATA + IA

## 📋 VISÃO GERAL

**Profissional:** Paulo (baseado em Brasília-DF, Brasil)
**Situação:** Transição de carreira ativa - disponível para oportunidades imediatas
**Objetivo:** Reposicionar de "Data Engineer Tradicional" para "Data Architect + AI Engineer"
**Timeline:** Urgente - necessidade de oportunidade em 30-60 dias

---

## 🎯 PERFIL PROFISSIONAL

### Experiência Core
- **25+ anos** em projetos de dados, Data Warehouse e Business Intelligence
- **Especialista** em governança de dados, modelagem dimensional e análise de dados
- **Experiência profunda** com órgãos públicos brasileiros:
  - PRF (Polícia Rodoviária Federal)
  - TCU (Tribunal de Contas da União)
  - TST (Tribunal Superior do Trabalho)
  - Sebrae-BA
  - Diversos tribunais federais
- **Expertise** em compliance (LGPD), frameworks (DMBOK), e gestão de projetos complexos
- **Background** em liderança técnica e arquitetura de soluções

### Stack Técnico ATUAL (Dominado)

**Databases & SQL:**
- SQL avançado (MySQL, PostgreSQL, SQL Server)
- Trino (distributed SQL)
- Modelagem dimensional (Kimball, Inmon)
- Performance tuning e otimização

**Data Engineering:**
- dbt (data build tool) - transformações, testes, documentação
- Python (intermediário/avançado para dados)
- ETL/ELT pipelines
- Data quality frameworks

**BI & Visualization:**
- Power BI (avançado)
- SAP BusinessObjects (legado)
- Dashboard design e storytelling

**Data Governance:**
- DMBOK framework
- Data cataloging
- Data lineage
- LGPD compliance
- Metadata management

**Tools & Infrastructure:**
- Git/GitHub (version control)
- Linux/bash scripting
- VS Code
- SAP PowerDesigner (modelagem)
- Excel (análise avançada, VBA)

**Soft Skills:**
- Documentação técnica (excelente)
- Comunicação com stakeholders não-técnicos
- Gestão de projetos
- Trabalho com ambientes regulados

### Stack em DESENVOLVIMENTO (Aprendizado Ativo)

**IA Generativa:**
- ✅ Prompt Engineering (em desenvolvimento)
- 🔄 LangChain (framework para LLM apps)
- 🔄 OpenAI API (GPT-4, embeddings)
- 🔄 Anthropic Claude API
- 🔄 RAG (Retrieval Augmented Generation)
- 🔄 LLM Agents e tools
- 📝 Function calling
- 📝 Fine-tuning (planejado)

**Vector Databases & Embeddings:**
- 🔄 Pinecone
- 🔄 Chroma (local vector store)
- 🔄 Weaviate
- 🔄 Embedding strategies e chunking

**MLOps:**
- 🔄 MLflow (model versioning e tracking)
- 📝 Feature stores
- 📝 Model monitoring
- 📝 A/B testing for models

**Data Observability:**
- 🔄 Great Expectations (data quality)
- 📝 Monte Carlo
- 📝 dbt testing avançado

**Cloud Platforms:**
- 🔄 Google Cloud Platform (BigQuery, Vertex AI, Cloud Run)
- 📝 AWS (planejado)
- 📝 Azure (planejado)

**Orchestration:**
- 📝 Airflow (planejado)
- 📝 Dagster (planejado)
- 📝 Prefect (planejado)

**Advanced Data Concepts:**
- 📝 Data Mesh architecture
- 📝 Lakehouse (Delta Lake, Iceberg)
- 📝 Real-time streaming (Kafka)

**Legenda:** 
- ✅ = Conhecimento inicial adquirido
- 🔄 = Em desenvolvimento ativo
- 📝 = Planejado para próximas semanas

---

## 🚀 PROJETOS PORTFOLIO EM DESENVOLVIMENTO

### Projeto 1: Database Documentation Assistant
**Status:** Em desenvolvimento
**Prazo:** 8 horas (sprint de 1 dia)

**Objetivo:** 
Ferramenta que conecta em databases e gera documentação automática usando LLMs, resolvendo o problema universal de documentação desatualizada.

**Stack:**
- Python 3.10+
- LangChain
- OpenAI API (GPT-4 para análise, GPT-3.5-turbo para docs)
- SQLAlchemy (conexão universal com DBs)
- Streamlit (interface web simples)

**Funcionalidades:**
1. **Conexão Database:**
   - Suporte MySQL, PostgreSQL
   - Connection string ou parâmetros separados
   - Test connection antes de processar

2. **Schema Extraction:**
   - Listar todas as tabelas e views
   - Extrair colunas (nome, tipo, nullable, default)
   - Identificar primary keys, foreign keys
   - Detectar índices

3. **LLM-Powered Documentation:**
   - Gerar descrição de negócio para cada tabela
   - Sugerir descrição para cada coluna
   - Identificar relacionamentos implícitos (naming patterns)
   - Sugerir data quality checks apropriados
   - Identificar possíveis PII (dados sensíveis)

4. **Output:**
   - Markdown formatado (compatível com dbt docs)
   - Opção de export para CSV
   - Visualização interativa no Streamlit

**Estrutura de Diretórios:**
```
database-doc-assistant/
├── README.md                      # Documentação completa do projeto
├── requirements.txt               # Dependencies Python
├── .env.example                   # Template de variáveis de ambiente
├── .gitignore                     # Ignorar .env, __pycache__, etc
│
├── src/
│   ├── __init__.py
│   ├── database_connector.py      # Classe para conexão com DBs
│   ├── schema_extractor.py        # Extrai schema completo
│   ├── llm_documenter.py          # Usa LLM para gerar docs
│   ├── markdown_generator.py      # Formata output em Markdown
│   └── config.py                  # Configurações e constantes
│
├── app.py                         # Streamlit app principal
│
├── examples/
│   ├── sample_output.md           # Exemplo de documentação gerada
│   └── screenshots/               # Screenshots do app
│
├── tests/
│   ├── __init__.py
│   ├── test_database_connector.py
│   └── test_schema_extractor.py
│
└── docs/
    └── ARCHITECTURE.md            # Explicação da arquitetura
```

**Key Code Patterns:**

```python
# database_connector.py
from sqlalchemy import create_engine, inspect
from typing import Dict, List, Optional

class DatabaseConnector:
    """Handle database connections and basic operations."""
    
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.inspector = inspect(self.engine)
    
    def test_connection(self) -> bool:
        """Test if database connection is valid."""
        try:
            with self.engine.connect() as conn:
                conn.execute("SELECT 1")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def get_table_names(self) -> List[str]:
        """Get all table names in the database."""
        return self.inspector.get_table_names()
```

```python
# llm_documenter.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class LLMDocumenter:
    """Use LLM to generate documentation for database objects."""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.llm = ChatOpenAI(api_key=api_key, model=model, temperature=0.3)
    
    def document_table(self, table_name: str, columns: List[Dict]) -> str:
        """Generate business description for a table."""
        
        prompt = ChatPromptTemplate.from_template(
            """You are a data documentation expert. Given the following table structure,
            provide a clear, concise business description of what this table likely stores.
            
            Table name: {table_name}
            Columns: {columns}
            
            Provide:
            1. Business purpose (2-3 sentences)
            2. Key entities represented
            3. Likely relationships with other tables
            
            Be specific but avoid speculation. Focus on what the schema tells us."""
        )
        
        chain = prompt | self.llm
        result = chain.invoke({
            "table_name": table_name,
            "columns": self._format_columns(columns)
        })
        
        return result.content
```

**Demo Flow:**
1. User inputs database credentials
2. App connects and extracts schema
3. Shows progress bar while processing tables
4. Displays interactive documentation
5. Allows download as Markdown

**README Structure:**
```markdown
# 🗄️ Database Documentation Assistant

## 🎯 Problem Solved
Database schemas grow over time without proper documentation, making it difficult for new team members to understand the data structure. Manual documentation is time-consuming and quickly becomes outdated.

## ✨ Solution
Automatic documentation generation using LLMs to analyze database schema and produce human-readable documentation with business context.

## 🚀 Features
- Automatic schema extraction
- AI-generated table and column descriptions  
- Relationship detection
- Data quality suggestions
- PII identification
- Export to Markdown (dbt-compatible)

## 🛠️ Tech Stack
- Python 3.10+
- LangChain
- OpenAI GPT-4
- SQLAlchemy
- Streamlit

## 📦 Installation
[Step-by-step instructions]

## 💻 Usage
[Code examples and screenshots]

## 📊 Example Output
[Link to example]

## 🔮 Future Enhancements
- Support for more databases (Oracle, MongoDB)
- Version tracking (schema changes over time)
- Integration with dbt Cloud
- Automatic CHANGELOG generation

## 👤 Author
Paulo - Senior Data Architect
[LinkedIn] | [GitHub]
```

---

### Projeto 2: Data Lineage Analyzer with AI
**Status:** Planejado
**Prazo:** 10 horas (sprint de 1.5 dias)

**Objetivo:**
Analisar queries SQL e código dbt para gerar mapeamento automático de lineage (origem → transformação → destino), crítico para governança de dados.

**Stack:**
- Python 3.10+
- sqlparse ou sqlglot (SQL parsing)
- LangChain + OpenAI API
- NetworkX (graph algorithms)
- Plotly (interactive visualizations)
- Streamlit

**Funcionalidades:**

1. **SQL Parsing:**
   - Parse de queries SQL complexas (CTEs, subqueries, JOINs)
   - Extrair tabelas source (FROM, JOIN)
   - Identificar colunas usadas
   - Mapear transformações (SELECT, WHERE, GROUP BY)

2. **dbt Integration:**
   - Ler arquivos .sql do dbt
   - Entender refs e sources
   - Mapear dependencies
   - Extrair metadata de schema.yml

3. **AI-Enhanced Analysis:**
   - LLM explica transformações complexas em linguagem natural
   - Identifica filtros críticos (ex: WHERE deleted_at IS NULL)
   - Detecta agregações e sua lógica
   - Sugere impacto de mudanças

4. **Lineage Graph:**
   - Grafo interativo (nodes = tables, edges = transformations)
   - Drill-down em cada transformação
   - Highlight de paths (source to target)
   - Export para formato OpenLineage (padrão da indústria)

5. **Impact Analysis:**
   - "Se eu mudar coluna X, o que quebra?"
   - "Quais dashboards dependem desta tabela?"
   - Análise upstream e downstream

**Estrutura de Diretórios:**
```
data-lineage-analyzer/
├── README.md
├── requirements.txt
├── .env.example
│
├── src/
│   ├── __init__.py
│   ├── sql_parser.py           # Parse SQL to extract components
│   ├── dbt_parser.py            # Parse dbt projects
│   ├── dependency_extractor.py  # Extract table dependencies
│   ├── llm_analyzer.py          # AI analysis of transformations
│   ├── graph_builder.py         # Build lineage graph with NetworkX
│   ├── visualizer.py            # Plotly visualizations
│   └── impact_analyzer.py       # Impact analysis logic
│
├── app.py                       # Streamlit application
│
├── examples/
│   ├── sample_queries.sql       # Example SQL queries
│   ├── sample_dbt_project/      # Small dbt project for demo
│   └── generated_lineage.png    # Example output
│
├── tests/
│   └── test_sql_parser.py
│
└── docs/
    ├── ARCHITECTURE.md
    └── OPENLINEAGE_SPEC.md
```

**Key Technical Challenges:**

1. **Complex SQL Parsing:**
   ```python
   # Use sqlglot for robust parsing
   import sqlglot
   
   parsed = sqlglot.parse_one(query, dialect="mysql")
   tables = [table.name for table in parsed.find_all(sqlglot.exp.Table)]
   ```

2. **LLM for Transformation Explanation:**
   ```python
   def explain_transformation(self, sql_snippet: str) -> str:
       prompt = f"""Explain this SQL transformation in business terms:
       
       {sql_snippet}
       
       Focus on:
       - What data is being selected
       - Any filters applied
       - Aggregations or calculations
       - Business logic implied
       
       Be concise (2-3 sentences)."""
       
       return self.llm.predict(prompt)
   ```

3. **Graph Visualization:**
   ```python
   import networkx as nx
   import plotly.graph_objects as go
   
   def build_lineage_graph(dependencies: List[Tuple[str, str]]):
       G = nx.DiGraph()
       G.add_edges_from(dependencies)
       
       pos = nx.spring_layout(G)
       
       # Create Plotly figure
       edge_trace = go.Scatter(...)
       node_trace = go.Scatter(...)
       
       fig = go.Figure(data=[edge_trace, node_trace], layout=...)
       return fig
   ```

**Demo Scenarios:**
1. Upload SQL file → See lineage
2. Connect to dbt project → Full project lineage
3. Click on table → See impact analysis
4. Export to OpenLineage JSON

---

### Projeto 3: RAG sobre Dicionário de Dados
**Status:** Planejado
**Prazo:** 12 horas (sprint de 2 dias)

**Objetivo:**
Sistema de chat conversacional que permite consultar a estrutura de dados da empresa em linguagem natural, eliminando necessidade de conhecer schemas SQL.

**Stack:**
- LangChain (framework core)
- OpenAI Embeddings + GPT-4
- Vector Database (Chroma para local, Pinecone para produção)
- Streamlit (chat interface)
- dbt (para gerar dicionário source)

**Funcionalidades:**

1. **Document Ingestion:**
   - SQL schema files (.sql, CREATE TABLE statements)
   - dbt documentation (manifest.json, catalog.json)
   - README files (markdown)
   - Data dictionaries (CSV, Excel)
   - Custom data catalogs

2. **Embedding & Indexing:**
   - Chunk documents intelligentemente
   - Gerar embeddings (OpenAI text-embedding-ada-002)
   - Armazenar em vector database
   - Metadata tagging (source, domain, timestamp)

3. **RAG Pipeline:**
   - User pergunta em linguagem natural
   - Semantic search no vector DB
   - Retrieve top-k chunks relevantes
   - LLM gera resposta com contexto
   - Cita fontes (links para docs)

4. **Advanced Features:**
   - Filtros por domínio (vendas, RH, finanças)
   - Histórico de conversas (memory)
   - Sugestões de perguntas comuns
   - Feedback loop (useful/not useful)

5. **Sample Questions:**
   - "Onde está armazenado o CPF do cliente?"
   - "Quais tabelas contêm informação de vendas?"
   - "Como é calculada a receita líquida?"
   - "Qual a diferença entre pedido e order?"
   - "Essa coluna contém dados sensíveis?"

**Estrutura de Diretórios:**
```
data-dictionary-rag/
├── README.md
├── requirements.txt
├── .env.example
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py      # Load and parse various doc types
│   ├── chunking.py              # Smart document chunking
│   ├── embedding_generator.py   # Generate embeddings
│   ├── vector_store.py          # Vector DB operations
│   ├── rag_chain.py             # RAG pipeline with LangChain
│   ├── chat_interface.py        # Streamlit chat UI
│   └── feedback_logger.py       # Log user feedback
│
├── app.py                       # Main Streamlit app
│
├── data/
│   ├── schemas/                 # SQL schemas to ingest
│   ├── dbt_docs/                # dbt documentation exports
│   ├── readme_files/            # Project READMEs
│   └── dictionaries/            # CSV/Excel data dictionaries
│
├── vector_db/                   # Local Chroma database
│
├── examples/
│   ├── sample_questions.md      # Common questions users can ask
│   └── screenshots/
│
├── tests/
│   ├── test_document_loader.py
│   └── test_rag_chain.py
│
└── docs/
    ├── ARCHITECTURE.md
    ├── RAG_DESIGN.md
    └── EVALUATION.md            # How to evaluate RAG quality
```

**Key Technical Components:**

1. **Smart Chunking:**
   ```python
   from langchain.text_splitter import RecursiveCharacterTextSplitter
   
   def chunk_database_docs(doc: str, metadata: dict) -> List[Document]:
       """
       Chunk database documentation with SQL-aware splitting.
       Preserves table definitions and column lists together.
       """
       splitter = RecursiveCharacterTextSplitter(
           chunk_size=1000,
           chunk_overlap=200,
           separators=["\n\n", "\n", "CREATE TABLE", "ALTER TABLE", " ", ""]
       )
       
       chunks = splitter.split_text(doc)
       
       return [
           Document(page_content=chunk, metadata=metadata) 
           for chunk in chunks
       ]
   ```

2. **RAG Chain:**
   ```python
   from langchain.chains import RetrievalQA
   from langchain.chat_models import ChatOpenAI
   from langchain.embeddings import OpenAIEmbeddings
   from langchain.vectorstores import Chroma
   
   class DataDictionaryRAG:
       def __init__(self, vector_store_path: str, openai_api_key: str):
           self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
           self.vectorstore = Chroma(
               persist_directory=vector_store_path,
               embedding_function=self.embeddings
           )
           self.llm = ChatOpenAI(
               model="gpt-4",
               temperature=0,
               openai_api_key=openai_api_key
           )
           
           self.qa_chain = RetrievalQA.from_chain_type(
               llm=self.llm,
               chain_type="stuff",
               retriever=self.vectorstore.as_retriever(
                   search_kwargs={"k": 5}
               ),
               return_source_documents=True
           )
       
       def ask(self, question: str) -> dict:
           """Ask a question and get answer with sources."""
           result = self.qa_chain({"query": question})
           
           return {
               "answer": result["result"],
               "sources": [
                   {
                       "content": doc.page_content,
                       "metadata": doc.metadata
                   }
                   for doc in result["source_documents"]
               ]
           }
   ```

3. **Streamlit Chat Interface:**
   ```python
   import streamlit as st
   
   st.title("💬 Data Dictionary Chat")
   
   # Initialize chat history
   if "messages" not in st.session_state:
       st.session_state.messages = []
   
   # Display chat history
   for message in st.session_state.messages:
       with st.chat_message(message["role"]):
           st.markdown(message["content"])
   
   # User input
   if prompt := st.chat_input("Ask about your data..."):
       # Add user message
       st.session_state.messages.append({"role": "user", "content": prompt})
       
       with st.chat_message("user"):
           st.markdown(prompt)
       
       # Get RAG response
       with st.chat_message("assistant"):
           with st.spinner("Searching data dictionary..."):
               result = rag.ask(prompt)
               
               st.markdown(result["answer"])
               
               # Show sources
               with st.expander("📚 Sources"):
                   for i, source in enumerate(result["sources"], 1):
                       st.markdown(f"**Source {i}:** {source['metadata']['source']}")
                       st.code(source['content'][:200] + "...")
       
       # Add assistant message
       st.session_state.messages.append({
           "role": "assistant",
           "content": result["answer"]
       })
   ```

4. **Evaluation Framework:**
   ```python
   # Test questions with expected answers
   test_cases = [
       {
           "question": "Where is customer CPF stored?",
           "expected_tables": ["customers", "users"],
           "expected_columns": ["cpf", "taxpayer_id"]
       },
       # More test cases...
   ]
   
   def evaluate_rag(rag_system, test_cases):
       results = []
       for test in test_cases:
           answer = rag_system.ask(test["question"])
           
           # Check if expected tables/columns mentioned
           score = calculate_relevance(answer, test)
           results.append(score)
       
       return sum(results) / len(results)
   ```

**Demo Flow:**
1. Ingest sample database documentation
2. User types question in chat
3. System searches semantically
4. Shows answer with sources
5. User can filter by domain
6. Suggests related questions

**Diferencial deste Projeto:**
- Resolve problema real em TODAS empresas
- Demonstra RAG completo (não toy example)
- Mostra governança (tracking de perguntas)
- Portfolio piece impressionante

---

## 📚 CONHECIMENTOS - GAP ANALYSIS

### ✅ DOMINADO (Pode usar com confiança)

**Data Engineering:**
- SQL otimização e tuning
- Modelagem dimensional (star schema, snowflake)
- ETL design patterns
- Data warehousing architecture
- dbt (modelos, tests, docs, macros)
- Data quality frameworks
- Metadata management

**Programming:**
- Python para data engineering
- Bash scripting
- Git/GitHub workflows
- Data structures e algorithms (intermediário)

**BI & Analytics:**
- Power BI (DAX, M, design)
- Dashboard design principles
- KPI definition
- Storytelling with data

**Governance & Compliance:**
- DMBOK framework
- Data lineage concepts
- Data cataloging
- LGPD requirements
- Audit trails

**Soft Skills:**
- Technical documentation
- Stakeholder management
- Project scoping
- Requirements gathering
- Team leadership

### 🔄 EM DESENVOLVIMENTO (Aprendendo ativamente)

**IA Generativa:**
- Prompt engineering patterns
- LangChain framework
- RAG architecture
- Vector databases e embeddings
- LLM agents design
- Function calling

**MLOps Basics:**
- Model versioning (MLflow)
- Experiment tracking
- Basic deployment concepts

**Modern Data Stack:**
- dbt advanced (packages, macros customizados)
- Great Expectations
- Data observability concepts

**Cloud (GCP focus):**
- BigQuery advanced
- Vertex AI basics
- Cloud Run deployment

### 📝 GAPS CRÍTICOS (Prioridade próximas semanas)

**MLOps Production:**
- Feature stores
- Model monitoring em produção
- A/B testing frameworks
- Automated retraining pipelines

**Advanced AI:**
- Fine-tuning de LLMs
- Multi-agent systems
- Advanced prompt techniques (few-shot, CoT)
- LLM evaluation metrics

**Real-time Data:**
- Kafka/streaming concepts
- Real-time feature computation
- Stream processing

**Data Mesh:**
- Domain-driven data ownership
- Data product thinking
- Federated governance

**Infrastructure:**
- Kubernetes basics
- Docker (além do básico)
- CI/CD pipelines
- Infrastructure as code (Terraform)

---

## 📖 PLANO DE ESTUDOS (3 SEMANAS - FAST TRACK)

### SEMANA 1: IA Generativa & RAG

**Segunda a Quarta (12h total)**
- DeepLearning.AI: "ChatGPT Prompt Engineering" (2h)
- Prompt Engineering Guide (leitura) (2h)
- Prática: 50 prompts para casos de dados (2h)
- OpenAI API tutorial oficial (2h)
- Anthropic Claude API tutorial (1h)
- Projeto mini: SQL generator via LLM (3h)

**Quinta a Domingo (20h total)**
- DeepLearning.AI: "LangChain for LLM Apps" (3h)
- RAG architecture deep dive (LangChain docs) (3h)
- Vector databases tutorial (Pinecone) (2h)
- Embeddings e similarity search (teoria + prática) (3h)
- **Projeto Portfolio #1: Database Doc Assistant** (8h)
- Documentar e publicar projeto (1h)

**Material:**
- https://www.deeplearning.ai/short-courses/
- https://www.promptingguide.ai/
- https://python.langchain.com/docs/
- https://www.pinecone.io/learn/

### SEMANA 2: MLOps & Advanced dbt

**Segunda a Quarta (12h total)**
- dbt Learn Advanced (dbt Labs) (4h)
- dbt macros e Jinja deep dive (2h)
- dbt packages ecosystem (dbt_utils, codegen) (2h)
- Great Expectations tutorial completo (4h)

**Quinta a Domingo (20h total)**
- MLOps foundations (Made With ML course) (5h)
- MLflow tutorial hands-on (3h)
- **Projeto Portfolio #2: Data Lineage Analyzer** (10h)
- Documentar e publicar projeto (2h)

**Material:**
- https://learn.getdbt.com/
- https://madewithml.com/
- https://mlflow.org/docs/latest/tutorials-and-examples/index.html
- https://docs.greatexpectations.io/

### SEMANA 3: Cloud & Projeto Final

**Segunda a Quarta (12h total)**
- Google Cloud Skills Boost: BigQuery paths (4h)
- Vertex AI Workbench tutorial (2h)
- Cloud Run deployment tutorial (2h)
- GCP data engineering best practices (2h)
- Microsoft AI-900 (estudo + prova) (2h)

**Quinta a Domingo (20h total)**
- **Projeto Portfolio #3: RAG Data Dictionary** (15h)
- Criar vídeos demo dos 3 projetos (3h)
- Escrever 1 artigo técnico (Medium/LinkedIn) (2h)

**Material:**
- https://www.cloudskillsboost.google/
- https://cloud.google.com/vertex-ai/docs
- https://learn.microsoft.com/en-us/certifications/azure-ai-fundamentals/

### Recursos Adicionais

**YouTube Channels (consumir paralelo):**
- Data with Zach (dbt best practices)
- James Briggs (LangChain tutorials)
- Abhishek Thakur (ML/MLOps)
- Seattle Data Guy (data engineering)

**Comunidades (participar ativamente):**
- dbt Slack: https://www.getdbt.com/community/join-the-community/
- LangChain Discord
- Data Engineering Brasil (Telegram)
- AI Brasil (Discord)

**Newsletters:**
- The Sequence (AI news)
- Data Engineering Weekly
- Pointer.io (engineering)

---

## 🎨 BRANDING & POSICIONAMENTO

### Elevator Pitch (30 segundos)
"Arquiteto de dados com 25 anos transformando dados em valor para organizações complexas como TCU e Sebrae. Especializado em modernizar sistemas legados usando IA - desde governança automatizada até analytics conversacional. Combino experiência profunda com órgãos públicos brasileiros e expertise técnica em dbt, Python, e IA Generativa para entregar soluções que funcionam em ambientes regulados."

### Proposta de Valor Única
1. **Experiência Rara:** Poucos profissionais têm experiência profunda com dados governamentais + IA
2. **Implementador:** Entrega projetos funcionando, não apenas conceitos
3. **Bridge Builder:** Conecta sistemas legados com arquitetura moderna
4. **Compliance Expert:** Entende LGPD, auditorias, e governança rigorosa
5. **Documentador:** Cria documentação que equipes realmente usam

### Nichos de Mercado Estratégicos

**Primário (Higher value + fit perfeito):**
1. **IA Aplicada a Governança de Dados**
   - Classificação automática de dados sensíveis
   - Lineage automatizado
   - Data quality com ML
   - Compliance monitoring

2. **Modernização de Sistemas Legados**
   - Migração de BI legado (SAP BO, Cognos) para moderno
   - Reverse engineering com IA
   - Documentação automática
   - Bridge entre gerações de tecnologia

3. **BI Aumentado (Augmented Analytics)**
   - Q&A em linguagem natural
   - Insights automáticos
   - Narrativas geradas por IA
   - Chat com dados (RAG sobre DW)

**Secundário (Good fit):**
4. **MLOps para Dados Governamentais**
   - Pipelines de ML para órgãos públicos
   - Smart cities data architecture
   - Otimização de recursos públicos

5. **Data Mesh + IA**
   - Arquitetura Data Mesh
   - Domain-driven data
   - Governança distribuída

### Títulos LinkedIn (A/B Test)

**Opção A (Técnico + Sênior):**
"Senior Data Architect | 25+ years DW/BI | AI-Enhanced Data Governance & Legacy System Modernization"

**Opção B (Transformação + Valor):**
"Transforming 25 Years of Data Expertise into AI-Powered Solutions | Data Architecture + Governance + GenAI"

**Opção C (Nicho específico):**
"Data Architect specializing in AI-Enhanced Governance | Modernizing Legacy Systems | 25yr+ in Public Sector Data"

### Posições-Alvo (Job Search)

**Tier 1 (Ideal match):**
- Senior Data Architect
- Lead Data Engineer
- Principal Data Engineer  
- Head of Data Governance
- Chief Data Officer (mid-size companies)

**Tier 2 (Good match):**
- Senior Analytics Engineer
- Data Platform Engineer
- MLOps Engineer (with upskilling)
- Data Consultant / Advisor
- Solutions Architect (Data & AI)

**Tier 3 (Stretch but possible):**
- AI Engineer (focus on data applications)
- Machine Learning Engineer (data-centric)
- Staff Engineer (Data platform)

### Empresas-Alvo

**Consultorias (Alta probabilidade):**
- Accenture, Deloitte, KPMG, PwC (áreas Data & AI)
- Tivit, Stefanini, CI&T, ThoughtWorks
- Indicium, Aquarela, Tail (boutiques nacionais)

**Tech Companies:**
- Bancos digitais (Nubank, Inter, C6)
- Fintechs (Stone, PagSeguro)
- Healthtechs (Alice, Conexa Saúde)
- Grandes varejistas (Magalu, Via)

**Setor Público/Híbrido:**
- Serpro, Dataprev (modernização)
- Tribunais (TRFs, TST, TCU)
- Sebrae nacional
- Empresas públicas (BB, CEF)

**Startups Scaleup:**
- Séries B+ com maturidade em dados
- Procurando primeiro Data Lead

### Faixa Salarial (Referência 2024/2025)

**CLT:**
- Senior Data Engineer: R$ 15k - 25k
- Lead/Staff Data Engineer: R$ 25k - 35k
- Data Architect: R$ 30k - 45k
- Head of Data: R$ 40k - 60k

**PJ (Consultoria):**
- Hourly: R$ 200 - 400/hora
- Projetos: R$ 80k - 150k (3-6 meses)

**Remoto Internacional:**
- USD $120k - $180k/ano (via Toptal, Remote.com)

---

## 💡 CONTEXTO PARA CODING SESSIONS

### Quando Trabalhar em Projetos

**Prioridades:**
1. **Funcionalidade > Perfeição:** MVP working > solução elegante incompleta
2. **Documentação = Código:** README tão importante quanto implementação
3. **Demo-friendly:** Sempre pensar em como demonstrar (screenshots, vídeos)
4. **Portfolio-oriented:** Código limpo e bem comentado (pessoas vão ler)

**Workflow Preferido:**
1. Criar estrutura de diretórios
2. Implementar funcionalidade core
3. Adicionar interface (Streamlit)
4. Testar com dados reais (anonimizados)
5. Documentar (README, docstrings)
6. Criar exemplos (screenshots, vídeo)
7. Publicar (GitHub + post LinkedIn)

### Padrões de Código

**Python Style:**
- PEP 8 compliant
- Type hints sempre que possível
- Docstrings em funções públicas
- Logging estruturado (não prints)
- Tratamento de erros explícito
- Constants em UPPERCASE

**Exemplo:**
```python
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class SchemaAnalyzer:
    """Analyze database schemas and extract metadata.
    
    This class provides methods to connect to databases,
    extract schema information, and prepare it for LLM analysis.
    """
    
    def __init__(self, connection_string: str):
        """Initialize the analyzer with a database connection.
        
        Args:
            connection_string: SQLAlchemy-style connection string
            
        Raises:
            ConnectionError: If unable to connect to database
        """
        self.connection_string = connection_string
        self._engine = None
        logger.info("SchemaAnalyzer initialized")
    
    def extract_tables(self, schema: Optional[str] = None) -> List[Dict[str, Any]]:
        """Extract table metadata from the database.
        
        Args:
            schema: Optional schema name to filter tables
            
        Returns:
            List of dictionaries containing table metadata
            
        Example:
            >>> analyzer = SchemaAnalyzer("mysql://...")
            >>> tables = analyzer.extract_tables(schema="public")
            >>> print(tables[0]['name'])
            'customers'
        """
        try:
            # Implementation
            logger.info(f"Extracting tables from schema: {schema}")
            return tables
        except Exception as e:
            logger.error(f"Failed to extract tables: {e}")
            raise
```

**SQL Style:**
```sql
-- Calculate monthly revenue by product category
-- Includes year-over-year comparison

with monthly_sales as (
    select
        date_trunc('month', order_date) as month,
        product_category,
        sum(order_value) as total_revenue,
        count(distinct order_id) as order_count
    from 
        orders
    where 
        order_status = 'completed'
        and order_date >= '2023-01-01'
    group by 
        1, 2
),

yoy_comparison as (
    select
        month,
        product_category,
        total_revenue,
        lag(total_revenue, 12) over (
            partition by product_category 
            order by month
        ) as revenue_last_year,
        round(
            100.0 * (total_revenue - lag(total_revenue, 12) over (
                partition by product_category order by month
            )) / nullif(lag(total_revenue, 12) over (
                partition by product_category order by month
            ), 0),
            2
        ) as yoy_growth_pct
    from 
        monthly_sales
)

select
    month,
    product_category,
    total_revenue,
    revenue_last_year,
    yoy_growth_pct
from 
    yoy_comparison
where 
    month >= '2024-01-01'
order by 
    month desc, 
    total_revenue desc;
```

**Git Commit Messages:**
```
feat: add LLM-based schema documentation generator
fix: handle NULL values in column descriptions
docs: update README with installation instructions
refactor: extract embedding logic into separate module
test: add unit tests for SQL parser
chore: update dependencies to latest versions
```

### Estrutura de README (Template)

```markdown
# 🚀 [Nome do Projeto]

[Badge do Python] [Badge do License] [Badge de Status]

> Uma linha descrevendo o projeto

## 🎯 Problema

Descreva o problema real que este projeto resolve. Use dados ou exemplos concretos.

## ✨ Solução

Como o projeto resolve o problema. Quais são os benefícios principais.

## 🚀 Features

- ✅ Feature principal 1
- ✅ Feature principal 2
- ✅ Feature principal 3
- 🔄 Feature em desenvolvimento
- 📝 Feature planejada

## 🛠️ Stack Técnico

- **Backend:** Python 3.10+, LangChain, OpenAI API
- **Database:** SQLAlchemy (MySQL, PostgreSQL)
- **Frontend:** Streamlit
- **Deployment:** Docker (optional)

## 📦 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- OpenAI API key
- [Outros requisitos]

### Passo a Passo

```bash
# Clone o repositório
git clone https://github.com/[seu-usuario]/[projeto].git
cd [projeto]

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas credenciais

# Execute o app
streamlit run app.py
```

## 💻 Uso

### Exemplo Básico

```python
from src.database_doc import DatabaseDocumenter

# Inicializar
documenter = DatabaseDocumenter(
    connection_string="mysql://user:pass@localhost/db",
    openai_api_key="sk-..."
)

# Gerar documentação
docs = documenter.generate_documentation()

# Salvar como Markdown
documenter.save_to_markdown("database_docs.md")
```

### Interface Web

![Screenshot do app](examples/screenshots/main_screen.png)

1. Abra o app: `streamlit run app.py`
2. Insira credenciais do database
3. Clique em "Analisar Schema"
4. Visualize e exporte a documentação

## 📊 Exemplos

- [Exemplo de output para database de e-commerce](examples/ecommerce_output.md)
- [Exemplo de output para database de RH](examples/hr_output.md)

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Com coverage
pytest --cov=src tests/

# Apenas um módulo
pytest tests/test_database_connector.py
```

## 📈 Roadmap

- [ ] Suporte para Oracle e SQL Server
- [ ] Export para dbt schema.yml
- [ ] Detecção automática de PII
- [ ] API REST para integração
- [ ] Tracking de mudanças de schema (versioning)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Paulo** - Data Architect & AI Engineer

- LinkedIn: [seu-perfil]
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu.email@example.com

## 🙏 Agradecimentos

- [Recursos ou inspirações]
- [Bibliotecas importantes usadas]

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
```

### Preferências de Desenvolvimento

**Environment Setup:**
```bash
# Sempre usar venv
python -m venv venv
source venv/bin/activate

# requirements.txt organizado
# requirements.txt
langchain==0.1.0
openai==1.3.0
streamlit==1.28.0
sqlalchemy==2.0.23

# requirements-dev.txt
pytest==7.4.3
black==23.11.0
flake8==6.1.0
mypy==1.7.0
```

**Environment Variables:**
```bash
# .env.example (commitar)
OPENAI_API_KEY=your_key_here
DATABASE_URL=mysql://user:pass@localhost:3306/dbname
VECTOR_DB_PATH=./vector_db
LOG_LEVEL=INFO

# .env (NUNCA commitar)
OPENAI_API_KEY=sk-real-key-here
DATABASE_URL=mysql://realuser:realpass@prod.server.com:3306/proddb
```

**.gitignore Essencial:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# Data
data/raw/*
!data/raw/.gitkeep
vector_db/
*.db

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db
```

### Limitações e Constraints

**Budget:**
- Usar free tiers quando possível
- OpenAI: começar com gpt-3.5-turbo, usar gpt-4 apenas quando necessário
- Vector DBs: preferir Chroma (local) antes de Pinecone (pago)
- Cloud: usar GCP free tier

**Time:**
- MVPs em 8-12h cada
- Priorizar funcionalidade core
- Documentação mínima viable
- Testes básicos (não coverage 100%)

**Deployment:**
- Começar local (Streamlit)
- Docker opcional (se tempo permitir)
- Deploy para Cloud pode vir depois

### Perguntas Frequentes para o Cursor

**"Como devo estruturar este módulo?"**
→ Função clara, bem documentada, type hints, error handling

**"Devo usar esta biblioteca X ou Y?"**
→ Preferir: mais popular, melhor documentada, mais simples

**"Este código está bom o suficiente?"**
→ Perguntar: Funciona? É legível? Está documentado? Se sim, é bom o suficiente para MVP.

**"Devo adicionar testes?"**
→ Testes básicos sempre. Coverage completo apenas se tempo permitir.

**"Como melhorar performance?"**
→ Primeiro fazer funcionar, depois otimizar se necessário (measure, don't guess)

---

## 📊 MÉTRICAS DE SUCESSO

### Portfolio (1 Semana)
- ✅ 3 projetos completos e funcionais
- ✅ READMEs profissionais (seguir template)
- ✅ 3 vídeos demo (2-3min cada)
- ✅ 1 artigo técnico publicado (Medium/LinkedIn)
- ✅ GitHub profile otimizado

### Job Search (1 Semana)
- ✅ 25+ aplicações para vagas relevantes
- ✅ 20+ conexões estratégicas no LinkedIn
- ✅ 15+ headhunters contatados
- ✅ 5+ posts de conteúdo no LinkedIn
- ✅ 10+ respostas/interações recebidas

### Learning (2 Semanas)
- ✅ 1 certificação obtida (Microsoft AI-900)
- ✅ 3 cursos completos (DeepLearning.AI)
- ✅ RAG architecture implementada
- ✅ LangChain proficiency
- ✅ Vector databases hands-on

### Networking (Contínuo)
- 🎯 3+ conversas com decisores por semana
- 🎯 2+ interviews técnicas por semana
- 🎯 1+ coffee chat semanal
- 🎯 Participar de 2+ eventos tech (presencial/virtual)

### Financial (30-60 dias)
- 🎯 1+ oferta de emprego CLT
- 🎯 2+ projetos freela em negociação
- 🎯 Portfolio gerando inbound leads

---

## 🚨 STATUS ATUAL & PRÓXIMOS PASSOS

### ✅ Completado
- [x] Plano de ação detalhado criado
- [x] Gap analysis de conhecimentos
- [x] Especificação de 3 projetos portfolio
- [x] Lista de headhunters compilada
- [x] 5 posts LinkedIn preparados
- [x] Plano de estudos de 3 semanas
- [x] Contexto completo para Cursor criado

### 🔄 Em Andamento
- [ ] Projeto 1: Database Doc Assistant (0%)
- [ ] Projeto 2: Data Lineage Analyzer (0%)
- [ ] Projeto 3: RAG Data Dictionary (0%)
- [ ] Estudos: Semana 1 de 3 (0%)
- [ ] Job applications: 0 de 25+
- [ ] Headhunters contatados: 0 de 15+
- [ ] Posts publicados: 0 de 5

### 📝 Próximas 24 Horas
1. Configurar ambiente de desenvolvimento
2. Iniciar Projeto 1 (Database Doc Assistant)
3. Atualizar perfil LinkedIn
4. Publicar primeiro post
5. Contatar primeiros 5 headhunters

### 📅 Esta Semana (Prioridade)
- **Segunda:** Setup + Projeto 1 + LinkedIn
- **Terça:** Finalizar Projeto 1 + Networking
- **Quarta:** Projeto 2 + Applications
- **Quinta:** Finalizar Projeto 2 + Certificação
- **Sexta:** Projeto 3 + Freela platforms
- **Sábado:** Continuar Projeto 3 + Estudos
- **Domingo:** Finalizar Projeto 3 + Planejamento Semana 2

---

## 🎯 QUICK REFERENCE

**Em dúvida sobre:**

❓ **Qual biblioteca usar?**
→ LangChain para LLM apps, SQLAlchemy para DB, Streamlit para UI

❓ **Como estruturar código?**
→ Seguir estrutura de diretórios especificada nos projetos

❓ **Quanto tempo dedicar?**
→ Funcionalidade core: 60%, Documentação: 25%, Testes: 15%

❓ **Deploy ou não?**
→ MVP local primeiro, deploy opcional depois

❓ **Quanto detalhar README?**
→ Seguir template fornecido, incluir screenshots

❓ **Devo otimizar agora?**
→ Só se estiver lento demais. Funcionalidade > Performance em MVP

❓ **Tests são obrigatórios?**
→ Testes básicos sim. Coverage 100% não.

❓ **Como escolher entre opções?**
→ Mais simples, mais popular, melhor documentação

---

## 📞 CONTATO & LINKS

**Profissional:**
- LinkedIn: [seu perfil]
- GitHub: [seu usuario]
- Email: [seu email]
- Portfolio: [link quando criado]

**Recursos Chave:**
- DeepLearning.AI: https://www.deeplearning.ai/short-courses/
- LangChain Docs: https://python.langchain.com/docs/
- dbt Learn: https://learn.getdbt.com/
- Made With ML: https://madewithml.com/

**Comunidades:**
- dbt Slack: https://www.getdbt.com/community/
- Data Engineering Brasil: [Telegram]
- AI Brasil: [Discord]

---

## 🔄 HISTÓRICO DE ATUALIZAÇÕES

**2024-XX-XX:** Documento inicial criado
- Definido stack técnico atual e gaps
- Especificados 3 projetos portfolio
- Criado plano de estudos de 3 semanas
- Listados headhunters e estratégia de job search

---

## 💭 FILOSOFIA DE DESENVOLVIMENTO

**Para Projetos Portfolio:**
1. **Show, don't tell:** Código funcional > descrições longas
2. **Document for humans:** README como pitch de vendas
3. **Demo-driven:** Se não pode demonstrar em 2min, simplifique
4. **Real problems:** Resolver dores reais, não toy examples
5. **Ship fast:** MVP em dias, não semanas

**Para Aprendizado:**
1. **Build to learn:** Fazer é melhor que apenas ler
2. **80/20 rule:** Aprender o suficiente para ser produtivo
3. **Just-in-time learning:** Aprender quando precisar usar
4. **Document insights:** Escrever solidifica aprendizado

**Para Job Search:**
1. **Quality > Quantity:** 10 applications pensadas > 50 genéricas
2. **Network first:** Referrals > job boards
3. **Content marketing:** Posts atraem oportunidades
4. **Be visible:** GitHub + LinkedIn + Articles

---

# ✅ FIM DO DOCUMENTO DE CONTEXTO

Este documento contém TUDO que o Cursor AI precisa saber para me assistir efetivamente na transição de carreira, desenvolvimento de projetos, e preparação para oportunidades.

**Princípio-guia:** 
Experiência sênior + Tecnologia moderna + Entrega rápida = Reposicionamento de sucesso

**Lembre-se:**
- Funcionalidade > Perfeição
- Documentação = Código
- MVP working > Solução elegante incompleta
- Demonstrações > Descrições

**Status:** Pronto para começar! 🚀

---

*Última atualização: [Data de hoje]*
*Próxima revisão: Ao final de cada projeto ou marco importante*
