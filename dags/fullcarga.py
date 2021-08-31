from datetime import datetime, timedelta

from airflow.models import Variable
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from fullcargascript import cargascript

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 8, 30, 23, 30),
    'retries': 0,    
    'email_on_failure': False,
    'catchup': False,
    'depends_on_past': False,
}

name = 'CargaFull'

schedule = '* * * * *'

dag = DAG(name, schedule_interval=schedule, default_args=default_args)


cargafull = cargascript

t1 = PythonOperator(
    task_id= 'CargaFull',
    dag=dag,
    provide_context=True,
    python_callable=cargafull
)
