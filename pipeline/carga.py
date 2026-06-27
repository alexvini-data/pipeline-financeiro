from sqlalchemy import create_engine
import pandas as pd

def carregar(df: pd.DataFrame, senha: str) -> None:
    engine = create_engine(
        f"postgresql://postgres:{senha}@localhost:5432/pipeline_financeiro"
    )
    df.to_sql("transacoes", con=engine, if_exists="replace", index=False)
    print(f"[CARGA] {len(df)} registros salvos no banco.")