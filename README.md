# Pipeline Financeiro

Pipeline ETL de dados financeiros desenvolvido em Python com PostgreSQL.

## Sobre o projeto

Simula o fluxo de dados de uma fintech — extrai transações brutas,
realiza limpeza e categorização, detecta padrões suspeitos e carrega
os dados tratados em um banco de dados relacional para análise com SQL avançado.

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
├── logs/                    # Logs de execução (não versionado)
├── pipeline/
│   ├── extracao.py          # Leitura da fonte de dados
│   ├── transformacao.py     # Limpeza e transformação
│   ├── carga.py             # Carga no banco de dados
│   └── analise.py           # Consultas SQL e insights
├── .env                     # Variáveis de ambiente (não versionado)
├── .gitignore
├── logger.py                # Configuração de logging
├── main.py                  # Orquestrador do pipeline
└── README.md

## O que o pipeline faz

- Extrai transações brutas de um arquivo CSV
- Remove transações sem valor
- Preenche categorias e cidades ausentes
- Carrega os dados tratados no PostgreSQL
- Gera análises com SQL avançado:
  - Volume e ticket médio por categoria
  - Detecção de transações suspeitas acima de R$ 5.000
  - Ranking de transações por valor dentro de cada categoria (window function)
  - Categorias com ticket médio acima da média geral (CTE)
- Registra todas as execuções em arquivo de log com timestamp

## Como rodar

1. Clone o repositório
   git clone https://github.com/alexvini-data/pipeline-financeiro.git

2. Instale as dependências
   pip install pandas sqlalchemy psycopg2-binary python-dotenv

3. Crie o banco de dados no PostgreSQL
   CREATE DATABASE pipeline_financeiro;

4. Crie o arquivo .env na raiz do projeto
   DB_USUARIO=postgres
   DB_SENHA=sua_senha
   DB_HOST=localhost
   DB_PORT=5432
   DB_NOME=pipeline_financeiro

5. Execute o pipeline
   python main.py

## Conceitos aplicados

- ETL — Extract, Transform, Load
- Tratamento de dados nulos com regras de negócio
- SQL avançado — window functions e CTEs
- Variáveis de ambiente para segurança de credenciais
- Logging profissional com FileHandler e StreamHandler
- Separação de responsabilidades por módulo
- Versionamento com Git e boas práticas de commit