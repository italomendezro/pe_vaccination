from datetime import datetime, time, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from pe_vacunacion import run_vaccination_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021,6,27),
    'email': ['italo.mendezro@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'pe_vaccination_dag',
    default_args=default_args,
    description='DAG for PE Vaccination',
    schedule_interval=timedelta(minutes=30)
)

def check_log():
    print('Running script')

run_etl = PythonOperator(
    task_id='whole_pe_vacc_etl',
    python_callable=run_vaccination_etl,
    dag=dag
)

run_etl