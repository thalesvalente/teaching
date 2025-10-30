# PROMPT — **Objetivos (Geral e Específicos)** em LaTeX a partir da **Introdução** + **Pergunta Central**
# ABNT (NBR 6022/2018; NBR 14724/2024; NBR 10520/2023) · compatível com **abnTeX2** · IMRaD/ICMJE
#
# Finalidade: gerar apenas **Objetivo Geral** e **Objetivos Específicos** como subseção da Introdução.

## 🎯 Objetivo do runner
Criar `docs/2-pesquisa-cientifica/01-problema/objetivos.tex` (LaTeX, sem preâmbulo) contendo:
- `\subsection{Objetivos}`
  - `\subsubsection{Objetivo Geral}` — **1 frase** derivada diretamente da **pergunta central** (sem reescrever o sentido).
  - `\subsubsection{Objetivos Específicos}` — **4 a 7 itens** numerados (`enumerate`), claros e verificáveis.

O texto deve **alinhar-se** à **Introdução** e à **Pergunta Central** já existentes. Incluir **3–5 referências metodológicas** (autor‑data) que fundamentem a formulação de objetivos (ex.: normalização ABNT, guias universitários, manuais de metodologia). **Apensar** (append) as entradas dessas referências no `.bib` (deduplicação).

---

## 🔐 PAC (Política de Ação e Controle)
- **Web ON (somente leitura)** para obter 3–5 referências metodológicas (ABNT, guias universitários, manuais). Use **SciELO/portais universitários/CTAN/ICMJE** como fonte. Google Scholar **apenas para descoberta** e volte ao **fonte original**.
- **Sem shell**; apenas I/O de arquivos.
- **UTF‑8**; **escrita atômica** (`*.tmp` → rename).
- **Idempotência**: criar diretórios/arquivos ausentes; não sobrescrever `.bib` (abrir em **append**).
- **Deduplicação** no `.bib`: por `doi` > `url` > `title+year`. Logar `Skipped dup: KEY`.
- **Logs**: `Read INTRO: …`, `Read PC: …`, `Created file: …`, `Appended refs: N`, `Skipped dup: …`.

---

## 📁 Caminhos
- `INTRO = docs/2-pesquisa-cientifica/01-problema/introducao.tex`
- `PC1   = docs/2-pesquisa-cientifica/01-problema/pergunta-central.tex`
- `PC2   = docs/2-pesquisa-cientifica/01-problema/perguna-central.tex`  # fallback caso exista erro de digitação
- `OUT_TEX = docs/2-pesquisa-cientifica/01-problema/objetivos.tex`
- `BIB = docs/2-pesquisa-cientifica/08-artigos-referencia/referencias.bib`  (criar se não existir; **append**)

**Leituras obrigatórias**
1) Ler `INTRO` (se existir) para garantir **coesão** e evitar contradições.  
2) Ler `PC1` ou `PC2` (o que existir) e **extrair a frase exata** da pergunta central. O **Objetivo Geral** deve refletir essa pergunta **sem alterar seu escopo**.

---

## ✅ Normas e coerência (ABNT + abnTeX2 + IMRaD)
- **ABNT NBR 6022** (artigos): elementos textuais em **Introdução → Desenvolvimento → Conclusão**; objetivos podem constar na **Introdução**.  
- **ABNT NBR 14724** (2024): uso de **seções/subseções numeradas**.  
- **ABNT NBR 10520**: citações **autor‑data** (usar `\cite{}`/`\citeonline{}` com abnTeX2).  
- **IMRaD (ICMJE)**: objetivos ao final da Introdução (sem repetir métodos/resultados).

---

## 🧱 Saída LaTeX (gerar conteúdo final; **sem preâmbulo**)
Gravar **integralmente** em `OUT_TEX` o seguinte esqueleto, preenchendo com conteúdo (PT‑BR, conciso e objetivo):

```latex
\subsection{Objetivos}\label{sec:objetivos}

\subsubsection{Objetivo Geral}
% 1 frase precisa, derivada da Pergunta Central lida do arquivo.
% Ex.: "Investigar ..." | "Analisar ..." | "Avaliar ..."

\subsubsection{Objetivos Específicos}
\begin{enumerate}
  \item % Identificar ...
  \item % Descrever ...
  \item % Analisar/Comparar ...
  \item % Avaliar/Medir ...
  \item % Explorar/Investigar ...
  % (adicione até 7 no total; cada item deve ser verificável no método/na análise)
\end{enumerate}

% Observações metodológicas (com 3–5 citações autor‑data que fundamentem a formulação de objetivos):
% - Definir verbos de ação e foco mensurável; evitar vagueza.
% - Garantir cobertura do escopo da Pergunta Central sem extrapolar.
% - Manter rastreabilidade: cada objetivo específico mapeia para dados/análises na seção de Métodos.
% Ex.: \cite{KEY_ABNT6022,KEY_UFV2025,KEY_PUCMINAS2025}
```

**Estilo e qualidade**
- **Clareza** e **verificabilidade**: objetivos específicos devem resultar em evidência observável (dados/indicadores ou categorias analíticas).  
- **Rastreabilidade**: mencionar, em comentário LaTeX, qual seção de **Métodos** mede cada objetivo (facilita auditoria).  
- **Consistência**: não criar objetivos que não possam ser respondidos pelos dados previstos na Introdução/Metodologia.

---

## 📚 BibTeX (append, 3–5 entradas)
- Inserir no `BIB` **apenas** as 3–5 referências **metodológicas** citadas (normas ABNT, guias universitários, manuais).
- Tipos: `@manual`, `@misc`, `@book` ou `@article` (conforme o caso).
- **Chave**: `sobrenomeYYYYpalavra` (ASCII). Campos mínimos: `author`, `title`, `year`, `url|doi`, `urldate`, `language` (+ `institution|publisher` quando cabível).
- **Deduplicação** antes do append (ver PAC).

---

## 🧪 QA e Relato
1) `Objetivo Geral`: 1 frase, alinhada **1:1** com a Pergunta Central.  
2) `Objetivos Específicos`: **4–7** itens verificáveis; sem redundância.  
3) **3–5** referências metodológicas citadas e apensadas no `.bib` (sem duplicar).  
4) Logs completos + caminhos absolutos dos arquivos gerados/atualizados.
