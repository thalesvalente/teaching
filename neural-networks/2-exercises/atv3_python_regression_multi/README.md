# Trabalho Individual – Regressão Linear **Multivariada**

---

![UFMA](./ufma_logo.png)&nbsp;&nbsp;&nbsp;&nbsp;![Engenharia da Computação](./eng_comp_logo.png)

---

## Universidade Federal do Maranhão  
### Engenharia da Computação  
### Disciplina: EECP0053 – **Tópicos em Engenharia da Computação II – Fundamentos de Redes Neurais**  
**Professor:** Dr. Thales Levi Azevedo Valente  
**E-mail:** <thales.levi@ufma.br> / <thales.l.a.valente@gmail.com>  
**Semestre:** 2025.1  

---

## 🎯 Objetivos

Este trabalho individual aprofunda a regressão linear **multivariada** com ênfase em **(i)** o impacto da _normalização das features_ e **(ii)** a comparação entre **Gradiente Descendente (GD)** e **Equação Normal (NE)** para estimação dos parâmetros \( \theta \).  

Objetivos específicos:

1. **Comparar métodos de normalização**  
   - Sem normalização  
   - Normalização **z‑score** (`features_normalize_by_std`)  
   - Normalização **min‑max** (`features_normalizes_by_min_max`)
2. **Comparar métodos de otimização**  
   - Gradiente Descendente clássico  
   - Solução fechada pela Equação Normal
3. **Implementar e documentar** (ou revisar) os componentes essenciais:
   - `RegressionMultivariate/features_normalize.py`
   - `RegressionMultivariate/compute_cost_multi.py`
   - `RegressionMultivariate/gradient_descent_multi.py`
   - `RegressionMultivariate/gradient_descent_multi_with_history.py`
   - `RegressionMultivariate/normal_eqn.py`
   - `regressao-multivariada-ex.py`
4. **Redigir um relatório ABNT** contendo:
   - Descrição dos experimentos e gráficos gerados
   - Discussão crítica dos resultados
   - Explicação do efeito da escala das features sobre GD e NE
   - Conclusões sobre desempenho, velocidade e precisão de cada abordagem

---

## 📚 Tópicos de Implementação & Gráficos

| Item | Conteúdo a gerar/entregar                                                                                                     |
|------|-------------------------------------------------------------------------------------------------------------------------------|
| 1    | **Curva de convergência** de custo do GD (uma linha por variante de normalização)                                             |
| 2    | **Comparação direta** entre menor custo obtido por GD × NE                                                                    |
| 3    | **Plano de regressão 3‑D** (tamanho × quartos × preço) ajustado com θ<sub>GD</sub>, sobre pontos de treino                    |
| 4    | **Superfície** e **contorno** de \( J(\theta_1,\theta_2) \) com trajetória do GD e ponto da NE (θ normalizado)            |

---

## 🗂️ Estrutura Sugerida do Repositório

```
regressao-linear-multivariada_<SeuNome>/
│
├─ Data/
│   └─ ex1data2.txt
│
├─ RegressionMultivariate/
│   ├─ __init__.py
│   ├─ features_normalize.py
│   ├─ compute_cost_multi.py
│   ├─ gradient_descent_multi.py
│   ├─ gradient_descent_multi_with_history.py
│   └─ normal_eqn.py
│
├─ Figures/                 # gráficos (.png / .svg) produzidos pelo script
│
├─ regressao-multivariada-ex.py            # **script principal**
├─ README.md                # **este arquivo**
├─ ufma_logo.png
├─ eng_comp_logo.png
├─ requirements.txt         # dependências mínimas (numpy, matplotlib)
├─ regressao-multi.yml      # ambiente Conda (opcional)
└─ setup_env.py             # cria venv + instala libs a partir de requirements.txt
```

---

## 🚀 Como Executar

### ✅ Opção 1 — Conda (recomendado)

```bash
conda env create -f regressao-multi.yml
conda activate regressao-multi
python main_multi.py
```

### 🐍 Opção 2 — Ambiente virtual Python puro

```bash
python setup_env.py      # cria venv regressao-multi + pip install -r requirements.txt
# Ative a venv conforme a instrução exibida no terminal, depois:
python main_multi.py
```

Todos os gráficos serão salvos em `Figures/`. Renomeie-os de forma descritiva ao comparar experimentos.

---

## ✍️ Relatório (formato ABNT)

Estrutura sugerida (não obrigatória):

1. **Introdução** – problema, propósito do experimento  
2. **Metodologia** – descrição dos métodos (GD, NE) e das estratégias de normalização  
3. **Resultados** – inserção dos gráficos (com legendas)  
4. **Discussão** – interpretação dos achados, comparação de custo, tempo, robustez  
5. **Conclusões** – principais lições sobre escala das features, preferências de otimização  
6. **Referências** – cite o material de apoio utilizado  

> Dica: use subtítulos para separar GD vs NE, z‑score vs min‑max, e _sem normalização_.

---

## 💡 Boas Práticas de Commit (**Bônus**)

Bônus extras serão concedidos pelo uso consistente dos *commit types* abaixo:

| Tipo      | Descrição                                                                            |
|-----------|---------------------------------------------------------------------------------------|
| **feat**  | Nova funcionalidade ou implementação significativa                                    |
| **fix**   | Correção de erros ou bugs                                                             |
| **chore** | Manutenção geral (configuração, organização de arquivos)                             |
| **docs**  | Atualizações ou adições em documentação                                               |
| **style** | Mudanças de formatação (espaços em branco, indentação)                               |
| **refactor** | Melhorias de código sem adicionar novas funcionalidades                           |
| **test**  | Adição de testes automatizados                                                        |
| **perf**  | Melhorias de desempenho                                                               |
| **ci**    | Alterações em configuração de integração contínua                                     |
| **build** | Modificações que afetam o processo de build ou dependências                           |

---

## 📅 Submissão

- **Prazo:** **04 / 05 / 2025** (23h59 BRT)  
- Enviar **somente** o link do repositório Git no SIGAA.  
- Commits devem refletir participação individual; integrantes sem contribuições significativas serão desconsiderados.  
- Tentativas de burla via histórico de commits acarretam **nota zero** para todos os envolvidos.  
- Submissões fora do prazo ou por outros meios serão ignoradas.

---

## 📋 Critérios de Avaliação

| Critério                                                                                | Peso |
|-----------------------------------------------------------------------------------------|------|
| Implementação correta dos módulos Python                                                | 2.5  |
| Geração e qualidade dos gráficos (itens 1–4)                                            | 2.0  |
| Experimentos comparativos (GD × NE × normalizações)                                     | 1.5  |
| Análise escrita (clareza, profundidade, formatação ABNT)                                | 3.0  |
| Organização do repositório, README e uso adequado de Git                                | 1.0  |

---

**Boa sorte e bom estudo!** Qualquer dúvida, estou disponível por e‑mail ou em aula.

---

### Reconhecimentos e Direitos Autorais

```
@autor:                [Seu Nome]
@contato:              [Seu Email]
@data última versão:   28/04/2025
@versão:               2.0
@outros repositórios:  [URLs opcionais]
@Agradecimentos:       Universidade Federal do Maranhão (UFMA),
                       Prof. Dr. Thales Levi Azevedo Valente,
                       colegas de curso.
```

---

### Licença (MIT)

> Este material é resultado de um trabalho acadêmico para a disciplina *EECP0053 - TÓPICOS EM ENGENHARIA DA COMPUTAÇÃO II - FUNDAMENTOS DE REDES NEURAIS*, semestre letivo 2025.1, curso Engenharia da Computação, UFMA.

```
MIT License

Copyright (c) 20/04/2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
