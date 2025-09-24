from datetime import datetime, timedelta
from typing import Any
from airflow.models import BaseOperator
from airflow.utils.context import Context
from airflow import DAG
from airflow.operators.dummy import DummyOperator


# Punto 4: Operador personalizado
class TimeDiffOperator(BaseOperator):
    def __init__(self, diff_date: datetime, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.diff_date = diff_date

    def execute(self, context: Context):
        now = datetime.utcnow()
        diff = now - self.diff_date
        self.log.info(f"La diferencia entre {self.diff_date} y {now} es {diff}")
        return diff


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
    schedule='0 3 * * *',  # Punto 1: Expresion CRON para ejecutar cada día a las 3:00 UTC
    catchup=False
) as dag:

    # Punto 2: tareas start y end. Colocamos end despues de start
    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")

    # Punto 3: lista de tareas dummy
    N = 6 
    tasks = [DummyOperator(task_id=f"task_{i}") for i in range(1, N + 1)]

    for i in range(1, N + 1):
        if i % 2 == 0:  # si es par
            for j in range(1, N + 1):
                if j % 2 != 0:  # si es impar
                    tasks[j - 1] >> tasks[i - 1]

    # Estructura del DAG
    start >> tasks >> end