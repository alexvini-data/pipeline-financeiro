import pandas as pd
import os
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
            "Transações suspeitas (valor acima de 5000)": """
                SELECT
                    id,
                    data,
                    valor,
                    comerciante,
                    status
                FROM transacoes
                WHERE valor > 5000
                ORDER BY valor DESC
            """,
            "Transações recusadas": """
                SELECT
                    id,
                    data,
                    valor,
                    comerciante,
                    status
                FROM transacoes
                WHERE status = 'recusado'
            """
        }
        
        for titulo, sql in consultas.items():
            print(f"\n{'='*50}")
            print(f"    {titulo.upper()}")
            print(f"{'='*50}")
            df = pd.read_sql(sql, con=engine)
            print(df.to_string(index=False))
        
    except Exception as e:
        print(f"[ERRO] Falha na análise: {e}")
        raise