from datetime import datetime

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {'start_date': datetime(2019, 1, 1)}

dag = DAG(dag_id='example_python', default_args=default_args)


def execute_first_task():
    print('first task')


def execute_second_task():
    print('second task')


with dag:
    first_task = PythonOperator(
        task_id='first_task',
        python_callable=execute_first_task,
    )

    second_task = PythonOperator(
        task_id='second_task',
        python_callable=execute_second_task,
    )

    second_task.set_upstream(first_task)

