# System Spec — Estrutura Completa de Pesquisa Científica **STRICT** (v2.1)

## Propósito
Criar **exatamente** a árvore abaixo dentro de `docs/99-prompts/2-pesquisa-cientifica/`,
incluindo **todas** as pastas e **todos** os arquivos `.md` listados (e `referencias.bib`),
com conteúdo inicial. **Nada é opcional.**

## PAC (Política de Ação e Controle)
- **Sem shell**; apenas operações de arquivo/pasta.
- **Idempotente**: não sobrescreva se já existir (apenas verifique).
- **Escrita atômica**: grave em `*.tmp` e renomeie.
- **Ordem fixa**: 1) criar diretórios; 2) criar arquivos; 3) imprimir verificação.
- **Logs obrigatórios** por item: `Created dir:`, `Exists dir:`, `Created file:`, `Exists file:`.

## Variáveis canônicas
- **BASE.DIR** = `docs/99-prompts/2-pesquisa-cientifica/` (sempre com `/` no final).

---

## Árvore-alvo (normativa)
```
docs/
└─ 99-prompts/
   └─ 2-pesquisa-cientifica/
      ├─ 00-orientacoes/
      │  ├─ README.md
      │  ├─ cronograma.md
      │  ├─ equipe.md
      │  └─ glossario.md
      ├─ 01-problema/
      │  ├─ pergunta-central.md
      │  ├─ justificativa.md
      │  └─ objetivos.md
      ├─ 02-revisao-literatura/
      │  ├─ referencias-principais.md
      │  ├─ fichamentos/
      │  └─ matriz-sintese.md
      ├─ 03-metodologia/
      │  ├─ tipo-pesquisa.md
      │  ├─ instrumentos-coleta.md
      │  └─ plano-analise.md
      ├─ 04-coleta-dados/
      │  ├─ dados-brutos/
      │  ├─ questionarios/
      │  └─ entrevistas/
      ├─ 05-analise-resultados/
      │  ├─ scripts/
      │  ├─ tabelas/
      │  ├─ figuras/
      │  └─ discussoes.md
      ├─ 06-relatorio-final/
      │  ├─ artigo.md
      │  ├─ resumo-expandido.md
      │  ├─ slides-apresentacao/
      │  └─ checklist-final.md
      ├─ 07-prompts-pesquisa/
      │  ├─ p1-problema.md
      │  ├─ p2-revisao.md
      │  ├─ p3-metodologia.md
      │  ├─ p4-analise.md
      │  └─ p5-relatorio.md
      └─ 08-artigos-referencia/
         ├─ artigos-pdf/
         └─ referencias.bib
```

---

## Manifesto **exato** (listas canônicas para execução)

### Dirs (criar na ordem)
```yaml
dirs:
  - 00-orientacoes
  - 01-problema
  - 02-revisao-literatura
  - 02-revisao-literatura/fichamentos
  - 03-metodologia
  - 04-coleta-dados
  - 04-coleta-dados/dados-brutos
  - 04-coleta-dados/questionarios
  - 04-coleta-dados/entrevistas
  - 05-analise-resultados
  - 05-analise-resultados/scripts
  - 05-analise-resultados/tabelas
  - 05-analise-resultados/figuras
  - 06-relatorio-final
  - 06-relatorio-final/slides-apresentacao
  - 07-prompts-pesquisa
  - 08-artigos-referencia
  - 08-artigos-referencia/artigos-pdf
```

### Files (criar se não existirem; conteúdo abaixo)
```yaml
files:
  - 00-orientacoes/README.md
  - 00-orientacoes/cronograma.md
  - 00-orientacoes/equipe.md
  - 00-orientacoes/glossario.md
  - 01-problema/pergunta-central.md
  - 01-problema/justificativa.md
  - 01-problema/objetivos.md
  - 02-revisao-literatura/referencias-principais.md
  - 02-revisao-literatura/matriz-sintese.md
  - 03-metodologia/tipo-pesquisa.md
  - 03-metodologia/instrumentos-coleta.md
  - 03-metodologia/plano-analise.md
  - 04-coleta-dados/README.md
  - 05-analise-resultados/discussoes.md
  - 06-relatorio-final/artigo.md
  - 06-relatorio-final/resumo-expandido.md
  - 06-relatorio-final/checklist-final.md
  - 07-prompts-pesquisa/p1-problema.md
  - 07-prompts-pesquisa/p2-revisao.md
  - 07-prompts-pesquisa/p3-metodologia.md
  - 07-prompts-pesquisa/p4-analise.md
  - 07-prompts-pesquisa/p5-relatorio.md
  - 08-artigos-referencia/referencias.bib
```

---

## Conteúdo inicial por arquivo (curto e didático)

**00-orientacoes/README.md**
```markdown
# Projeto de Pesquisa: IA na escrita acadêmica
Este repositório demonstra todas as etapas de uma pesquisa — da formulação
do problema ao relatório final — com organização clara para alunos iniciantes.
```

**00-orientacoes/cronograma.md**
```markdown
# Cronograma da Pesquisa
| Etapa | Período | Responsável |
|------|---------|-------------|
| Problema | Sem 1 | Equipe |
| Revisão | Sem 2-3 | Pesquisador |
| Coleta | Sem 4 | Equipe |
| Análise/Relatório | Sem 5 | Orientador |
```

**00-orientacoes/equipe.md**
```markdown
# Equipe
- Orientador: Prof. Dr. Thales Levi Azevedo Valente
- Discentes: <nomes>
- Apoio técnico: Assistente de IA
```

**00-orientacoes/glossario.md**
```markdown
# Glossário
- **IA**: Inteligência Artificial.
- **Revisão sistemática**: método estruturado de síntese de estudos.
```

**01-problema/pergunta-central.md**
```markdown
# Pergunta Central
Como a IA influencia a escrita acadêmica de estudantes universitários?
```

**01-problema/justificativa.md**
```markdown
# Justificativa
Adoção crescente de IA na educação exige evidências sobre impacto, ética e autonomia.
```

**01-problema/objetivos.md**
```markdown
# Objetivos
**Geral:** Investigar efeitos da IA na escrita acadêmica.
**Específicos:** percepções, mudanças de estilo, diretrizes de uso responsável.
```

**02-revisao-literatura/referencias-principais.md**
```markdown
# Referências principais (inicial)
Freire (1987); Lévy (1999); Carvalho (2020).
```

**02-revisao-literatura/matriz-sintese.md**
```markdown
# Matriz de síntese (rascunho)
| Autor | Ano | Contribuição |
|-------|-----|--------------|
| Freire | 1987 | Autonomia |
| Lévy | 1999 | Mediação |
| Carvalho | 2020 | IA na escrita |
```

**03-metodologia/tipo-pesquisa.md**
```markdown
# Tipo de Pesquisa
Qualitativa, exploratória-descritiva; questionário + entrevistas.
```

**03-metodologia/instrumentos-coleta.md**
```markdown
# Instrumentos de Coleta
Questionário semiestruturado; roteiro de entrevista (30–45 min).
```

**03-metodologia/plano-analise.md**
```markdown
# Plano de Análise
Codificação temática → eixos → categorias; triangulação de fontes.
```

**04-coleta-dados/README.md**
```markdown
# Coleta de Dados
Subpastas: dados-brutos/, questionarios/, entrevistas/. Armazene cópias anonimizadas.
```

**05-analise-resultados/discussoes.md**
```markdown
# Discussões (rascunho)
Utilidade percebida, mudanças de estilo, dilemas éticos.
```

**06-relatorio-final/artigo.md**
```markdown
# Estrutura do Artigo
## 1 Introdução
## 2 Metodologia
## 3 Resultados e Discussão
## 4 Conclusões
```

**06-relatorio-final/resumo-expandido.md**
```markdown
# Resumo Expandido
Objetivo, método, principais achados, limitações e implicações.
```

**06-relatorio-final/checklist-final.md**
```markdown
# Checklist Final
- [ ] Problema/objetivos claros
- [ ] Revisão coerente
- [ ] Método adequado
- [ ] Dados organizados
- [ ] Resultados interpretados
- [ ] Referências padronizadas
```

**07-prompts-pesquisa/p1-problema.md**
```markdown
# Prompt — Problema
Gere 5 perguntas de pesquisa (variáveis, recortes, justificativas).
```

**07-prompts-pesquisa/p2-revisao.md**
```markdown
# Prompt — Revisão
Sugira descritores e 3 fichamentos-modelo (150–200 palavras).
```

**07-prompts-pesquisa/p3-metodologia.md**
```markdown
# Prompt — Metodologia
Proponha desenho qualitativo, amostragem e instrumentos.
```

**07-prompts-pesquisa/p4-analise.md**
```markdown
# Prompt — Análise
Plano de codificação temática e exemplos de categorias.
```

**07-prompts-pesquisa/p5-relatorio.md**
```markdown
# Prompt — Relatório
Esboce Introdução, Método e Discussão em 2–3 parágrafos cada.
```

**08-artigos-referencia/referencias.bib**
```bibtex
@book{freire1987, title={Pedagogia do Oprimido}, author={Freire, Paulo}, year={1987}}
```

---

## Verificação e saída
- Após criar tudo, imprima **lista de pendências** (se algo não foi criado) ou `OK: árvore completa`.
- Resumo numérico: `dirs_created`, `dirs_existing`, `files_created`, `files_existing`.

**Fim do system spec.**
