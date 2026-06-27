import pandas as pd 

def transformar(df: pd.DataFrame) -> pd.DataFrame:
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

    print(f"[TRANFORMAÇÃO] {len(df)} registros após limpeza.")
    return df