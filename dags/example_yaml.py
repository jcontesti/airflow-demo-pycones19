import yaml
import glob
from datetime import datetime

from airflow.models import DAG
from airflow.operators.postgres_operator import PostgresOperator

YAML_DIR = '/usr/local/airflow/dags'

default_args = {'start_date': datetime(2019, 1, 1)}

dag = DAG(dag_id='example_yaml', default_args=default_args)

with dag:
    for filename in glob.glob(YAML_DIR + '/*.yaml'):
        with open(filename, 'r') as stream:
            yaml_data = yaml.safe_load(stream)

            incremental_task = PostgresOperator(
                task_id=yaml_data['task_id'],
                sql=yaml_data['sql'],
            )

