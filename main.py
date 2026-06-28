from pipeline.extracao import extrair
from pipeline.transformacao import transformar
from pipeline.carga import carregar
from pipeline.analise import analisar

df_bruto = extrair("data/transacoes_reais.csv")
df_limpo = transformar(df_bruto)
carregar(df_limpo)
analisar()