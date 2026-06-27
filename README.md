# Pipeline Financeiro

Pipeline ETL de dados financeiros desenvolvido em Python com PostgreSQL.

## Sobre o projeto

Simula o fluxo de dados de uma fintech — extrai transações brutas, realiza limpeza e categorização, detecta padrões suspeitos e carrega os dados tratados em um banco de dados relacional.

## Tecnologias

- Python 3.14
- Pandas
- PostgreSQL
- SQLAlchemy
- Git

## Estrutura

pipeline_financeiro/
├── data/               # Dados brutos
├── pipeline/
│   ├── extracao.py     # Leitura da fonte de dados
│   ├── transformacao.py # Limpeza e transformação
│   ├── carga.py        # Carga no banco de dados
│   └── analise.py      # Consultas e insights
└── main.py             # Orquestrador do pipeline

## Como rodar

1. Clone o repositório
2. Instale as dependências: pip install pandas sqlalchemy psycopg2-binary
3. Crie o banco de dados no PostgreSQL: CREATE DATABASE pipeline_financeiro;
4. Execute: python main.py