import pandas as pd
from logger import logger 

def transformar(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # Remove transações sem valor
        df = df.dropna(subset=["valor"])
        #Preenche categorias desconhecidas
        df["categoria"] = df["categoria"].fillna("desconhecida")
        #Preenche cidades não informadas
        df["cidade"] = df["cidade"].fillna("não informada")
        #Converte data para formato de data real
        df["data"] = pd.to_datetime(df["data"])
        #Converte valor para float
        df["valor"] = df["valor"].astype(float)
        logger.info(f"[TRANFORMAÇÃO] {len(df)} registros após limpeza.")
        return df
    except KeyError as e:
        logger.error(f"[ERRO] Coluna não encontrada: {e}")
        raise
    except Exception as e:
        logger.error(f"[ERRO] Falha ma transformação: {e}")
        raise