# ==========================================================
# Script: executar_criar_estrutura_pesquisa.ps1
# Objetivo: Criar estrutura completa da pesquisa científica
# conforme especificado em criar_estrutura_pesquisa.md
# ==========================================================

Write-Host "🚀 Iniciando criação da estrutura de pesquisa..." -ForegroundColor Cyan

# Caminho base
$base = "docs/99-prompts/2-pesquisa-cientifica"

# Diretórios
$dirs = @(
    "00-orientacoes",
    "01-problema",
    "02-revisao-literatura/fichamentos",
    "03-metodologia",
    "04-coleta-dados/dados-brutos",
    "04-coleta-dados/questionarios",
    "04-coleta-dados/entrevistas",
    "05-analise-resultados/scripts",
    "05-analise-resultados/tabelas",
    "05-analise-resultados/figuras",
    "06-relatorio-final/slides-apresentacao",
    "07-prompts-pesquisa",
    "08-artigos-referencia/artigos-pdf"
)

foreach ($dir in $dirs) {
    $path = Join-Path $base $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
        Write-Host "📂 Criado: $path"
    } else {
        Write-Host "⚠️ Já existe: $path"
    }
}

# Arquivos com conteúdo
$arquivos = @{
    "00-orientacoes/README.md" = @"
# Projeto de Pesquisa: A influência da inteligência artificial no processo de escrita acadêmica
Este repositório demonstra todas as etapas da pesquisa — da formulação do problema à redação final.
"@
    "00-orientacoes/cronograma.md" = "# Cronograma da Pesquisa\n\n| Etapa | Período | Responsável |\n|-------|----------|-------------|\n| Formulação do Problema | Semana 1 | Equipe |\n| Revisão de Literatura | Semanas 2-3 | Pesquisador |\n| Coleta de Dados | Semana 4 | Equipe |\n| Análise e Relatório | Semana 5 | Orientador |"
    "00-orientacoes/equipe.md" = "# Equipe de Pesquisa\n\n- Orientador: Prof. Dr. Thales Levi Azevedo Valente\n- Discentes: [Nome dos alunos]\n- Apoio técnico: IA Assistente"
    "00-orientacoes/glossario.md" = "# Glossário de Termos\n\n- **IA**: Inteligência Artificial\n- **Revisão Sistemática**: método estruturado de levantamento bibliográfico."
    "01-problema/pergunta-central.md" = "# Pergunta Central\n\nComo a inteligência artificial influencia o processo de escrita acadêmica de estudantes universitários?"
    "01-problema/justificativa.md" = "# Justificativa\n\nA crescente adoção de ferramentas de IA na educação motiva a análise de seus impactos na escrita científica."
    "01-problema/objetivos.md" = "# Objetivos\n\n**Geral:** Investigar como a IA afeta a escrita acadêmica.\n\n**Específicos:**\n- Identificar percepções de estudantes;\n- Avaliar mudanças no estilo de escrita;\n- Propor diretrizes para uso ético."
    "02-revisao-literatura/referencias-principais.md" = "# Referências Principais\n\n- Freire (1987)\n- Lévy (1999)\n- Carvalho (2020)"
    "02-revisao-literatura/matriz-sintese.md" = "# Matriz de Síntese\n\n| Autor | Ano | Contribuição |\n|--------|------|---------------|\n| Freire | 1987 | Educação libertadora |\n| Lévy | 1999 | Inteligência coletiva |"
    "03-metodologia/tipo-pesquisa.md" = "# Tipo de Pesquisa\n\nAbordagem qualitativa, exploratória e descritiva, com coleta de dados via questionário e entrevistas."
    "03-metodologia/instrumentos-coleta.md" = "# Instrumentos de Coleta\n\nQuestionário semiestruturado aplicado a estudantes de graduação."
    "03-metodologia/plano-analise.md" = "# Plano de Análise\n\nAnálise de conteúdo das respostas, com codificação e agrupamento temático."
    "05-analise-resultados/discussoes.md" = "# Discussão dos Resultados\n\nOs dados coletados indicam que a IA é vista como ferramenta auxiliar na escrita, mas há preocupações éticas."
    "06-relatorio-final/artigo.md" = "# Estrutura do Artigo Científico\n\n## 1 Introdução\n## 2 Metodologia\n## 3 Resultados e Discussão\n## 4 Conclusões"
    "06-relatorio-final/resumo-expandido.md" = "# Resumo Expandido\n\nA pesquisa analisa a influência da IA no processo de escrita científica, destacando avanços e desafios éticos."
    "06-relatorio-final/checklist-final.md" = "# Checklist Final\n\n- [x] Problema formulado\n- [x] Metodologia definida\n- [x] Dados coletados\n- [x] Resultados analisados\n- [x] Relatório completo"
    "07-prompts-pesquisa/p1-problema.md" = "# Prompt — Formulação do Problema\n\n> Gere ideias de perguntas de pesquisa relacionadas ao impacto da IA na escrita científica."
    "07-prompts-pesquisa/p2-revisao.md" = "# Prompt — Revisão de Literatura\n\n> Busque e resuma artigos sobre IA e produção acadêmica."
    "07-prompts-pesquisa/p3-metodologia.md" = "# Prompt — Metodologia\n\n> Sugira métodos qualitativos adequados para investigar percepções sobre IA na escrita."
    "07-prompts-pesquisa/p4-analise.md" = "# Prompt — Análise de Resultados\n\n> Gere interpretações automáticas de dados com base em respostas coletadas."
    "07-prompts-pesquisa/p5-relatorio.md" = "# Prompt — Relatório Final\n\n> Crie um resumo estruturado dos achados da pesquisa."
    "08-artigos-referencia/referencias.bib" = "@book{freire1987, title={Pedagogia do Oprimido}, author={Freire, Paulo}, year={1987}}"
}

foreach ($item in $arquivos.GetEnumerator()) {
    $file = Join-Path $base $item.Key
    $conteudo = $item.Value
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Path $file -Force | Out-Null
        Set-Content -Path $file -Value $conteudo -Encoding UTF8
        Write-Host "📝 Criado arquivo: $file"
    } else {
        Write-Host "⚠️ Já existe arquivo: $file"
    }
}

Write-Host "`n✅ Estrutura da pesquisa criada e populada com sucesso!" -ForegroundColor Green
