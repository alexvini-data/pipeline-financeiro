import pandas as pd
import pytest
from pipeline.transformacao import transformar

def criar_df_teste():
    return pd.DataFrame({
        "Transaction_ID":                  [1.0, 2.0, 3.0, 4.0],
        "Customer_ID":                     [10.0, 20.0, 30.0, 40.0],
        "Transaction_Amount (in Million)": [5.0, None, 3.0, 7.0],
        "Transaction_Date":                ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
        "Transaction_Type":                ["Online", "POS", "ATM", "Online"],
        "Merchant_Category":               ["Fuel", "Normal", None, "ATM"],
        "Is_International_Transaction":    ["Yes", "No", None, "Yes"],
        "Unusual_Time_Transaction":        ["No", "Yes", "No", None],
        "Fraud_Label":                     ["Normal", "Fraud", None, "Normal"]
    })
    
def test_remove_linhas_sem_valor():
    df = criar_df_teste()
    resultado = transformar(df)
    assert resultado["valor"].isnull().sum() == 0
    
def test_preenche_categoria_desconhecida():
    df = criar_df_teste()
    resultado = transformar(df)
    assert "desconhecida" in resultado["categoria"].values
    
def test_preenche_internacional_no():
    df = criar_df_teste()
    resultado = transformar(df)
    assert resultado["internacional"].isnull().sum() == 0
    
def test_converte_data_para_datetime():
    df = criar_df_teste()
    resultado = transformar(df)
    assert pd.api.types.is_datetime64_any_dtype(resultado["data"])
    
def test_valor_e_float():
    df = criar_df_teste()
    resultado = transformar(df)
    assert resultado["valor"].dtype == float