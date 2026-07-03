# Pipeline Financeiro

Pipeline ETL de dados financeiros com dashboard de análise de fraudes.

## Sobre o projeto

Extrai transações financeiras brutas com valores ausentes, realiza imputação
e remoção dos registros inválidos, e carrega os dados tratados num banco
PostgreSQL para análise de padrões de fraude com SQL avançado e Power BI.

## Tecnologias

- Python 3.14
- Pandas
- PostgreSQL 18
- SQLAlchemy
- python-dotenv
- pytest
- Power BI Desktop
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
├── tests/
│   └── test_transformacao.py  # Testes automatizados com pytest
├── .env                     # Variáveis de ambiente (não versionado)
├── .gitignore
├── dashboard_financeiro.pbix  # Dashboard Power BI
├── logger.py                # Configuração de logging
├── main.py                  # Orquestrador do pipeline
└── README.md

## O que o pipeline faz

- Extrai 50.000 transações financeiras reais de um arquivo CSV
- Remove transações sem valor registrado
- Preenche categorias e outros campos ausentes com valores padrão
- Carrega os dados tratados no PostgreSQL
- Gera análises com SQL avançado:
  - Volume e ticket médio por categoria
  - Detecção de transações suspeitas (internacional + horário incomum)
  - Distribuição de fraudes por categoria
  - Ranking de transações por valor dentro de cada categoria (window function)
  - Categorias com ticket médio acima da média geral (CTE)
- Registra todas as execuções em arquivo de log com timestamp
- Dashboard Power BI conectado diretamente ao banco PostgreSQL

## Resultados

- 49.985 transações processadas
- 4,84% de taxa de fraude identificada
- R$ 249,92 mil em volume total analisado

## Como rodar

1. Clone o repositório
   git clone https://github.com/alexvini-data/pipeline-financeiro.git

2. Instale as dependências
   pip install pandas sqlalchemy psycopg2-binary python-dotenv pytest

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

6. Execute os testes
   python -m pytest tests/ -v

7. Abra o dashboard
   Abra o arquivo dashboard_financeiro.pbix no Power BI Desktop

## Conceitos aplicados

- ETL — Extract, Transform, Load
- Imputação de dados nulos com regras de negócio
- SQL avançado — window functions e CTEs
- Detecção de padrões de fraude
- Variáveis de ambiente para segurança de credenciais
- Logging profissional com FileHandler e StreamHandler
- Testes automatizados com pytest
- Separação de responsabilidades por módulo
- Versionamento com Git e boas práticas de commit