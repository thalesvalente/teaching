# 📘 PROMPT — **Somente** Pergunta Central em LaTeX (ABNT) + Append BibTeX
*(versão focada, com busca em bases públicas; compatível com abnTeX2)*

## 🎯 Objetivo
Gerar **apenas** a seção **Pergunta Central** em LaTeX e **anexar** (append) as referências citadas:
- TEX: `docs/2-pesquisa-cientifica/01-problema/pergunta-central.tex`
- BibTeX (append): `docs/referencias.bib`

O texto deve ter **120–220 palavras** (PT‑BR), seguir **ABNT (autor‑data)** e ser **compilável** com **abnTeX2** (\cite/\citeonline).

---

## 🔐 PAC (Política de Ação e Controle)
- **Web ON (somente leitura)** para localizar **2–3 fontes** 2023–2025.
- **Bases públicas** prioritárias: SciELO, DOAJ, PubMed Central, ERIC, repositórios institucionais (usar Google Scholar só para descoberta e retornar à fonte).
- **Sem shell**; apenas I/O de arquivos.
- **Idempotente**: criar diretórios/arquivos se faltarem; **não sobrescrever** `docs/referencias.bib` (abrir em **append**); **deduplicar** por `doi`/`url`/`title+year`.
- **UTF‑8**; **escrita atômica**: gravar como `*.tmp` e renomear.
- **Logs**: `Created file: …`, `Appended refs: <N>`, `Skipped dup: <KEY>`.

---

## ✅ Conformidade (ABNT + abnTeX2)
- **Citações**: **NBR 10520:2023** (autor‑data; direta curta com **página**; direta longa em bloco recuado; indireta autor‑data).
- **Referências**: **NBR 6023:2018** (elementos, DOI/URL, **data de acesso**).
- **Estrutura/numeração**: **NBR 14724:2024** (seções numeradas).
- **LaTeX/abnTeX2**: usar `\cite{}`/`\citeonline{}` e chaves únicas sem acento; texto compatível com o pacote **abnTeX2**.

> Referências técnicas das normas e do abnTeX2 estão amplamente documentadas online (CTAN e páginas de bibliotecas universitárias).

---

## 🔎 Busca mínima (2023–2025)
Localize **2–3 fontes** que **contextualizem a relevância** da pergunta (IA/LLMs/ChatGPT **na escrita acadêmica** ou **integridade**). Preferir artigos com **DOI** e **acesso aberto** (SciELO/DOAJ). Registrar: autores; ano; título; periódico/venue; vol/nº/pág.; **DOI**; **URL**; `urldate` (AAAA‑MM‑DD); `language`.

---

## 🧱 Saída TEX (gravar exatamente este esqueleto + conteúdo)
Gravar (ou substituir integralmente) `docs/2-pesquisa-cientifica/pergunta-central.tex` com o corpo abaixo (sem preâmbulo). Preencher com **120–220 palavras** e **2–3 citações** (\cite/\citeonline), PT‑BR:

```latex
\section{Pergunta Central}\label{sec:pergunta-central}
\noindent\textbf{Questão de pesquisa:} Como a inteligência artificial influencia a escrita acadêmica de estudantes universitários?

% Contextualize em 1--2 parágrafos curtos a relevância da questão, citando 2--3 trabalhos recentes
% (2023--2025) sobre IA/LLMs/ChatGPT na produção ou avaliação de textos acadêmicos,
% e/ou sobre integridade acadêmica no uso de IA.
% Ex.: \cite{KEYA}; \citeonline{KEYB}; citação direta curta com página: \cite[p.~xx]{KEYC}.
```

**Regras LaTeX (abnTeX2)**  
- Indireta: `\cite{KEY}`; menção no texto: `\citeonline{KEY}`.  
- Direta curta com página: `\cite[p.~xx]{KEY}`; direta longa: bloco recuado + `\cite[p.~xx]{KEY}`.

---

## 📚 BibTeX (append, sem sobrescrever)
- Abrir/criar `docs/referencias.bib` **em append**.
- Para **cada citação** no TEX, **inserir** entrada BibTeX válida (`@article`, `@inproceedings`, `@book`, `@misc` quando necessário).
- **Chave**: `sobrenomeYYYYpalavra` (ASCII, sem espaços/acentos); garantir unicidade.
- **Campos mínimos**: `author`, `title`, `year`, `doi|url`, `urldate`, `language`; e quando aplicável `journal|booktitle`, `volume`, `number`, `pages`, `publisher`.
- **Deduplicação**: antes de anexar, **ler** `docs/referencias.bib`; se houver mesmo `doi` (ou `url` ou `title+year`), **não** duplicar (log `Skipped dup: KEY`).

---

## 🧪 QA e Relato
1) Verificar correspondência 1:1 entre `\cite{}` usados no TEX e entradas no `.bib`.  
2) Garantir `doi` ou `url` + `urldate` em entradas web.  
3) Imprimir resumo: `Appended refs: <N>`, `Skipped dup: <K1,K2,...>` e caminhos dos arquivos gerados/atualizados.

---

## 📌 Observações finais
- Texto curto e direto, **somente** a Pergunta Central + contextualização.  
- **Justificativa** e **Objetivos** serão produzidos em prompts separados.
