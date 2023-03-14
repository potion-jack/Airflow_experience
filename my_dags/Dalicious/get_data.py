import pandas as pd

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id = "Dalicious get data",
    start_date = airflow.utils.dates.days_ago(21),
    schudule_interval = None
)
