import pandas as pd
import sqlalchemy

def run():
    engine = sqlalchemy.create_engine('postgresql+psycop2://admin:admin@localhost:5432/dw')
    df = pd.read_parquet('data_lake/staged/recebiveis_curado.parquet')
    df.to_sql('fact_recebiveis', engine, if_exists='append', index=False)
    print('Carregando no DW!')