from datetime import datetime

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'start_date': datetime(2019, 1, 1)}

dag = DAG(dag_id='example_template', default_args=default_args)

with dag:
    task = BashOperator(
        task_id='task',
        bash_command='echo {{ ds }} {{ params.param }}',
        params={'param': 'value'},
    )

