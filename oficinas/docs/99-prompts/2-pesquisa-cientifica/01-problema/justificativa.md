# PROMPT — **Justificativa** em LaTeX a partir de **Introdução** + **Pergunta Central**
# ABNT (NBR 10520/2023; NBR 6023/2018; NBR 14724/2024; NBR 6022/2018) · compatível com **abnTeX2**

## 🎯 Objetivo
Gerar **somente a subseção _Justificativa_** (LaTeX, sem preâmbulo) em:
- `OUT_TEX = docs/2-pesquisa-cientifica/01-problema/justificativa.tex`

Usar como insumos os arquivos já existentes:
- `INTRO = docs/2-pesquisa-cientifica/01-problema/introducao.tex`
- `PC1   = docs/2-pesquisa-cientifica/01-problema/pergunta-central.tex`
- `PC2   = docs/2-pesquisa-cientifica/01-problema/perguna-central.tex`  *(fallback para erro de digitação)*

Citar **no mínimo 10 referências** no texto e **apensar** (append) suas entradas **deduplicadas** em:
- `BIB = docs/2-pesquisa-cientifica/08-artigos-referencia/referencias.bib`

---

## 🔐 PAC (Política de Ação e Controle)
- **Web ON (somente leitura, 2023–2025)**: priorizar **SciELO**, **DOAJ**, **PubMed Central**, **ERIC** e repositórios institucionais. Usar **Google Scholar apenas para descoberta** e recuperar metadados no **fonte original**.
- **Sem shell**; apenas I/O de arquivos.
- **UTF‑8**; **escrita atômica** (`*.tmp` → rename).
- **Idempotente**: criar diretórios/arquivos se faltarem; abrir `BIB` em **append**; **não** sobrescrever entradas existentes.
- **Deduplicação** no `.bib`: comparar por `doi` > `url` > `(title+year)`; pular duplicatas (`Skipped dup: KEY`); se a nova versão estiver mais completa, **mesclar sem apagar** campos válidos existentes.
- **Logs**: `Read INTRO: …`, `Read PC: …`, `Created file: …`, `Appended refs: <N>`, `Skipped dup: <KEY>`.

---

## ✅ Conformidade (ABNT + abnTeX2)
- **Citações**: **NBR 10520:2023**, sistema **autor‑data**; direta curta (≤3 linhas) **com página**; direta longa em bloco recuado; indireta autor‑data. *(compilação com abnTeX2)*
- **Referências**: **NBR 6023/2018** (elementos obrigatórios; **DOI/URL** e **`urldate`** quando aplicável).
- **Apresentação/numeração**: **NBR 14724/2024** (seções e subseções numeradas; **Introdução** precede **Métodos**, **Resultados**, **Discussão** – IMRaD). **NBR 6022/2018** define elementos de artigos.
- **LaTeX/abnTeX2**: usar `\cite{}` e `\citeonline{}`; chaves ASCII; projeto com estilo `abntex2-alf`.

---

## 🔎 Insumos obrigatórios
1) **Ler `INTRO`** (se existir) para manter **coesão e evitar redundância**; extrair tópicos já abordados.  
2) **Ler `PC1`**; se ausente, **tentar `PC2`**; capturar **a frase exata** da pergunta central para **referência cruzada** (não reescrever a pergunta na _Justificativa_).  
3) Mapear **lacunas** e **motivações** que **ainda não foram** explicadas na `INTRO` para desenvolver na _Justificativa_.

---

## 🧱 Saída LaTeX (gerar conteúdo final; **sem preâmbulo**)
Gravar **integralmente** em `OUT_TEX` o corpo abaixo, preenchendo com **400–700 palavras** (PT‑BR) e **≥10 citações** distribuídas ao longo do texto:

```latex
\subsection{Justificativa}\label{sec:justificativa}
% Desenvolver as razões científicas, educacionais e éticas do estudo, a partir da literatura recente (2023--2025).
% Estrutura sugerida (parágrafos):
% 1) Contextualize a relevância da investigação sobre IA/LLMs na escrita acadêmica (benefícios e riscos).
% 2) Explique a pertinência para estudantes de graduação (competências de escrita, feedback, desigualdades de acesso).
% 3) Aborde integridade acadêmica (plágio, autoria, transparência no uso de IA) e políticas institucionais.
% 4) Evidencie a lacuna específica que o estudo enfrenta (coerente com a INTRO e com a pergunta central lida do arquivo).
% 5) Impactos esperados (científicos e práticos) e originalidade.
%
% Regras de citação (abnTeX2):
% - Indireta: \cite{KEY}; menção no texto: \citeonline{KEY}.
% - Direta curta (≤3 linhas) com página: \cite[p.~xx]{KEY}; direta longa: bloco recuado + \cite[p.~xx]{KEY}.
%
% Observação: NÃO reescrever a pergunta central aqui; apenas fazer referência a ela.
```

> **Importante**: manter **coerência** com `INTRO` e **alinhamento** com a pergunta central; não repetir texto já presente na `INTRO`.

---

## 📚 Requisitos de busca e seleção (mínimo **10** referências)
- **≥6** estudos empíricos/revisões sobre IA/LLMs/ChatGPT **na escrita acadêmica** (qualidade, revisão, feedback, avaliação de textos).
- **≥2** sobre **integridade/ética** (plágio, autoria, transparência).
- **≥2** do **contexto brasileiro/ibero** (português/espanhol).
Para cada item, registrar: `author`, `year`, `title`, `journal|booktitle`, `volume`, `number`, `pages`, **`doi`**, **`url`**, **`urldate`** (AAAA‑MM‑DD), `language`.

---

## 📚 BibTeX (append)
- Abrir/criar `BIB` em **append**.
- Inserir **1 entrada para cada chave citada** (`@article`, `@inproceedings`, `@book`, `@misc` quando indispensável).
- **Chave**: `sobrenomeYYYYpalavra` (ASCII, sem acentos/espaços).
- **Deduplicação**: pular duplicatas por `doi`/`url`/`title+year`; se a nova tiver mais metadados, **mesclar** sem apagar campos existentes.

---

## 🧪 QA e Relato
1) Garantir correspondência 1:1 entre `\cite{}` no TEX e entradas no `.bib`.  
2) **≥10** referências distintas (`Appended refs: N` com N ≥ 10; reportar `Skipped dup: …`).  
3) Verificar presença de **`doi`** ou **`url` + `urldate`** em cada entrada online.  
4) Publicar caminhos absolutos dos arquivos gerados/atualizados.
