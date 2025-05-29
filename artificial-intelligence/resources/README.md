# 🏗️ IFC → Neo4j: Integrando Modelos BIM em Grafos de Conhecimento

Este guia passo‑a‑passo mostra como instalar as ferramentas necessárias, carregar um modelo **`.ifc`** e visualizá‑lo como um **grafo de conhecimento** no Neo4j – perfeito para projetos de graduação que combinam **BIM**, **IA** e **banco de dados em grafo**.

---

## 📦 Pré‑requisitos

| Ferramenta | Link | Função |
|------------|------|--------|
| 🧱 **Blender** | <https://www.blender.org/download/> | Modelagem e visualização 3D |
| 🌿 **Bonsai** (add‑on para Blender) | <https://extensions.blender.org/add-ons/bonsai/> | Exportação BIM → IFC |
| 🧠 **Neo4j Desktop** | <https://neo4j.com/download/> | Banco de dados em grafo |
| ☕ **Java JDK 17** | <https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html> | Necessário para rodar o Neo4j |
| 🐍 **Python 3.10+** | — | Ambiente para executar o script de importação |

> **Bibliotecas Python obrigatórias**  
> `ifcopenshell  py2neo  rdflib  lark-parser`

---

## 🛠️ Instalação passo a passo

### 1. Blender + Bonsai

1. Baixe e instale o **Blender**.  
2. Dentro do Blender abra **Edit ▸ Preferences ▸ Add‑ons ▸ Install…** e selecione o    arquivo `bonsai.zip`.

### 2. Java JDK 17

1. Instale o **JDK 17**.  
2. Defina a variável de ambiente `JAVA_HOME` apontando para a pasta do JDK:

```bash
# Windows (exemplo)
setx JAVA_HOME "C:\Program Files\Java\jdk‑17.0.12"
```

### 3. Neo4j Desktop

1. Instale e abra o **Neo4j Desktop**.  
2. Crie um novo **DBMS local** e depois um banco chamado **`ifctest`**    (evite hífens no nome).  
3. Na primeira abertura do Browser será solicitado que troque a senha    padrão; anote‑a – você usará no script.

### 4. Ambiente Python

```bash
# Crie/ative seu ambiente (opcional)
python -m venv venv
venv\Scripts\activate               # Linux/Mac: source venv/bin/activate

# Instale as libs necessárias
pip install ifcopenshell py2neo rdflib lark-parser
```

---

## 🏢 Baixar modelo IFC de exemplo

https://raw.githubusercontent.com/buildingSMART/Sample-Test-Files/main/IFC%204.3.2.0%20(IFC4X3_ADD2)/PCERT-Sample-Scene/Building-Architecture.ifc

---

## 🐍 Executar o script `ifc.ipynb`

Edite as variáveis no início do notebook/script:

```python
IFC_FILE = r"C:\CAMINHO\Building-Architecture.ifc"
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "SUA_SENHA_AQUI"
NEO4J_DATABASE = "ifctest"
```

Depois **rode todas as células**.  
O script irá:

1. Ler o modelo IFC com `ifcopenshell`;
2. Converter elementos básicos para RDF (`rdflib`);
3. Inserir nós e relações no Neo4j usando `py2neo`.

---

## 🔎 Visualização no Neo4j Browser

No Browser (`localhost:7474`), escolha o banco **`ifctest`** e execute:

```cypher
-- Mostra todo o grafo (pode ficar pesado)
MATCH p=()-->() RETURN p;

-- Exibe também nós isolados
MATCH p=()-->() RETURN p
UNION
MATCH (n) WHERE NOT (n)-->() RETURN n;
```

Use os ícones de **layout force‑directed** e **tamanho de nó por grau** para explorar a topologia.

---

## 📂 Estrutura de repositório sugerida

```
.
├── data/
│   └── Building-Architecture.ifc
├── notebooks/
│   └── ifc.ipynb
├── src/
│   └── ifc_to_neo4j.py
└── README.md
```

---


> **Contribuições são bem‑vindas!** ✨
