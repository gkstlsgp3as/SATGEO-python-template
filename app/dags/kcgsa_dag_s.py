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
    # conn = psycopg2.connect(**DB_CONN_PARAMS)
    # cursor = conn.cursor()
    #
    # # 예시: 특정 테이블에 원하는 값이 있는지 확인
    # cursor.execute("SELECT * FROM my_table WHERE condition_met = TRUE")
    # result = cursor.fetchone()
    #
    # cursor.close()
    # conn.close()

    result = True

    # 조건 만족 시 s01 task 로 진행, 아니면 s1_end_task 에서 종료
    if result:
        return 's01'
    else:
        return 's01_end_task'


def s01_api_call():
    print('s01 completed')


def s02_api_call():
    print('s02 completed')


def s05_api_call():
    print('s05 completed')


def s06_api_call():
    print('s06 completed')


def s03_check_shipdet_branch(**kwargs):
    # conn = psycopg2.connect(**DB_CONN_PARAMS)
    # cursor = conn.cursor()
    #
    # # 예시: 특정 테이블에 원하는 값이 있는지 확인
    # cursor.execute("SELECT * FROM my_table WHERE condition_met = TRUE")
    # result = cursor.fetchone()
    #
    # cursor.close()
    # conn.close()

    result = True

    # 조건 만족 시 s03 task 로 진행, 아니면 s3_end_task 에서 종료
    if result:
        return 's03'
    else:
        return 's03_end_task'


def s03_api_call():
    print('s03 completed')


def s04_api_call():
    print('s04 completed')


def s09_api_call():
    print('s09 completed')


with DAG(
        'n_kcgsa_ship_dag',
        default_args={
            'owner': 'airflow',
            'start_date': datetime(2024, 9, 28),
            'schedule_interval': '*/10 * * * *',  # 10분마다 실행
            'catchup': False,
        }
) as dag:
    s01_check_task = BranchPythonOperator(
        task_id='s01_l1a_l1d_check',
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

    s05_task = PythonOperator(
        task_id='s05',
        python_callable=s05_api_call
    )

    s06_task = PythonOperator(
        task_id='s06',
        python_callable=s06_api_call
    )

    s03_check_task = BranchPythonOperator(
        task_id='s03_l1d_ais_check',
        python_callable=s03_check_shipdet_branch,
        provide_context=True
    )

    s03_end_task = DummyOperator(
        task_id='s03_end_task'
    )

    s03_task = PythonOperator(
        task_id='s03',
        python_callable=s03_api_call
    )

    s04_task = PythonOperator(
        task_id='s04',
        python_callable=s04_api_call
    )

    s09_task = PythonOperator(
        task_id='s09',
        python_callable=s09_api_call
    )

    s01_check_task >> s01_task >> s02_task >> [s05_task, s06_task]
    s01_check_task >> s01_end_task

    s03_check_task >> s03_task
    s03_check_task >> s03_end_task

    [s01_task, s03_task] >> s04_task >> s09_task
