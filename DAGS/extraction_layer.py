"""
**********************************************************
2023-20-06
Prueba técnica Nequi - Data Engineer
Elaborado por: Danilo Hernando Moreno Gonzalez
Script correspondiente al DAG de la capa de ingesta
**********************************************************
"""

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Definir los argumentos default del DAG
default_args = {
    'owner': 'Danilo',
    'start_date': datetime(2023, 6, 20),
    'retries': 3,
}

# Definir los argumentos complementarios del DAG
args = {
    'schedule_interval': '05 00 * * *',
    'catchup': False,
    'concurrency': 2,
    'max_active_runs': 2,
    'tags': ['extraction_layer', 'dev']
}

# Crear el objeto DAG
dag = DAG('extraction_layer', default_args=default_args, **args)

"""
++++++++++++++++++++++++++++++++
Definir las funciones a utilizar
++++++++++++++++++++++++++++++++
"""


# Acciones para task: CRM_extraction
def CRM_extraction_func():
    print("Ingestando los datos del CRM mediante JDBC connector... (Trigger Job Glue )")
    print("Luego almacenando los datos en S3 en la zona 'Raw'...")

# Acciones para task: count_source_extraction
def count_source_extraction_func():
    print("Comprobaciones de fuente/conteo para asegurar la integridad de los datos...")

# Acciones para task: AWS_run_crawler
def AWS_run_crawler_func():
    print("Trigger crawler para actualizar el catalogo de Glue...")


"""
Definir las tareas

"""
start = DummyOperator(task_id='start', dag=dag)

CRM_extraction = PythonOperator(
    task_id='CRM_extraction', python_callable=CRM_extraction_func, dag=dag)

count_source_extraction = PythonOperator(
    task_id='count_source_extraction', python_callable=count_source_extraction_func, dag=dag)

AWS_run_crawler = PythonOperator(
    task_id='AWS_run_crawler', python_callable=AWS_run_crawler_func, dag=dag)

# Definir las dependencias entre las tareas
start >> CRM_extraction
CRM_extraction >> count_source_extraction
count_source_extraction >> AWS_run_crawler
