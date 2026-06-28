import pandas as pd
from logger import logger

def extrair(caminho: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(caminho)
        logger.info(f"[EXTRAÇÃO] {len(df)} registros extraídos.")
        return df
    except FileNotFoundError:
        logger.error(f"[ERRO] Arquivo não encontrado {caminho}")
        raise
    except Exception as e:
        logger.error(f"[ERRO] Falha na extração: `{e}")
        raise