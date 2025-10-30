# System Spec — Pesquisa Científica COMPLETA (v3, com MANIFEST)

## PAC (Política de Ação e Controle)
- Sem shell. Apenas criar diretórios/arquivos.
- Idempotente: não sobrescreva o que já existir.
- Escrita atômica: escreva em `*.tmp` e renomeie.
- Determinístico: crie **na ordem do MANIFEST** (dirs → files).
- Logs: `Created dir:`, `Exists dir:`, `Created file:`, `Exists file:`.
- Base: `docs/99-prompts/2-pesquisa-cientifica/` (BASE.DIR).

---

## MANIFEST (ORDEM EXATA DE CRIAÇÃO)
> **Interpretação:** cada linha inicia por `[D]` (diretório) ou `[F]` (arquivo).  
> Para `[F]`, tudo após o segundo `|` é o **conteúdo** do arquivo (UTF‑8).

```
[D]|00-orientacoes/
[D]|01-problema/
[D]|02-revisao-literatura/
[D]|02-revisao-literatura/fichamentos/
[D]|03-metodologia/
[D]|04-coleta-dados/
[D]|04-coleta-dados/dados-brutos/
[D]|04-coleta-dados/questionarios/
[D]|04-coleta-dados/entrevistas/
[D]|05-analise-resultados/
[D]|05-analise-resultados/scripts/
[D]|05-analise-resultados/tabelas/
[D]|05-analise-resultados/figuras/
[D]|06-relatorio-final/
[D]|06-relatorio-final/slides-apresentacao/
[D]|07-prompts-pesquisa/
[D]|08-artigos-referencia/
[D]|08-artigos-referencia/artigos-pdf/

[F]|00-orientacoes/README.md|# Projeto de Pesquisa: IA na escrita acadêmica
Este repositório demonstra todas as etapas — do problema ao relatório —
organizadas para alunos iniciantes. Use as pastas como guia de trabalho.

## Estrutura (visão geral)
1) Problema · 2) Revisão · 3) Metodologia · 4) Coleta · 5) Análise · 6) Relatório

[F]|00-orientacoes/cronograma.md|# Cronograma da Pesquisa
| Etapa                  | Período  | Responsável |
|------------------------|----------|-------------|
| Formulação do problema | Semana 1 | Equipe      |
| Revisão de literatura  | Sem 2-3  | Pesquisador |
| Coleta de dados        | Semana 4 | Equipe      |
| Análise e relatório    | Semana 5 | Orientador  |

[F]|00-orientacoes/equipe.md|# Equipe de Pesquisa
- Orientador: Prof. Dr. Thales Levi Azevedo Valente
- Discentes: <nomes>
- Apoio técnico: Assistente de IA

[F]|00-orientacoes/glossario.md|# Glossário
- **IA**: Inteligência Artificial.
- **Revisão sistemática**: método estruturado para localizar e sintetizar estudos.

[F]|01-problema/pergunta-central.md|# Pergunta Central
Como a inteligência artificial influencia o processo de escrita acadêmica de estudantes universitários?

[F]|01-problema/justificativa.md|# Justificativa
O uso crescente de IA na educação demanda evidências sobre impactos na qualidade, ética e autonomia da escrita científica.

[F]|01-problema/objetivos.md|# Objetivos
**Geral:** Investigar como a IA afeta a escrita acadêmica.
**Específicos:**
- Identificar percepções de estudantes;
- Avaliar mudanças de estilo e fluidez;
- Propor diretrizes de uso responsável.

[F]|02-revisao-literatura/referencias-principais.md|# Referências principais (lista inicial)
- Freire, P. (1987). *Pedagogia do Oprimido*.
- Lévy, P. (1999). *Cibercultura*.
- Carvalho, D. (2020). Escrita acadêmica mediada por tecnologias.

[F]|02-revisao-literatura/matriz-sintese.md|# Matriz de síntese (exemplo)
| Autor   | Ano | Tema‑chave             | Contribuição                    |
|---------|-----|------------------------|---------------------------------|
| Freire  | 1987| Educação crítica       | Autonomia e reflexão            |
| Lévy    | 1999| Inteligência coletiva  | Mediação tecnológica            |
| Carvalho| 2020| Escrita com apoio de IA| Benefícios e desafios éticos    |

[F]|03-metodologia/tipo-pesquisa.md|# Tipo de Pesquisa
Qualitativa, exploratória e descritiva; coleta por questionário e entrevistas.

[F]|03-metodologia/instrumentos-coleta.md|# Instrumentos de Coleta
- Questionário semiestruturado (Google Forms ou similar);
- Roteiro de entrevista (30–45 min).

[F]|03-metodologia/plano-analise.md|# Plano de Análise
Análise de conteúdo temática; codificação inicial → eixos → categorias.

[F]|04-coleta-dados/README.md|# Coleta de Dados
Use as subpastas **dados-brutos/**, **questionarios/** e **entrevistas/**.
Armazene apenas cópias anonimizadas.

[F]|05-analise-resultados/discussoes.md|# Discussão (rascunho)
Tópicos iniciais: utilidade percebida, mudanças de estilo, dilemas éticos.

[F]|06-relatorio-final/artigo.md|# Estrutura do Artigo
## 1 Introdução
## 2 Metodologia
## 3 Resultados e Discussão
## 4 Conclusões

[F]|06-relatorio-final/resumo-expandido.md|# Resumo Expandido
Objetivo, método, principais achados, limitações e implicações.

[F]|06-relatorio-final/checklist-final.md|# Checklist Final
- [ ] Problema e objetivos claros
- [ ] Revisão coerente
- [ ] Método adequado
- [ ] Dados organizados
- [ ] Resultados interpretados
- [ ] Referências padronizadas

[F]|07-prompts-pesquisa/p1-problema.md|# Prompt — Formulação do Problema
Gere 5 versões de perguntas de pesquisa sobre IA e escrita acadêmica, com variáveis, recortes e justificativas.

[F]|07-prompts-pesquisa/p2-revisao.md|# Prompt — Revisão de Literatura
Sugira descritores/strings de busca e produza 3 fichamentos-modelo (150–200 palavras).

[F]|07-prompts-pesquisa/p3-metodologia.md|# Prompt — Metodologia
Proponha desenho de estudo qualitativo, amostragem e instrumentos.

[F]|07-prompts-pesquisa/p4-analise.md|# Prompt — Análise
Dê um plano de codificação temática e exemplos de categorias com trechos ilustrativos.

[F]|07-prompts-pesquisa/p5-relatorio.md|# Prompt — Relatório
Esboce Introdução, Método e Discussão em 2–3 parágrafos cada, mantendo coesão.

[F]|08-artigos-referencia/referencias.bib|@book{freire1987, title={Pedagogia do Oprimido}, author={Freire, Paulo}, year={1987}}
```

---

## CRITÉRIOS DE SUCESSO
- Todos os itens do **MANIFEST** existem em `BASE.DIR`.
- Conteúdo dos arquivos criado quando ausente (sem sobrescrever existentes).
- Emita um sumário final com contagens de `created/exists` para dirs e files.

**Fim do system spec.**
