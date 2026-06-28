import pandas as pd
import os
from logger import logger
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def analisar() -> None:
    try:
        engine = create_engine(
            f"postgresql://{os.getenv('DB_USUARIO')}:{os.getenv('DB_SENHA')}"
            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NOME')}"
        )
    
        consultas = {
            "Transações por categoria": """
                SELECT
                    categoria,
                    COUNT(*)    AS total_transacoes,
                    ROUND(SUM(valor)::numeric, 2)   AS volume_total,
                    ROUND(AVG(valor)::numeric, 2)   AS ticket_medio
                FROM transacoes
                GROUP BY categoria
                ORDER BY volume_total DESC
            """,
            "Transações suspeitas (internacional + horário incomum)": """
                SELECT
                    id,
                    data,
                    valor,
                    tipo,
                    categoria,
                    internacional,
                    horario_incomum,
                    fraude
                FROM transacoes
                WHERE internacional = 'Yes'
                    AND horario_incomum = 'Yes'
                ORDER BY data DESC
                LIMIT 50
            """,
            "Distribuição de fraudes por categoria": """
                SELECT
                    categoria,
                    fraude,
                    COUNT(*) AS total
                FROM transacoes
                GROUP BY categoria, fraude
                ORDER BY total DESC
            """,
            "Ranking de valor por categoria": """
                SELECT
                    id,
                    categoria,
                    tipo,
                    valor,
                    RANK() OVER (
                        PARTITION BY categoria
                        ORDER BY valor DESC
                    ) AS ranking_na_categoria
                FROM transacoes
                ORDER BY categoria, ranking_na_categoria
                LIMIT 20
            """,
            "Categoria com volume acima da média geral": """
                WITH media_geral AS (
                    SELECT AVG(valor) AS media
                    FROM transacoes
                ),
                volume_por_categoria AS (
                    SELECT
                        categoria,
                        ROUND(SUM(valor)::numeric, 2) AS volume_total,
                        ROUND(AVG(valor)::numeric, 2) AS ticket_medio
                    FROM transacoes
                    GROUP BY categoria
                )
                SELECT
                    v.categoria,
                    v.volume_total,
                    v.ticket_medio,
                    ROUND(m.media::numeric, 2) AS media_geral
                FROM volume_por_categoria v
                CROSS JOIN media_geral m
                WHERE v.ticket_medio > m.media
                ORDER BY v.volume_total DESC
            """
        }
        
        for titulo, sql in consultas.items():
            print(f"\n{'='*50}")
            print(f"  {titulo.upper()}")
            print(f"{'='*50}")
            df = pd.read_sql(sql, con=engine)
            print(df.to_string(index=False))
            logger.info(f"[ANÁLISE] '{titulo}' — {len(df)} registros retornados.")
        
    except Exception as e:
        logger.error(f"[ERRO] Falha na análise: {e}")
        raise