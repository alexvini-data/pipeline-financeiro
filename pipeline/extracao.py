import pandas as pd

def extrair(caminho: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(caminho)
        print(f"[EXTRAÇÃO] {len(df)} registros extraídos.")
        return df
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado {caminho}")
        raise
    except Exception as e:
        print(f"[ERRO] Falha na extração: `{e}")
        raise