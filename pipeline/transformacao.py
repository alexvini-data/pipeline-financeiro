import pandas as pd
from logger import logger


def transformar(df: pd.DataFrame) -> pd.DataFrame:
    try:
        colunas = [
            "Transaction_ID",
            "Customer_ID",
            "Transaction_Amount (in Million)",
            "Transaction_Date",
            "Transaction_Type",
            "Merchant_Category",
            "Is_International_Transaction",
            "Unusual_Time_Transaction",
            "Fraud_Label"
        ]
        df = df[colunas]

        df = df.rename(columns={
            "Transaction_ID":               "id",
            "Customer_ID":                  "cliente_id",
            "Transaction_Amount (in Million)": "valor",
            "Transaction_Date":             "data",
            "Transaction_Type":             "tipo",
            "Merchant_Category":            "categoria",
            "Is_International_Transaction": "internacional",
            "Unusual_Time_Transaction":     "horario_incomum",
            "Fraud_Label":                  "fraude"
        })

        df = df.dropna(subset=["valor", "id"])
        df["categoria"]      = df["categoria"].fillna("desconhecida")
        df["fraude"]         = df["fraude"].fillna("Unknown")
        df["internacional"]  = df["internacional"].fillna("No")
        df["horario_incomum"] = df["horario_incomum"].fillna("No")
        df["data"]           = pd.to_datetime(df["data"], errors="coerce")
        df = df.dropna(subset=["data"])
        df["valor"]          = df["valor"].astype(float)

        logger.info(f"[TRANSFORMAÇÃO] {len(df)} registros após limpeza.")
        return df

    except KeyError as e:
        logger.error(f"[TRANSFORMAÇÃO] Coluna não encontrada: {e}")
        raise
    except Exception as e:
        logger.error(f"[TRANSFORMAÇÃO] Falha inesperada: {e}")
        raise