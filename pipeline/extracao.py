import pandas as pd

def extrair(caminho: str) -> pd.DataFrame:
    df = pd.read_csv(caminho)
    print(f"[EXTRAÇÃO] {len(df)} registros extraídos.")
    return df