# System Spec — Árvore LaTeX completa (ABNT/abnTeX2) · v1

> **Meta:** criar a **árvore inteira na raiz do projeto** usando **arquivos `.tex`** (não `.md`)
> e gerar um **`main.tex`** na raiz, configurado para **abnTeX2** com bibliografia em
> `docs/2-pesquisa-cientifica/08-artigos-referencia/referencias.bib`.
>
> **Referências de formatação**: abnTeX2 (classe/estilos) e normas ABNT para citação e referências
> (NBR 10520:2023; NBR 6023:2018; NBR 14724:2024).

---

## PAC (Política de Ação e Controle)
- **Idempotente:** não sobrescreva arquivos existentes; apenas crie os ausentes.
- **Escrita atômica:** grave em `*.tmp` e renomeie para o destino.
- **Logs obrigatórios:** `Created dir: …`, `Exists dir: …`, `Created file: …`, `Exists file: …`.
- **Codificação:** UTF‑8.
- **Ordem:** 1) diretórios → 2) arquivos → 3) sumário final (`dirs_created`, `files_created`, `files_existing`).

---

## BEGIN_MANIFEST_JSON
{
  "version": "1.0",
  "mode": "create_tree",
  "idempotent": true,
  "log": true,
  "base_dir": ".",
  "dirs": [
    "docs/2-pesquisa-cientifica/00-orientacoes",
    "docs/2-pesquisa-cientifica/01-problema",
    "docs/2-pesquisa-cientifica/02-revisao-literatura",
    "docs/2-pesquisa-cientifica/02-revisao-literatura/fichamentos",
    "docs/2-pesquisa-cientifica/03-metodologia",
    "docs/2-pesquisa-cientifica/04-coleta-dados",
    "docs/2-pesquisa-cientifica/04-coleta-dados/dados-brutos",
    "docs/2-pesquisa-cientifica/04-coleta-dados/questionarios",
    "docs/2-pesquisa-cientifica/04-coleta-dados/entrevistas",
    "docs/2-pesquisa-cientifica/05-analise-resultados",
    "docs/2-pesquisa-cientifica/05-analise-resultados/scripts",
    "docs/2-pesquisa-cientifica/05-analise-resultados/tabelas",
    "docs/2-pesquisa-cientifica/05-analise-resultados/figuras",
    "docs/2-pesquisa-cientifica/06-relatorio-final",
    "docs/2-pesquisa-cientifica/06-relatorio-final/slides-apresentacao",
    "docs/2-pesquisa-cientifica/07-prompts-pesquisa",
    "docs/2-pesquisa-cientifica/08-artigos-referencia",
    "docs/2-pesquisa-cientifica/08-artigos-referencia/artigos-pdf"
  ],
  "files": [
    {
      "path": "main.tex",
      "content": "\documentclass[12pt,oneside]{abntex2}\n% Pacotes usuais\n\usepackage[T1]{fontenc}\n\usepackage[utf8]{inputenc}\n\usepackage[brazil]{babel}\n\usepackage{lipsum}\n\n% Estilo de citações autor-data do abnTeX2\n\bibliographystyle{abntex2-alf}\n\n% Metadados mínimos\n\title{Projeto de Pesquisa}\n\author{Equipe da Oficina}\n\date{\today}\n\n\begin{document}\n\imprimircapa\n\tableofcontents\n\newpage\n\n% --- Inclusão das seções (use \input). São opcionais; inclua as que existirem.\n\IfFileExists{docs/2-pesquisa-cientifica/01-problema/pergunta-central.tex}{\input{docs/2-pesquisa-cientifica/01-problema/pergunta-central.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/01-problema/justificativa.tex}{\input{docs/2-pesquisa-cientifica/01-problema/justificativa.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/01-problema/objetivos.tex}{\input{docs/2-pesquisa-cientifica/01-problema/objetivos.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/02-revisao-literatura/referencias-principais.tex}{\input{docs/2-pesquisa-cientifica/02-revisao-literatura/referencias-principais.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/02-revisao-literatura/matriz-sintese.tex}{\input{docs/2-pesquisa-cientifica/02-revisao-literatura/matriz-sintese.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/03-metodologia/tipo-pesquisa.tex}{\input{docs/2-pesquisa-cientifica/03-metodologia/tipo-pesquisa.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/03-metodologia/instrumentos-coleta.tex}{\input{docs/2-pesquisa-cientifica/03-metodologia/instrumentos-coleta.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/03-metodologia/plano-analise.tex}{\input{docs/2-pesquisa-cientifica/03-metodologia/plano-analise.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/05-analise-resultados/discussoes.tex}{\input{docs/2-pesquisa-cientifica/05-analise-resultados/discussoes.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/06-relatorio-final/resumo-expandido.tex}{\input{docs/2-pesquisa-cientifica/06-relatorio-final/resumo-expandido.tex}}{}\n\IfFileExists{docs/2-pesquisa-cientifica/06-relatorio-final/artigo.tex}{\input{docs/2-pesquisa-cientifica/06-relatorio-final/artigo.tex}}{}\n\n% --- Referências (BibTeX)\n\bibliography{docs/2-pesquisa-cientifica/08-artigos-referencia/referencias}\n\end{document}\n"
    },
    { "path": "docs/2-pesquisa-cientifica/00-orientacoes/readme.tex", "content": "% README da oficina (LaTeX) — orientações gerais\n\section{Orientações Gerais}\nEste projeto demonstra a organização de uma pesquisa para graduandos." },
    { "path": "docs/2-pesquisa-cientifica/00-orientacoes/cronograma.tex", "content": "\section{Cronograma}\n\begin{tabular}{|l|l|l|}\n\hline Etapa & Período & Responsável \\\n\hline Problema & Sem 1 & Equipe \\\nRevisão & Sem 2--3 & Pesquisador \\\nColeta & Sem 4 & Equipe \\\nAnálise/Relatório & Sem 5 & Orientador \\\n\hline\end{tabular}" },
    { "path": "docs/2-pesquisa-cientifica/00-orientacoes/equipe.tex", "content": "\section{Equipe}\nOrientadora: Prof.ª Verônica Lima Costa\\Discentes: \textless nomes\textgreater{}\\Apoio técnico: Assistente de IA" },
    { "path": "docs/2-pesquisa-cientifica/00-orientacoes/glossario.tex", "content": "\section{Glossário}\n\textbf{IA}: Inteligência Artificial.\\\textbf{Revisão sistemática}: método estruturado de síntese de estudos." },
    { "path": "docs/2-pesquisa-cientifica/01-problema/pergunta-central.tex", "content": "\section{Pergunta Central}\n\noindent\textbf{Questão de pesquisa:} Como a inteligência artificial influencia a escrita acadêmica de estudantes universitários?" },
    { "path": "docs/2-pesquisa-cientifica/01-problema/justificativa.tex", "content": "\section{Justificativa}\n% Conteúdo a ser produzido em prompt específico (ABNT/autor-data)." },
    { "path": "docs/2-pesquisa-cientifica/01-problema/objetivos.tex", "content": "\section{Objetivos}\n\subsection{Objetivo Geral}\n% ...\n\subsection{Objetivos Específicos}\n\begin{itemize}\n\item ...\n\item ...\n\end{itemize}" },
    { "path": "docs/2-pesquisa-cientifica/02-revisao-literatura/referencias-principais.tex", "content": "\section{Referências Principais}\n% Listagem e breve contextualização dos autores-chave." },
    { "path": "docs/2-pesquisa-cientifica/02-revisao-literatura/matriz-sintese.tex", "content": "\section{Matriz de Síntese}\n% Tabela comparativa dos autores/achados." },
    { "path": "docs/2-pesquisa-cientifica/03-metodologia/tipo-pesquisa.tex", "content": "\section{Tipo de Pesquisa}\nQualitativa, exploratória e descritiva." },
    { "path": "docs/2-pesquisa-cientifica/03-metodologia/instrumentos-coleta.tex", "content": "\section{Instrumentos de Coleta}\nQuestionário semiestruturado e roteiro de entrevista." },
    { "path": "docs/2-pesquisa-cientifica/03-metodologia/plano-analise.tex", "content": "\section{Plano de Análise}\nCodificação temática; triangulação de fontes." },
    { "path": "docs/2-pesquisa-cientifica/05-analise-resultados/discussoes.tex", "content": "\section{Discussões}\n% Interpretação e conclusões parciais." },
    { "path": "docs/2-pesquisa-cientifica/06-relatorio-final/artigo.tex", "content": "\section{Artigo}\n% Estrutura do artigo final (seções serão consolidadas aqui)." },
    { "path": "docs/2-pesquisa-cientifica/06-relatorio-final/resumo-expandido.tex", "content": "\section{Resumo Expandido}\n% Objetivo, método, achados, limitações e implicações." },
    { "path": "docs/2-pesquisa-cientifica/06-relatorio-final/checklist-final.tex", "content": "\section{Checklist Final}\n\begin{itemize}\n\item Problema e objetivos claros;\n\item Revisão coerente;\n\item Método adequado;\n\item Dados organizados;\n\item Resultados interpretados;\n\item Referências padronizadas.\n\end{itemize}" },
    { "path": "docs/2-pesquisa-cientifica/07-prompts-pesquisa/p1-problema.tex", "content": "% Prompt LaTeX — P1 Problema (para runner de IA)\n\section*{P1 Problema}\nGere variações da pergunta de pesquisa e seus recortes." },
    { "path": "docs/2-pesquisa-cientifica/07-prompts-pesquisa/p2-revisao.tex", "content": "% Prompt LaTeX — P2 Revisão\n\section*{P2 Revisão}\nGere descritores e fichamentos (150--200 palavras)." },
    { "path": "docs/2-pesquisa-cientifica/07-prompts-pesquisa/p3-metodologia.tex", "content": "% Prompt LaTeX — P3 Metodologia\n\section*{P3 Metodologia}\nProponha desenho qualitativo, amostragem e instrumentos." },
    { "path": "docs/2-pesquisa-cientifica/07-prompts-pesquisa/p4-analise.tex", "content": "% Prompt LaTeX — P4 Análise\n\section*{P4 Análise}\nPlano de codificação temática e exemplos." },
    { "path": "docs/2-pesquisa-cientifica/07-prompts-pesquisa/p5-relatorio.tex", "content": "% Prompt LaTeX — P5 Relatório\n\section*{P5 Relatório}\nEsboce Introdução, Método e Discussão em 2--3 parágrafos cada." },
    { "path": "docs/2-pesquisa-cientifica/08-artigos-referencia/referencias.bib", "content": "% Arquivo BibTeX. Entradas serão APENSADAS (append) por prompts futuros.\n% Ex.: @article{sobrenome2024exemplo,\n%  author = {Sobrenome, Nome},\n%  title = {Título},\n%  year = {2024},\n%  journal = {Revista},\n%  volume = {1}, number = {1}, pages = {1--10},\n%  doi = {10.0000/xyz}, url={https://...}, urldate={2025-10-30}, language={portuguese}\n% }" }
  ]
}
## END_MANIFEST_JSON

---

## Notas técnicas
- **abnTeX2 (classe/estilos)**: fornece `abntex2-alf` (autor‑data) e macros compatíveis para trabalhos acadêmicos brasileiros. Consulte CTAN e documentação do projeto. 
- **Citações e referências**: siga NBR 10520:2023 (citação), NBR 6023:2018 (referências) e NBR 14724:2024 (estrutura).

