# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Dimas Wahyu Saputro',
    'start_date': days_ago(0),
    'email': ['diwms29@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

# define the DAG
dag = DAG(
    dag_id='rawg-etl',
    default_args=default_args,
    description='Extracting, Transforming and Loading RAWG API data to MySQL',
    schedule_interval='@once',
)

# define the tasks
extract = BashOperator(
    task_id='get_data_from_api',
    bash_command='$AIRFLOW_HOME/dags/scripts/get_data.sh ',
    dag=dag,
)

transform = BashOperator(
    task_id='transform_data',
    bash_command='python $AIRFLOW_HOME/dags/scripts/transform_data.py',
    dag=dag,
)

load = BashOperator(
    task_id='load_to_mysql',
    bash_command='python $AIRFLOW_HOME/dags/scripts/load_data_to_db.py',
    dag=dag,
)

# task pipeline
extract >> transform >> load