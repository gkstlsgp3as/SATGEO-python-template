import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.python import PythonSensor
from datetime import datetime

host_path = 'http://ship-service.ship.svc.cluster.local:80/'


def s05_api_call(execution_date, **kwargs):
    api_path = '/api/ships/s05'
    api_params = {
        'max-hour': 48
    }

    requests.get(host_path + api_path, params=api_params)


with DAG(
        'n_kcgsa_ship-classification_dag',
        default_args={
            'owner': 'airflow',
            'start_date': datetime(2024, 12, 29),
        },
        schedule_interval=timedelta(minutes=3)
        #schedule_interval='@hourly',  # 매 시 실행
        catchup=False  # 과거 실행을 건너뛸지 여부 (False로 하면 과거 실행 건너뜀)
) as dag:

    s05_task = PythonOperator(
        task_id='s05',
        python_callable=s05_api_call
    )

    # api_task >> next_task
    s05_task
