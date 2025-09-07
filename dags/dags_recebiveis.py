from datetime import timedelta
from airflow import DAG
from airflow.operators import PythonOperator
from airflow.utils.dates import days_ago

def task_ingest(**kwargs):
    from ingest.portal_cedente import run as portal_run
    from ingest.financeiro import run as financeiro_run
    portal_run()
    financeiro_run()

def task_transform(**kwargs):
    from transform.curate_recebiveis import run as curate_run
    curate_run()

def task_load(**kwargs):
    from transform.load_dw import run as load_run
    load_run()

with DAG('recebiveis_pipeline', start_date=days_ago(1), schedule_interval='@daily', default_args={'retries':1, 'retry_delay': timedelta(minutes=5)}) as dag:
    ingest = PythonOperator(task_id ='ingest', python_callable=task_ingest)
    transform = PythonOperator(task_id ='transform', python_callable=task_transform)
    load = PythonOperator(task_id='load', python_callable=task_load)

    ingest >> transform >> load