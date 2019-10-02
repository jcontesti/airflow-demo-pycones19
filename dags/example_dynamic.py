from datetime import datetime

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'start_date': datetime(2019, 1, 1)}

dag = DAG(dag_id='example_dynamic', default_args=default_args)

with dag:

    dynamic_tasks = []
    for task_id in range(5):
        dynamic_task = BashOperator(
            task_id='dynamic_task_' + str(task_id),
            bash_command='echo {{ task.task_id }}',
        )
        dynamic_tasks.append(dynamic_task)

    end_task = BashOperator(
            task_id='end_task',
            bash_command='echo {{ task.task_id }}',
    )
    end_task.set_upstream(dynamic_tasks)

