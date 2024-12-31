import requests
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
import psycopg2

# Database와 API 설정
DB_CONN_PARAMS = {
    'dbname': 'mydb',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'localhost',
    'port': 5432
}
host_path = 'http://ship-service.ship.svc.cluster.local:80/'
# host_path = 'http://127.0.0.1:8000'
#host_path = 'http://host.docker.internal:8000'

def s01_check_shipdet_branch(**kwargs):
    ti = kwargs['ti']
    
    status = ti.xcom_pull(key='s01_status')

    # 조건 만족 시 s02 task 로 진행, 아니면 s1_end_task 에서 종료
    if status:       # 미식별 선박 존재 시 
        return 's02'
    else:
        return 's01_end_task'


def s01_api_call(execution_date, **kwargs):
    api_path = '/api/risk-mappings/s01'
    api_params = {
        'satellite_sar_image_id': 1234567890,
    }
    response = requests.get(host_path + api_path, params=api_params)  
    ti.xcom_push(key='s01_status', value=response.status)
    ti.xcom_push(key='s01_img_id', value=api_params.satellite_sar_image_id)
    if response.status == 'completed':    # 미식별 선박이 존재하면
        return True
    else:    # status == 'no_unidentification'
        print(f"Note: No Unidentifcation Ships")
        return False
        

def s02_api_call(execution_date, **kwargs):
    formatted_date = execution_date.strftime('%Y%m%d%H') + '0000'
    api_path = '/api/risk-mappings/s02'
    api_params = {
        'satellite_sar_image_id': ti.xcom_pull(key='s01_img_id')
    }

    requests.get(host_path + api_path, params=api_params)


with DAG(
        'n_kcgsa_ship_dag',
        default_args={
            'owner': 'airflow',
            'start_date': datetime(2024, 9, 28),
            'schedule_interval': @hourly,  # 1시간마다 실행
            'catchup': False,
        }
) as dag:
    s01_check_task = BranchPythonOperator(
        task_id='s01_unid_check',
        python_callable=s01_check_shipdet_branch,
        provide_context=True
    )

    s01_end_task = DummyOperator(
        task_id='s01_end_task'
    )

    s01_task = PythonOperator(
        task_id='s01',
        python_callable=s01_api_call
    )

    s02_task = PythonOperator(
        task_id='s02',
        python_callable=s02_api_call
    )


    s01_task >> s01_check_task >> s02_task 
    s01_check_task >> s01_end_task

