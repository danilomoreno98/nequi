"""
**********************************************************
2023-20-06
Prueba técnica Nequi - Data Engineer
Elaborado por: Danilo Hernando Moreno Gonzalez
Script correspondiente al DAG de la capa de procesamiento y modelado
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
    'schedule_interval': '00 07 * * *',
    'catchup': False,
    'concurrency': 2,
    'max_active_runs': 2,
    'tags': ['modeling_layer', 'dev']
}

# Crear el objeto DAG
dag = DAG('processing_modeling_layer', default_args=default_args, **args)

"""
++++++++++++++++++++++++++++++++
Definir las funciones a utilizar
++++++++++++++++++++++++++++++++
"""


# Acciones para RUN task: stg_dim_date
def stg_dim_date_run_func():
    print("Creando el modelo de la dimensión stg_dim_date...")

# Acciones para TEST task: stg_dim_date
def stg_dim_date_test_func():
    print("Realizo pruebas de calidad sobre stg, luego almaceno los datos en S3 en la zona 'Silver'...")

# Acciones para FINAL task: dim_date
def dim_date_func():
    print("Creo la tabla final de dim_date en zona Gold y Datawarehouse'...")

# Acciones para RUN task: stg_dim_customers
def stg_dim_customers_run_func():
    print("Creando el modelo de la dimensión stg_dim_customers...")

# Acciones para TEST task: stg_dim_customers
def stg_dim_customers_test_func():
    print("Realizo pruebas de calidad sobre stg, luego almaceno los datos en S3 en la zona 'Silver'...")

# Acciones para FINAL task: dim_customers
def dim_customers_func():
    print("Creo la tabla final de dim_customers en zona Gold y Datawarehouse'...")

# Acciones para RUN task: stg_dim_products
def stg_dim_products_run_func():
    print("Creando el modelo de la dimensión stg_dim_products...")

# Acciones para TEST task: stg_dim_products
def stg_dim_products_test_func():
    print("Realizo pruebas de calidad sobre stg, luego almaceno los datos en S3 en la zona 'Silver'...")

# Acciones para FINAL task: dim_products
def dim_products_func():
    print("Creo la tabla final de dim_products en zona Gold y Datawarehouse'...")

# Acciones para RUN task: stg_fct_invoices
def stg_fct_invoices_run_func():
    print("Creando el modelo de la dimensión stg_fct_invoices...")

# Acciones para TEST task: stg_fct_invoices
def stg_fct_invoices_test_func():
    print("Realizo pruebas de calidad sobre stg, luego almaceno los datos en S3 en la zona 'Silver'...")

# Acciones para FINAL task: fct_invoices
def fct_invoices_func():
    print("Creo la tabla final de fct_invoices en zona Gold y Datawarehouse'...")

# Acciones para task: AWS_run_crawler
def AWS_run_crawler_func():
    print("Trigger crawler para actualizar el catalogo de Glue...")


"""
Definir las tareas

"""
start = DummyOperator(task_id='start', dag=dag)


# *************** Branch dim_date ***************
# Tarea RUN stg_dim_date
stg_dim_date_run = PythonOperator(
    task_id='stg_dim_date_run', python_callable=stg_dim_date_run_func, dag=dag)
# Tarea QUALITY stg_dim_date
stg_dim_date_test = PythonOperator(
    task_id='stg_dim_date_test', python_callable=stg_dim_date_test_func, dag=dag)
# Tarea CRAWLER stg_dim_date
AWS_run_crawler_stg_dim_date = PythonOperator(
    task_id='AWS_run_crawler_stg_dim_date', python_callable=AWS_run_crawler_func, dag=dag)
# Tarea FINAL MODEL dim_date
dim_date = PythonOperator(
    task_id='dim_date', python_callable=dim_date_func, dag=dag)

# Definir las dependencias entre las tareas
start >> stg_dim_date_run
stg_dim_date_run >> stg_dim_date_test
stg_dim_date_test >> AWS_run_crawler_stg_dim_date
AWS_run_crawler_stg_dim_date >> dim_date

# *************** Branch dim_customers ***************
# Tarea RUN stg_dim_customers
stg_dim_customers_run = PythonOperator(
    task_id='stg_dim_customers_run', python_callable=stg_dim_customers_run_func, dag=dag)
# Tarea QUALITY stg_dim_customers
stg_dim_customers_test = PythonOperator(
    task_id='stg_dim_customers_test', python_callable=stg_dim_customers_test_func, dag=dag)
# Tarea CRAWLER stg_dim_customers
AWS_run_crawler_stg_dim_customers = PythonOperator(
    task_id='AWS_run_crawler_stg_dim_customers', python_callable=AWS_run_crawler_func, dag=dag)
# Tarea FINAL MODEL dim_customers
dim_customers = PythonOperator(
    task_id='dim_customers', python_callable=dim_customers_func, dag=dag)

# Definir las dependencias entre las tareas
start >> stg_dim_customers_run
stg_dim_customers_run >> stg_dim_customers_test
stg_dim_customers_test >> AWS_run_crawler_stg_dim_customers
AWS_run_crawler_stg_dim_customers >> dim_customers


# *************** Branch dim_products ***************
# Tarea RUN stg_dim_products
stg_dim_products_run = PythonOperator(
    task_id='stg_dim_products_run', python_callable=stg_dim_products_run_func, dag=dag)
# Tarea QUALITY stg_dim_products
stg_dim_products_test = PythonOperator(
    task_id='stg_dim_products_test', python_callable=stg_dim_products_test_func, dag=dag)
# Tarea CRAWLER stg_dim_products
AWS_run_crawler_stg_dim_products = PythonOperator(
    task_id='AWS_run_crawler_stg_dim_product', python_callable=AWS_run_crawler_func, dag=dag)
# Tarea FINAL MODEL dim_products
dim_products = PythonOperator(
    task_id='dim_products', python_callable=dim_products_func, dag=dag)

# Definir las dependencias entre las tareas
start >> stg_dim_products_run
stg_dim_products_run >> stg_dim_products_test
stg_dim_products_test >> AWS_run_crawler_stg_dim_products
AWS_run_crawler_stg_dim_products >> dim_products


# *************** Branch fct_invoices ***************
# Tarea RUN stg_fct_invoices
stg_fct_invoices_run = PythonOperator(
    task_id='stg_fct_invoices_run', python_callable=stg_fct_invoices_run_func, dag=dag)
# Tarea QUALITY stg_fct_invoices
stg_fct_invoices_test = PythonOperator(
    task_id='stg_fct_invoices_test', python_callable=stg_fct_invoices_test_func, dag=dag)
# Tarea CRAWLER stg_fct_invoices
AWS_run_crawler_stg_fct_invoices = PythonOperator(
    task_id='AWS_run_crawler_stg_fct_invoices', python_callable=AWS_run_crawler_func, dag=dag)
# Tarea FINAL MODEL fct_invoices
fct_invoices = PythonOperator(
    task_id='fct_invoices', python_callable=fct_invoices_func, dag=dag)

# Definir las dependencias entre las tareas
start >> stg_fct_invoices_run
stg_fct_invoices_run >> stg_fct_invoices_test
stg_fct_invoices_test >> AWS_run_crawler_stg_fct_invoices
AWS_run_crawler_stg_fct_invoices >> fct_invoices







