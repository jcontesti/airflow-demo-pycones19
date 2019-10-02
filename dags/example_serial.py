from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {'start_date': datetime(2019, 1, 1)}

dag = DAG(dag_id='example_serial', default_args=default_args)

with dag:
    first_task = DummyOperator(task_id='first_task')
    second_task = DummyOperator(task_id='second_task')
    third_task = DummyOperator(task_id='third_task')

    second_task.set_upstream(first_task)
    third_task.set_upstream(second_task)
