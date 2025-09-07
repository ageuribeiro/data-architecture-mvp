# ingest/portal_cedente.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def run():
    n = 100
    df = pd.DataFrame({
        'cedente_id': [f'C{str(i).zfill(3)}' for i in range(n)],
        'nome': [f'Cedente {i}' for i in range(n)],
        'cnpj': [f'{np.random.randint(10000000,99999999)}' for _ in range(n)],
        'segmento': np.random.choice(['A','B','C'], n),
        'risk_score': np.random.rand(n)*100
    })
    df.to_parquet('data_lake/raw/cedente.parquet', index=False)
    print("Portal cedente gerado!")

if __name__=="__main__":
    run()