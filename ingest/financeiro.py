import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def run():
    n = 200
    start_date = datetime.today() - timedelta(days=30)
    df = pd.DataFrame({
        'date': [start_date + timedelta(days=i%30) for i in range(n)],
        'cedente_id': [f'C{str(np.random.randint(0,100)).zfill(3)}' for _ in range(n)],
        'produto_id': [f'P{str(np.random.randint(0,10)).zfill(2)}' for _ in range(n)],
        'valor_bruto': np.random.rand(n)*10000,
        'taxa_pct': np.random.rand(n)*5,
        'valor_liquido': lambda x: x['valor_bruto']*(1-x['taxa_pct']/100),
        'quantidade_documentos': np.random.randint(1,10,n),
        'data_processamento': datetime.now()
    })

    df.to_parquet('data_lake/raw/financeiro.parquet', index=False)
    print("Financeiro gerado!")

if __name__ == "__main__":
    run()