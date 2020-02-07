# coding: utf-8

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# 定義參數
default_args = {
    'owner': 'Kevin',  # 擁有者名稱
    'start_date': datetime(2020, 2, 6, 16, 00),  # 第一次開始時間(格林威治)，為了方便測試，一般設置為當前時間減去執行週期
    'email': ['kevin7674@gmail.com'],  # 接收通知的email列表
    'email_on_failure': True,  # 是否在任務執行失敗時接收邮件
    'email_on_retry': True,  # 是否在任務重試時接收邮件
    'retries': 3,  # 失敗重試次數
    'retry_delay': timedelta(seconds=5)  # 失敗重試間隔
}

# 定義DAG
dag = DAG(
    dag_id='hello_world',  # dag_id
    default_args=default_args,  # 指定預設參數
    # schedule_interval="00, *, *, *, *"  # 執行周期，依次是分，時，天，月，年，此處表示每個整點執行
    schedule_interval=timedelta(minutes=1)  # 執行周期，表示每分鐘執行一次
)

# 定義要執行的Python函數1
def hello_world_1():
    current_time = str(datetime.today())
    with open('/root/tmp/hello_world_1.txt', 'a') as f:
        f.write('%s\n' % current_time)
    assert 1 == 1  # 可以在函数中使用assert斷言來判斷執行是否正常，也可以直接抛出異常行是否正常，也可以直接抛出異常

# 定義要執行的Python函數2
def hello_world_2():
    current_time = str(datetime.today())
    with open('/root/tmp/hello_world_2.txt', 'a') as f:
        f.write('%s\n' % current_time)

# 定義要執行的Python函數3
def hello_world_3():
    current_time = str(datetime.today())
    with open('/root/tmp/hello_world_3.txt', 'a') as f:
        f.write('%s\n' % current_time)

# 定義要執行的task 1
t1 = PythonOperator(
    task_id='hello_world_1',  # task_id
    python_callable=hello_world_1,  # 指定要執行的函數
    dag=dag,  # 指定歸屬的dag
    retries=2,  # 重寫失敗重試次數,如果不寫,預設使用dag中default_args指定的設置。
)

# 定義要執行的task 2
t2 = PythonOperator(
    task_id='hello_world_2',  # task_id
    python_callable=hello_world_2,  # 指定要執行的函数
    dag=dag,  # 指定歸屬的dag
)

# 定義要執行的的task 3
t3 = PythonOperator(
    task_id='hello_world_3',  # task_id
    python_callable=hello_world_3,  # 指定要執行的函数
    dag=dag,  # 指定歸屬的dag
)

t2.set_upstream(t1)
# 表示t2這個任務只有在t1這個任務執行成功時才執行，
# 等同於 t1.set_downstream(t2)
# 同時等價於 dag.set_dependency('hello_world_1', 'hello_world_2')

t3.set_upstream(t1)  # 同理
