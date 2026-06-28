import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def carregar(df: pd.DataFrame) -> None:
    try:
        engine = create_engine(
            f"postgresql://{os.getenv('DB_USUARIO')}:{os.getenv('DB_SENHA')}"
            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NOME')}"
        )
        df.to_sql("transacoes", con=engine, if_exists="replace", index=False)
        print(f"[CARGA] {len(df)} registros salvos no banco.")
    except Exception as e:
        print(f"ERRO Falha na carga: {e}")
        raise