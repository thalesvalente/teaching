# System Spec — Estrutura Completa de Pesquisa Científica (v2)

## PAC (Política de Ação e Controle)
- **Sem shell.** Apenas operações de arquivo/folder.
- **Rede read-only.** Nada externo é baixado.
- **Idempotente.** Se o caminho já existir, **pule** (não sobrescreva).
- **Escrita atômica.** Crie como `*.tmp` e renomeie para o destino.
- **Determinístico.** Ordem de criação: diretórios → arquivos.
- **Logs.** Emita mensagens: `Created dir:`, `Exists dir:`, `Created file:`, `Exists file:`.

## Variáveis canônicas
- **BASE.DIR** = `docs/99-prompts/2-pesquisa-cientifica/` (sempre com barra final).

---

## 1) Diretórios a criar (em ordem)
Crie **todos** abaixo, respeitando os níveis:

1. `00-orientacoes/`
2. `01-problema/`
3. `02-revisao-literatura/`
4. `02-revisao-literatura/fichamentos/`
5. `03-metodologia/`
6. `04-coleta-dados/`
7. `04-coleta-dados/dados-brutos/`
8. `04-coleta-dados/questionarios/`
9. `04-coleta-dados/entrevistas/`
10. `05-analise-resultados/`
11. `05-analise-resultados/scripts/`
12. `05-analise-resultados/tabelas/`
13. `05-analise-resultados/figuras/`
14. `06-relatorio-final/`
15. `06-relatorio-final/slides-apresentacao/`
16. `07-prompts-pesquisa/`
17. `08-artigos-referencia/`
18. `08-artigos-referencia/artigos-pdf/`

> Para cada item: se existir → log `Exists dir: <path>`; se não → criar e log `Created dir: <path>`.

---

## 2) Arquivos a criar + conteúdo inicial
Para **cada arquivo** abaixo:  
- se **não existir**, crie via escrita atômica (`.tmp` → rename) com o **conteúdo indicado** e log `Created file: <path>`;  
- se **existir**, **não sobrescreva** e log `Exists file: <path>`.

### 2.1 Orientações
**`00-orientacoes/README.md`**
```markdown
# Projeto de Pesquisa: IA na escrita acadêmica
Este repositório demonstra todas as etapas de uma pesquisa — da formulação
do problema ao relatório final — com organização clara para alunos iniciantes.

## Estrutura (visão geral)
1) Problema · 2) Revisão · 3) Metodologia · 4) Coleta · 5) Análise · 6) Relatório
```

**`00-orientacoes/cronograma.md`**
```markdown
# Cronograma da Pesquisa
| Etapa                  | Período  | Responsável |
|------------------------|----------|-------------|
| Formulação do problema | Semana 1 | Equipe      |
| Revisão de literatura  | Sem 2-3  | Pesquisador |
| Coleta de dados        | Semana 4 | Equipe      |
| Análise e relatório    | Semana 5 | Orientador  |
```

**`00-orientacoes/equipe.md`**
```markdown
# Equipe de Pesquisa
- Orientador: Prof. Dr. Thales Levi Azevedo Valente
- Discentes: <nomes>
- Apoio técnico: Assistente de IA
```

**`00-orientacoes/glossario.md`**
```markdown
# Glossário
- **IA**: Inteligência Artificial.
- **Revisão sistemática**: método estruturado para localizar e sintetizar estudos.
```

### 2.2 Problema
**`01-problema/pergunta-central.md`**
```markdown
# Pergunta Central
Como a inteligência artificial influencia o processo de escrita acadêmica
de estudantes universitários?
```

**`01-problema/justificativa.md`**
```markdown
# Justificativa
O uso crescente de IA na educação demanda evidências sobre impactos na
qualidade, ética e autonomia da escrita científica.
```

**`01-problema/objetivos.md`**
```markdown
# Objetivos
**Geral:** Investigar como a IA afeta a escrita acadêmica.
**Específicos:**
- Identificar percepções de estudantes;
- Avaliar mudanças de estilo e fluidez;
- Propor diretrizes de uso responsável.
```

### 2.3 Revisão de literatura
**`02-revisao-literatura/referencias-principais.md`**
```markdown
# Referências principais (lista inicial)
- Freire, P. (1987). *Pedagogia do Oprimido*.
- Lévy, P. (1999). *Cibercultura*.
- Carvalho, D. (2020). Escrita acadêmica mediada por tecnologias.
```

**`02-revisao-literatura/matriz-sintese.md`**
```markdown
# Matriz de síntese (exemplo)
| Autor   | Ano | Tema-chave             | Contribuição                    |
|---------|-----|------------------------|---------------------------------|
| Freire  | 1987| Educação crítica       | Autonomia e reflexão            |
| Lévy    | 1999| Inteligência coletiva  | Mediação tecnológica            |
| Carvalho| 2020| Escrita com apoio de IA| Benefícios e desafios éticos    |
```

### 2.4 Metodologia
**`03-metodologia/tipo-pesquisa.md`**
```markdown
# Tipo de Pesquisa
Qualitativa, exploratória e descritiva; coleta por questionário e entrevistas.
```

**`03-metodologia/instrumentos-coleta.md`**
```markdown
# Instrumentos de Coleta
- Questionário semiestruturado (Google Forms ou similar);
- Roteiro de entrevista (30–45 min).
```

**`03-metodologia/plano-analise.md`**
```markdown
# Plano de Análise
Análise de conteúdo temática; codificação inicial → eixos → categorias.
```

### 2.5 Coleta de dados
**`04-coleta-dados/README.md`**
```markdown
# Coleta de Dados
Use as subpastas: **dados-brutos/**, **questionarios/** e **entrevistas/**.
Armazene apenas cópias anonimizadas.
```

### 2.6 Análise e resultados
**`05-analise-resultados/discussoes.md`**
```markdown
# Discussão (rascunho)
Tópicos iniciais: utilidade percebida, mudanças de estilo, dilemas éticos.
```

### 2.7 Relatório final
**`06-relatorio-final/artigo.md`**
```markdown
# Estrutura do Artigo
## 1 Introdução
## 2 Metodologia
## 3 Resultados e Discussão
## 4 Conclusões
```

**`06-relatorio-final/resumo-expandido.md`**
```markdown
# Resumo Expandido
Objetivo, método, principais achados, limitações e implicações.
```

**`06-relatorio-final/checklist-final.md`**
```markdown
# Checklist Final
- [ ] Problema e objetivos claros
- [ ] Revisão coerente
- [ ] Método adequado
- [ ] Dados organizados
- [ ] Resultados interpretados
- [ ] Referências padronizadas
```

### 2.8 Prompts de apoio
**`07-prompts-pesquisa/p1-problema.md`**
```markdown
# Prompt — Formulação do Problema
Gere 5 versões de perguntas de pesquisa sobre IA e escrita acadêmica, com
variáveis, recortes e justificativas.
```

**`07-prompts-pesquisa/p2-revisao.md`**
```markdown
# Prompt — Revisão de Literatura
Sugira descritores/strings de busca e produza 3 fichamentos-modelo (150–200 palavras).
```

**`07-prompts-pesquisa/p3-metodologia.md`**
```markdown
# Prompt — Metodologia
Proponha desenho de estudo qualitativo, amostragem e instrumentos.
```

**`07-prompts-pesquisa/p4-analise.md`**
```markdown
# Prompt — Análise
Dê um plano de codificação temática e exemplos de categorias com trechos ilustrativos.
```

**`07-prompts-pesquisa/p5-relatorio.md`**
```markdown
# Prompt — Relatório
Esboce Introdução, Método e Discussão em 2–3 parágrafos cada, mantendo coesão.
```

### 2.9 Base de referência
**`08-artigos-referencia/referencias.bib`**
```bibtex
@book{freire1987, title={Pedagogia do Oprimido}, author={Freire, Paulo}, year={1987}}
```

---

## 3) Critérios de sucesso
- Todos os diretórios da seção **1** existem em **BASE.DIR**.
- Todos os arquivos da seção **2** existem com **conteúdo inicial**.
- Logs emitidos conforme PAC.

## 4) Saída final
- Imprima um sumário com o total de **diretórios criados/ignorados** e **arquivos criados/ignorados**.

--- 

**Fim do system spec.**
