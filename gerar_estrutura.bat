@echo off
echo Gerando estrutura da pasta "C:\projetos\paulo_sousa\paulo-career-accelerator"...

REM O comando 'tree' gera a estrutura. /F inclui os arquivos. > exporta o resultado.
tree "C:\projetos\paulo_sousa\paulo-career-accelerator" /F > "pasta_estrutura.txt"

echo.
echo Concluído! Estrutura salva no arquivo "pasta_sebrae_ba.txt".
pause