import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.python import PythonSensor
from datetime import datetime

host_path = 'http://ship-service.ship.svc.cluster.local:80/'

def w04_async_api_call(**kwargs):
    ti = kwargs['ti']
    api_path = '/api/risk-mappings/w04'
    api_params = {
        'satellite_sar_image_id': 123456789
    }

    requests.get(host_path + api_path, params=api_params)


def w05_async_api_call(**kwargs):
    ti = kwargs['ti']
    api_path = '/api/risk-mappings/w05'
    api_params = {
        'satellite_sar_image_id': 123456789  
    }

    requests.get(host_path + api_path, params=api_params)


with DAG(
        'n_kcgsa_risk-mapping_img_dag',
        default_args={
            'owner': 'airflow',
            'start_date': datetime(2024, 9, 28),
        },
        schedule_interval='@hourly',  # 영상 트리거시 발동해야하나 우선은 1시간 단위로 실행
        catchup=False  # 과거 실행을 건너뛸지 여부 (False로 하면 과거 실행 건너뜀)
) as dag:
    w04_async_task = PythonOperator(
        task_id='w04',
        python_callable=w04_async_api_call
    )

    w05_async_task = PythonOperator(
        task_id='w05',
        python_callable=w05_async_api_call
    )

    # api_task >> next_task
    w04_async_task
    w05_async_task
