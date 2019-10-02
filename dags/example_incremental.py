from datetime import datetime

from airflow.models import DAG
from airflow.operators.postgres_operator import PostgresOperator

default_args = {'start_date': datetime(2019, 1, 1)}

dag = DAG(dag_id='example_incremental', default_args=default_args)

with dag:

    sql = '''
        DELETE FROM daily_totals 
        WHERE day = '{{ ds }}';

        INSERT INTO daily_totals
        SELECT 
            day,
            COUNT(*) AS total
        FROM
            table
        WHERE 
            day = '{{ ds }}';
    '''

    incremental_task = PostgresOperator(
        task_id='incremental_task',
        sql=sql,
    )



