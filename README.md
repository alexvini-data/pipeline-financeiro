# Pipeline Financeiro

Pipeline ETL de dados financeiros desenvolvido em Python com PostgreSQL.

## Sobre o projeto

Simula o fluxo de dados de uma fintech — extrai transações brutas,
realiza limpeza e categorização, detecta padrões suspeitos e carrega
os dados tratados em um banco de dados relacional para análise.

## Tecnologias

- Python 3.14
- Pandas
- PostgreSQL 18
- SQLAlchemy
- python-dotenv
- Git

## Estrutura

pipeline_financeiro/
├── data/                    # Dados brutos de entrada
├── pipeline/
│   ├── extracao.py          # Leitura da fonte de dados
│   ├── transformacao.py     # Limpeza e transformação
│   ├── carga.py             # Carga no banco de dados
│   └── analise.py           # Consultas SQL e insights
├── .env                     # Variáveis de ambiente (não versionado)
├── .gitignore
├── main.py                  # Orquestrador do pipeline
└── README.md

## Como rodar

1. Clone o repositório
   git clone https://github.com/alexvini-data/pipeline-financeiro.git

2. Instale as dependências
   pip install pandas sqlalchemy psycopg2-binary python-dotenv

3. Crie o banco de dados no PostgreSQL
   CREATE DATABASE pipeline_financeiro;

4. Crie o arquivo .env na raiz do projeto com as variáveis
   DB_USUARIO=postgres
   DB_SENHA=sua_senha
   DB_HOST=localhost
   DB_PORT=5432
   DB_NOME=pipeline_financeiro

5. Execute o pipeline
   python main.py

## O que o pipeline faz

- Extrai transações brutas de um arquivo CSV
- Remove transações sem valor
- Preenche categorias e cidades ausentes
- Carrega os dados tratados no PostgreSQL
- Gera análises de volume por categoria,
  transações suspeitas e transações recusadas