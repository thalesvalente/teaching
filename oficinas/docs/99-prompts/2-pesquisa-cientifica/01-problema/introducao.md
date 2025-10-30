# PROMPT — **Introdução** (somente) em LaTeX · ABNT/abnTeX2 · com busca web e BibTeX (append)
*(Foco exclusivo na Introdução; **não** incluir a pergunta central. A pergunta será inserida separadamente no `main.tex`.)*

## 🎯 Objetivo
Gerar **`docs/2-pesquisa-cientifica/01-problema/introducao.tex`** (600–900 palavras, PT‑BR) com a **Introdução** do artigo, em LaTeX (sem preâmbulo), seguindo ABNT e compatível com **abnTeX2**.  
Citar **no mínimo 10 referências** e **apensar** (append) as entradas BibTeX em `docs/2-pesquisa-cientifica/08-artigos-referencia/referencias.bib`, **sem sobrescrever** o conteúdo existente (deduplicação por DOI > URL > title+year).

---

## 🔐 PAC (Política de Ação e Controle)
- **Web ON (read‑only)** 2023–2025. Priorizar bases públicas: **SciELO**, **DOAJ**, **PubMed Central**, **ERIC**, repositórios institucionais. Usar **Google Scholar apenas para descoberta** e **recuperar metadados na fonte original**.
- **Sem shell**. Apenas operações de arquivo.
- **UTF‑8** e **escrita atômica** (`*.tmp` → rename).
- **Idempotente**: criar diretórios/arquivos se faltarem; `.bib` sempre aberto em **append**; **não** duplicar entradas.
- **Logs**: `Created file: …`, `Appended refs: <N>`, `Skipped dup: <KEY>`.

---

## 📁 Caminhos
- **TEX (saída)**: `docs/2-pesquisa-cientifica/01-problema/introducao.tex`
- **BIB (append)**: `docs/2-pesquisa-cientifica/08-artigos-referencia/referencias.bib` (criar se não existir)

---

## ✅ Regras de Conformidade (ABNT + abnTeX2)
- **Citações**: **NBR 10520:2023**, sistema **autor‑data**; direta curta (≤3 linhas) **com página**; direta longa em bloco recuado; indireta autor‑data.
- **Referências**: **NBR 6023:2018** (elementos obrigatórios; **DOI/URL** e **`urldate`** quando aplicável).
- **Apresentação**: **NBR 14724:2024** (seções numeradas; Introdução antecede Métodos, Resultados e Discussão — **IMRaD**).
- **LaTeX/abnTeX2**: usar `\cite{}` e `\citeonline{}`; chaves ASCII; projeto compila com `abntex2-alf`.

---

## 🔎 Busca e seleção (mínimo **10** referências)
Coletar **≥10** fontes com distribuição sugerida:  
- **≥6** estudos empíricos/revisões sobre IA/LLMs/ChatGPT **na escrita acadêmica** (qualidade, revisão, feedback, avaliação).  
- **≥2** sobre **integridade/ética** (plágio, autoria, transparência).  
- **≥2** do **contexto brasileiro/ibero** (português/espanhol).  
Para cada item: `author`, `year`, `title`, `journal|booktitle`, `volume`, `number`, `pages`, **`doi`**, **`url`**, **`urldate` (AAAA‑MM‑DD)**, `language`.

---

## 🧱 Estrutura do TEX (gerar conteúdo final; **sem preâmbulo**)
Gravar o arquivo **substituindo integralmente** o conteúdo por:

```latex
\section{Introdução}\label{sec:introducao}
% Parágrafos 1--3: Contextualize o tema "IA e escrita acadêmica em estudantes universitários".
% Apresente mini-estado-da-arte (2023--2025), destacando benefícios (revisão, feedback, fluência)
% e riscos (homogeneização textual, autoria, plágio). Use \cite/\citeonline;
% quando for citação direta curta, informe página: \cite[p.~xx]{KEY}.

% Parágrafos 4--5: Aponte lacunas recentes (ex.: efeitos em cursos de graduação/língua portuguesa;
% implicações metacognitivas; política institucional; questões de transparência e ética),
% e situe o objetivo geral do estudo, SEM declarar a pergunta central.

% Último parágrafo: faça a transição para a pergunta de pesquisa (que será inserida externamente no main).
% Ex.: "À luz dessa discussão, a questão de pesquisa é explicitada na sequência deste trabalho."
```

> **Importante**: **não** incluir a pergunta central nesta Introdução. Ela será inserida manualmente no `main.tex`.

---

## 📚 BibTeX (append)
- Abrir/criar `BIB` em **append**.
- Inserir **uma entrada por chave citada** (`@article`, `@inproceedings`, `@book`, `@misc` quando indispensável).
- **Chave**: `sobrenomeYYYYpalavra` (ASCII, sem espaços/acentos).
- **Deduplicação**: checar `BIB` e pular duplicatas (mesmo `doi` ou `url` ou `title+year`). Se a entrada nova for mais completa, **mesclar sem apagar** campos válidos existentes.

---

## 🧪 QA e Relato
1) Conferir correspondência 1:1 entre `\cite{}` no TEX e entradas no `.bib`.  
2) Garantir `doi` **ou** `url` + `urldate` em cada entrada online.  
3) Exigir **≥10** referências distintas; reportar `Appended refs: <N>` (N ≥ 10).  
4) Exibir caminhos absolutos dos arquivos gerados/atualizados.
