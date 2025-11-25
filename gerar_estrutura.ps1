# Define o caminho da pasta raiz
$RootPath = "C:\projetos\paulo_sousa\paulo-career-accelerator"

# Define onde salvar (Na raiz do projeto)
$OutputFile = "$RootPath\pasta_estrutura.txt"

# Define as pastas a serem IGNORADAS
$ExcludeFolders = @("venv", ".git", ".idea", "__pycache__", ".vscode", "node_modules", "site-packages")

function Show-Tree {
    param (
        [string]$Path,
        [string]$Indent = "",
        [bool]$IsLast = $false
    )

    # Pega itens, ignorando erros de permissão
    $Items = Get-ChildItem -Path $Path -Force -ErrorAction SilentlyContinue

    # Filtra os itens
    $FilteredItems = $Items | Where-Object { $ExcludeFolders -notcontains $_.Name }
    
    $Count = $FilteredItems.Count
    $Index = 0

    foreach ($Item in $FilteredItems) {
        $Index++
        $IsLastItem = ($Index -eq $Count)
        
        # --- ALTERAÇÃO AQUI: Usando caracteres simples para evitar erro de codificação ---
        $Prefix = if ($IsLastItem) { "\--- " } else { "+--- " }
        $Line = "$Indent$Prefix$($Item.Name)"
        
        Write-Output $Line
        $Line | Out-File -FilePath $OutputFile -Append -Encoding utf8

        if ($Item.PSIsContainer) {
            $NextIndent = if ($IsLastItem) { "$Indent    " } else { "$Indent|   " }
            Show-Tree -Path $Item.FullName -Indent $NextIndent
        }
    }
}

Write-Host "Gerando estrutura da pasta: $RootPath" -ForegroundColor Cyan
Write-Host "Arquivo sera salvo em: $OutputFile" -ForegroundColor Cyan

# Cria/Limpa o arquivo
"Estrutura da pasta: $RootPath" | Out-File -FilePath $OutputFile -Encoding utf8
"Gerado em: $(Get-Date)" | Out-File -FilePath $OutputFile -Append -Encoding utf8
"--------------------------------------------------" | Out-File -FilePath $OutputFile -Append -Encoding utf8

Show-Tree -Path $RootPath

Write-Host "`nConcluido! Verifique o arquivo em: $OutputFile" -ForegroundColor Green