from pipeline.extracao import extrair
from pipeline.transformacao import transformar
from pipeline.carga import carregar

df_bruto = extrair("data/transacoes_brutas.csv")
df_limpo = transformar(df_bruto)
carregar(df_limpo, senha="#Paparata123")