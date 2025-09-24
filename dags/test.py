from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

# Definición del DAG
with DAG(
    'test',
    default_args=default_args,
    schedule='0 3 * * *',  # Punto 2: Expresion CRON para ejecutar cada día a las 3:00 UTC
    catchup=False
) as dag:

    pass