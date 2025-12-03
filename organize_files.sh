#!/bin/bash

# Script de Organização de Arquivos - Paulo Career Accelerator
# Data: 27 Novembro 2025
# Propósito: Mover arquivos da pasta Download para estrutura do projeto

echo "🚀 Iniciando organização de arquivos..."

# Definir variáveis (AJUSTE O CAMINHO SE NECESSÁRIO)
DOWNLOAD_DIR="$HOME/Downloads"
PROJECT_DIR="$HOME/paulo-career-accelerator"

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Criar estrutura de diretórios se não existir
echo -e "${BLUE}📁 Criando estrutura de diretórios...${NC}"

mkdir -p "$PROJECT_DIR/docs/planning"
mkdir -p "$PROJECT_DIR/docs/automation"
mkdir -p "$PROJECT_DIR/docs/tracking"
mkdir -p "$PROJECT_DIR/projects/01-database-documentation-assistant"
mkdir -p "$PROJECT_DIR/projects/02-data-lineage-analyzer"
mkdir -p "$PROJECT_DIR/projects/03-rag-data-dictionary"
mkdir -p "$PROJECT_DIR/resources/resume"
mkdir -p "$PROJECT_DIR/resources/certifications"

# Mover arquivos de planejamento
echo -e "${BLUE}📄 Movendo arquivos de planejamento...${NC}"

mv "$DOWNLOAD_DIR/00_INDICE_MASTER_PROJETO.md" "$PROJECT_DIR/docs/planning/" 2>/dev/null && \
    echo -e "${GREEN}✅ 00_INDICE_MASTER_PROJETO.md movido${NC}"

mv "$DOWNLOAD_DIR/PLANO_ESTUDO_25_DIAS.md" "$PROJECT_DIR/docs/planning/" 2>/dev/null && \
    echo -e "${GREEN}✅ PLANO_ESTUDO_25_DIAS.md movido${NC}"

mv "$DOWNLOAD_DIR/ESTRATEGIA_COMPLETA_FINAL.md" "$PROJECT_DIR/docs/planning/" 2>/dev/null && \
    echo -e "${GREEN}✅ ESTRATEGIA_COMPLETA_FINAL.md movido${NC}"

mv "$DOWNLOAD_DIR/LINKEDIN_CV_OPTIMIZATION.md" "$PROJECT_DIR/docs/planning/" 2>/dev/null && \
    echo -e "${GREEN}✅ LINKEDIN_CV_OPTIMIZATION.md movido${NC}"

mv "$DOWNLOAD_DIR/CAREER_ROADMAP.md" "$PROJECT_DIR/" 2>/dev/null && \
    echo -e "${GREEN}✅ CAREER_ROADMAP.md movido para raiz${NC}"

mv "$DOWNLOAD_DIR/README_OPTIMIZED.md" "$PROJECT_DIR/README.md" 2>/dev/null && \
    echo -e "${GREEN}✅ README_OPTIMIZED.md → README.md (raiz)${NC}"

# Mover CV (se existir)
if [ -f "$DOWNLOAD_DIR/CV_Paulo_César_M_Sousa_Jr20250515det.pdf" ]; then
    mv "$DOWNLOAD_DIR/CV_Paulo_César_M_Sousa_Jr20250515det.pdf" "$PROJECT_DIR/resources/resume/" && \
    echo -e "${GREEN}✅ CV movido para resources/resume/${NC}"
fi

echo ""
echo -e "${GREEN}✅ Organização completa!${NC}"
echo ""
echo "📂 Estrutura criada em: $PROJECT_DIR"
echo ""
echo "Próximos passos:"
echo "1. cd $PROJECT_DIR"
echo "2. git status (verificar mudanças)"
echo "3. git add ."
echo "4. git commit -m 'docs: organizar estrutura do projeto'"
echo "5. git push origin main"
