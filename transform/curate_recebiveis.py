import pandas as pd

def run():
    df_cedente = pd.read_parquet('data_lake/raw/cedente.parquet')
    df_fin = pd.read_parquet('data_lake/raw/financeiro.parquet')

    # máscara cnpj
    df_cedente['cnpj_masked'] = df_cedente['cnpj'].str[:2] + '***.***.***/****-**'

    # merge
    df_curado = df_fin.merge(df_cedente[['cedente_id','nome','cnpj_masked']], on='cedente_id', how='left')

    # grava staged
    df_curado.to_parquet('data_lake/staged/recebiveis_curado.parquet', index=False)
    print("Curated stage gerada!")