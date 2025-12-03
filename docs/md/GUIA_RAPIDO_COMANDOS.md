# ⚡ GUIA RÁPIDO DE COMANDOS - DIA 1

**Referência rápida para consulta durante o dia**

---

## 🚀 COMANDOS ESSENCIAIS

### Virtual Environment
```powershell
# Ativar venv
cd C:\projetos\paulo_sousa\paulo-career-accelerator
.\venv\Scripts\Activate.ps1

# Desativar venv
deactivate

# Verificar se está ativo
# Deve mostrar (venv) no prompt
```

### Python & Pip
```powershell
# Versão Python
python --version

# Versão pip
pip --version

# Listar pacotes instalados
pip list

# Instalar pacote
pip install <package-name>

# Instalar do requirements.txt
pip install -r requirements.txt

# Atualizar pip
python -m pip install --upgrade pip
```

### Git Básico
```powershell
# Status do repositório
git status

# Adicionar arquivos
git add .                    # Todos os arquivos
git add <filename>           # Arquivo específico

# Commit
git commit -m "mensagem"

# Push
git push origin main

# Pull (atualizar)
git pull origin main

# Ver histórico
git log --oneline -10        # Últimos 10 commits

# Ver branches
git branch -a
```

### GitHub CLI
```powershell
# Verificar autenticação
gh auth status

# Criar repo
gh repo create <name> --public --source=. --remote=origin

# Ver repos
gh repo list

# Abrir repo no navegador
gh repo view --web

# Criar issue
gh issue create --title "Título" --body "Descrição"

# Ver PRs
gh pr list
```

### VSCode
```powershell
# Abrir VSCode no diretório atual
code .

# Abrir arquivo específico
code <filename>

# Listar extensões instaladas
code --list-extensions

# Instalar extensão
code --install-extension <extension-id>
```

---

## 📂 NAVEGAÇÃO DE DIRETÓRIOS

### PowerShell
```powershell
# Ver diretório atual
pwd

# Listar arquivos
ls                           # Lista simples
ls -Force                    # Incluindo ocultos
Get-ChildItem -Recurse       # Recursivo (todos subdiretórios)

# Mudar diretório
cd <caminho>
cd ..                        # Subir um nível
cd ~                         # Home directory

# Criar diretório
mkdir <nome>
New-Item -ItemType Directory -Path <caminho>

# Criar arquivo
New-Item -ItemType File -Path <arquivo>
# OU
echo "" > <arquivo>

# Deletar
Remove-Item <arquivo>
Remove-Item -Recurse <diretório>  # Com subpastas
```

### Atalhos Úteis
```
Ctrl+C        → Copiar
Ctrl+V        → Colar
Ctrl+A        → Selecionar tudo
Tab           → Autocompletar
↑/↓           → Histórico de comandos
Ctrl+L        → Limpar tela (PowerShell)
```

---

## 🔍 PROJETO 1 - COMANDOS ESPECÍFICOS

### Setup Inicial
```powershell
# Navegar para projeto
cd projects/01-database-documentation-assistant

# Criar .env
cp .env.example .env

# Editar .env
code .env

# Instalar dependências
pip install -r requirements.txt
```

### Testes Rápidos
```powershell
# Testar imports
python -c "from src.database_connector import DatabaseConnector; print('✅ OK')"
python -c "from src.schema_extractor import SchemaExtractor; print('✅ OK')"
python -c "from src.llm_documentation_generator import create_documentation_generator; print('✅ OK')"

# Rodar tests (quando implementar)
pytest
pytest -v                    # Verbose
pytest tests/                # Diretório específico
pytest tests/test_*.py       # Arquivo específico

# Rodar com coverage
pytest --cov=src --cov-report=html
```

### Rodar Aplicação
```powershell
# Main script
python main.py --help        # Ver opções

# Com config file
python main.py --config config.yaml

# Com argumentos
python main.py \
    --db-type postgresql \
    --db-host localhost \
    --db-name mydb

# Streamlit (quando implementar)
streamlit run app.py
```

### Code Quality
```powershell
# Formatação com Black
black .                      # Formatar tudo
black <file.py>              # Arquivo específico

# Linting com Flake8
flake8 src/                  # Lint diretório
flake8 <file.py>             # Arquivo específico

# Type checking com MyPy
mypy src/
mypy <file.py>
```

---

## 📊 JUPYTER LAB

```powershell
# Iniciar Jupyter Lab
jupyter lab

# Criar notebook via linha de comando
jupyter notebook --notebook-dir=<path>

# Listar notebooks rodando
jupyter notebook list

# Parar servidor
Ctrl+C (no terminal onde iniciou)
```

---

## 🔧 TROUBLESHOOTING RÁPIDO

### Problema: Import Error
```powershell
# Verificar se venv está ativo
# Deve mostrar (venv) no prompt

# Reinstalar pacote
pip uninstall <package>
pip install <package>

# Verificar se está instalado
pip show <package>
```

### Problema: Git Push Rejeição
```powershell
# Pull primeiro
git pull origin main

# Se houver conflito, resolver manualmente
# Depois:
git add .
git commit -m "resolve merge conflict"
git push origin main
```

### Problema: VSCode não reconhece Python
```powershell
# Selecionar interpretador Python correto
# Ctrl+Shift+P → "Python: Select Interpreter"
# Escolher: .\venv\Scripts\python.exe
```

### Problema: PowerShell não reconhece comando
```powershell
# Fechar e reabrir PowerShell
# Se ainda não funcionar, adicionar ao PATH

# Verificar PATH
$env:PATH -split ';'
```

---

## 🎨 GITHUB COPILOT (VSCode)

```
Ctrl+I           → Abrir Copilot inline
Ctrl+Shift+I     → Abrir Copilot chat
Tab              → Aceitar sugestão
Esc              → Rejeitar sugestão
Alt+]            → Próxima sugestão
Alt+[            → Sugestão anterior
```

---

## 💡 DICAS PRODUTIVAS

### PowerShell Aliases
```powershell
# Criar alias temporário (válido na sessão atual)
Set-Alias -Name gs -Value "git status"
Set-Alias -Name gc -Value "git commit"
Set-Alias -Name gp -Value "git push"

# Usar
gs              # Equivale a: git status
gc -m "msg"     # Equivale a: git commit -m "msg"
gp origin main  # Equivale a: git push origin main
```

### Comandos Úteis
```powershell
# Encontrar arquivo
Get-ChildItem -Recurse -Filter "*.py" | Select-Object FullName

# Contar linhas de código
(Get-Content <file.py>).Count

# Buscar texto em arquivos
Select-String -Path "*.py" -Pattern "DatabaseConnector"

# Ver tamanho de diretório
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum

# Histórico de comandos
Get-History
Get-History | Where-Object {$_.CommandLine -like "*git*"}
```

---

## 📝 TEMPLATES DE COMMIT

### Conventional Commits
```bash
# Features
git commit -m "feat(db-doc): add markdown exporter"
git commit -m "feat(api): implement authentication"

# Fixes
git commit -m "fix(database): resolve connection timeout"
git commit -m "fix(ui): correct button alignment"

# Documentation
git commit -m "docs(readme): add installation guide"
git commit -m "docs(api): update endpoint documentation"

# Chores
git commit -m "chore(deps): update dependencies"
git commit -m "chore(config): add eslint configuration"

# Refactor
git commit -m "refactor(schema): optimize query performance"

# Tests
git commit -m "test(connector): add unit tests for DatabaseConnector"

# Breaking changes
git commit -m "feat(api)!: change authentication method"
```

---

## 🎯 COMANDOS DO DIA 1

### Manhã (9h-13h)
```powershell
# 1. Ativar ambiente
cd C:\projetos\paulo_sousa\paulo-career-accelerator
.\venv\Scripts\Activate.ps1

# 2. Abrir VSCode
code .

# 3. Verificar Git
git status
git pull origin main

# 4. Iniciar Jupyter (para Academy)
jupyter lab
```

### Tarde (14h-17h)
```powershell
# 1. Navegar para Projeto 1
cd projects/01-database-documentation-assistant

# 2. Setup
cp .env.example .env
code .env

# 3. Instalar deps (se necessário)
pip install -r requirements.txt

# 4. Testar módulos
python -c "from src.database_connector import DatabaseConnector; print('✅')"
python -c "from src.schema_extractor import SchemaExtractor; print('✅')"

# 5. Implementar feature (markdown exporter)
code src/markdown_exporter.py

# 6. Testar
python -c "from src.markdown_exporter import MarkdownExporter; print('✅')"

# 7. Commitar
git add .
git commit -m "feat(db-doc): add markdown exporter"
git push origin main

# 8. Criar tag
git tag v0.2.0 -m "Add markdown export functionality"
git push origin v0.2.0
```

---

## 📞 AJUDA RÁPIDA

### Se algo der errado:
1. **Leia a mensagem de erro completa**
2. **Google o erro** (copie a mensagem exata)
3. **Consulte documentação** (README.md do projeto)
4. **Use GitHub Copilot** (Ctrl+I no VSCode)
5. **Peça ajuda** neste chat do framework

### Recursos de Suporte:
- 🤖 GitHub Copilot (Ctrl+I)
- 🔍 Google + Stack Overflow
- 📚 Documentação oficial (Python, Git, etc.)
- 💬 Claude Pro (este chat)
- 📖 Academy materiais

---

## ✅ CHECKLIST DE FIM DE DIA

```powershell
# Antes de encerrar:

# 1. Commitar mudanças
git status
git add .
git commit -m "chore: end of day 1 progress"
git push origin main

# 2. Atualizar Notion
# - Marcar tarefas concluídas
# - Adicionar notas do que aprendeu

# 3. Backup (opcional)
# - Se fez muitas mudanças importantes
git tag checkpoint-dia1-$(Get-Date -Format "yyyy-MM-dd")
git push --tags

# 4. Desativar venv
deactivate

# 5. Fechar aplicações
# - VSCode
# - PowerShell
# - Jupyter Lab (Ctrl+C no terminal)
```

---

## 🎯 ÚLTIMA DICA

**Mantenha este arquivo aberto durante o dia!**

Use Ctrl+F para buscar comandos rapidamente quando precisar.

**Atalho útil:**
```powershell
# Abrir este arquivo rapidamente
code ~/Downloads/GUIA_RAPIDO_COMANDOS.md
```

---

**BOA EXECUÇÃO NO DIA 1! 🚀**
