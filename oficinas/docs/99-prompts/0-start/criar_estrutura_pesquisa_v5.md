# System Spec — Pesquisa Científica (Manifesto Estrito v2.2)
# Objetivo: criar **exatamente** a árvore abaixo com **todas** as pastas e **todos** os arquivos .md/.bib
# Execução: cole este arquivo no seu runner de specs (ChatGPT/Copilot/Agent) e execute.
# Regras: idempotente; não sobrescrever; logs Created/Exists; escrita atômica (arquivo.tmp → rename).

BEGIN_MANIFEST_JSON
{
  "version": "2.2",
  "mode": "create_tree",
  "idempotent": true,
  "log": true,
  "base_dir": "docs/99-prompts/2-pesquisa-cientifica",
  "dirs": [
    "00-orientacoes",
    "01-problema",
    "02-revisao-literatura",
    "02-revisao-literatura/fichamentos",
    "03-metodologia",
    "04-coleta-dados",
    "04-coleta-dados/dados-brutos",
    "04-coleta-dados/questionarios",
    "04-coleta-dados/entrevistas",
    "05-analise-resultados",
    "05-analise-resultados/scripts",
    "05-analise-resultados/tabelas",
    "05-analise-resultados/figuras",
    "06-relatorio-final",
    "06-relatorio-final/slides-apresentacao",
    "07-prompts-pesquisa",
    "08-artigos-referencia",
    "08-artigos-referencia/artigos-pdf"
  ],
  "files": [
    { "path": "00-orientacoes/README.md", "content": "# Projeto de Pesquisa: IA na escrita acadêmica\nEste repositório demonstra todas as etapas de uma pesquisa — da formulação do problema ao relatório final — com organização clara para alunos iniciantes." },
    { "path": "00-orientacoes/cronograma.md", "content": "# Cronograma da Pesquisa\n| Etapa | Período | Responsável |\n|------|---------|-------------|\n| Problema | Sem 1 | Equipe |\n| Revisão | Sem 2-3 | Pesquisador |\n| Coleta | Sem 4 | Equipe |\n| Análise/Relatório | Sem 5 | Orientador |" },
    { "path": "00-orientacoes/equipe.md", "content": "# Equipe\n- Orientadora: Orientador: Prof. Dr. Thales Levi Azevedo Valente\n- Discentes: <nomes>\n- Apoio técnico: Assistente de IA" },
    { "path": "00-orientacoes/glossario.md", "content": "# Glossário\n- **IA**: Inteligência Artificial.\n- **Revisão sistemática**: método estruturado de síntese de estudos." },
    { "path": "01-problema/pergunta-central.md", "content": "# Pergunta Central\nComo a IA influencia a escrita acadêmica de estudantes universitários?" },
    { "path": "01-problema/justificativa.md", "content": "# Justificativa\nAdoção crescente de IA na educação exige evidências sobre impacto, ética e autonomia." },
    { "path": "01-problema/objetivos.md", "content": "# Objetivos\n**Geral:** Investigar efeitos da IA na escrita acadêmica.\n**Específicos:** percepções, mudanças de estilo, diretrizes de uso responsável." },
    { "path": "02-revisao-literatura/referencias-principais.md", "content": "# Referências principais (inicial)\nFreire (1987); Lévy (1999); Carvalho (2020)." },
    { "path": "02-revisao-literatura/matriz-sintese.md", "content": "# Matriz de síntese (rascunho)\n| Autor | Ano | Contribuição |\n|-------|-----|--------------|\n| Freire | 1987 | Autonomia |\n| Lévy | 1999 | Mediação |\n| Carvalho | 2020 | IA na escrita |" },
    { "path": "03-metodologia/tipo-pesquisa.md", "content": "# Tipo de Pesquisa\nQualitativa, exploratória-descritiva; questionário + entrevistas." },
    { "path": "03-metodologia/instrumentos-coleta.md", "content": "# Instrumentos de Coleta\nQuestionário semiestruturado; roteiro de entrevista (30–45 min)." },
    { "path": "03-metodologia/plano-analise.md", "content": "# Plano de Análise\nCodificação temática → eixos → categorias; triangulação de fontes." },
    { "path": "05-analise-resultados/discussoes.md", "content": "# Discussões (rascunho)\nUtilidade percebida, mudanças de estilo, dilemas éticos." },
    { "path": "06-relatorio-final/artigo.md", "content": "# Estrutura do Artigo\n## 1 Introdução\n## 2 Metodologia\n## 3 Resultados e Discussão\n## 4 Conclusões" },
    { "path": "06-relatorio-final/resumo-expandido.md", "content": "# Resumo Expandido\nObjetivo, método, principais achados, limitações e implicações." },
    { "path": "06-relatorio-final/checklist-final.md", "content": "# Checklist Final\n- [ ] Problema/objetivos claros\n- [ ] Revisão coerente\n- [ ] Método adequado\n- [ ] Dados organizados\n- [ ] Resultados interpretados\n- [ ] Referências padronizadas" },
    { "path": "07-prompts-pesquisa/p1-problema.md", "content": "# Prompt — Problema\nGere 5 perguntas de pesquisa (variáveis, recortes, justificativas)." },
    { "path": "07-prompts-pesquisa/p2-revisao.md", "content": "# Prompt — Revisão\nSugira descritores e 3 fichamentos-modelo (150–200 palavras)." },
    { "path": "07-prompts-pesquisa/p3-metodologia.md", "content": "# Prompt — Metodologia\nProponha desenho qualitativo, amostragem e instrumentos." },
    { "path": "07-prompts-pesquisa/p4-analise.md", "content": "# Prompt — Análise\nPlano de codificação temática e exemplos de categorias." },
    { "path": "07-prompts-pesquisa/p5-relatorio.md", "content": "# Prompt — Relatório\nEsboce Introdução, Método e Discussão em 2–3 parágrafos cada." },
    { "path": "08-artigos-referencia/referencias.bib", "content": "@book{freire1987, title={Pedagogia do Oprimido}, author={Freire, Paulo}, year={1987}}" }
  ]
}
END_MANIFEST_JSON

# Critérios de sucesso:
# - Todos os diretórios de 'dirs' existem.
# - Todos os 'files' existem e, se recém-criados, contêm o conteúdo acima.
# - Logs por item: Created/Exists.
# - Resumo final: dirs_created, dirs_existing, files_created, files_existing.
