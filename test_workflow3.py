# coding: utf-8

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# 定義參數
default_args = {
    'owner': 'Kevin',  # 擁有者名稱
    'start_date': datetime(2020, 2, 8, 9, 30),  # 第一次開始時間(格林威治)，為了方便測試，一般設置為當前時間減去執行週期
    #'email': ['kevin7674@gmail.com'],  # 接收通知的email列表
    #'email_on_failure': True,  # 是否在任務執行失敗時接收邮件
    #'email_on_retry': True,  # 是否在任務重試時接收邮件
    'retries': 1,  # 失敗重試次數
    'retry_delay': timedelta(seconds=60)  # 失敗重試間隔
}

# 定義DAG
dag = DAG(
    dag_id='test_flow3',  # dag_id
    default_args=default_args,  # 指定預設參數
    # schedule_interval="00, *, *, *, *"  # 執行周期，依次是分，時，天，月，年，此處表示每個整點執行
    schedule_interval=timedelta(minutes=5)  # Cronjob 執行周期，表示每分鐘執行一次
)

# 定義要執行的Python函數1
def task_1():
    current_time = str(datetime.today())
    with open('/usr/local/airflow/task_1.txt', 'a') as f:
        f.write('%s\n' % current_time)
    assert 1 == 1  # 可以在函数中使用assert斷言來判斷執行是否正常，也可以直接抛出異常行是否正常，也可以直接抛出異常

# 定義要執行的Python函數2
def task_2():
    current_time = str(datetime.today())
    with open('/usr/local/airflow/task_2.txt', 'a') as f:
        f.write('%s\n' % current_time)
    assert 1 == 2  # 可以在函数中使用assert斷言來判斷執行是否正常，也可以直接抛出異常行是否正常，也可以直接抛出異常
	
# 定義要執行的Python函數3
def task_3():
    current_time = str(datetime.today())
    with open('/usr/local/airflow/task_3.txt', 'a') as f:
        f.write('%s\n' % current_time)
		
# 定義要執行的Python函數4
def task_4():
    current_time = str(datetime.today())
    with open('/usr/local/airflow/task_4.txt', 'a') as f:
        f.write('%s\n' % current_time)
		
# 定義要執行的Python函數5
def task_5():
    current_time = str(datetime.today())
    with open('/usr/local/airflow/task_5.txt', 'a') as f:
        f.write('%s\n' % current_time)

# 定義要執行的task 1
t1 = PythonOperator(
    task_id='task_1',  # task_id
    python_callable=task_1,  # 指定要執行的函數
    dag=dag,  # 指定歸屬的dag
    retries=1,  # 重寫失敗重試次數,如果不寫,預設使用dag中default_args指定的設置。
)

# 定義要執行的task 2
t2 = PythonOperator(
    task_id='task_2',  # task_id
    python_callable=task_2,  # 指定要執行的函数
    dag=dag,  # 指定歸屬的dag
    retries=1,  # 重寫失敗重試次數,如果不寫,預設使用dag中default_args指定的設置。
)

# 定義要執行的的task 3
t3 = PythonOperator(
    task_id='task_3',  # task_id
    python_callable=task_3,  # 指定要執行的函数
    dag=dag,  # 指定歸屬的dag
)

# 定義要執行的的task 4
t4 = PythonOperator(
    task_id='task_4',  # task_id
    python_callable=task_4,  # 指定要執行的函数
    dag=dag,  # 指定歸屬的dag
)

# 定義要執行的的task 5
t5 = PythonOperator(
    task_id='task_5',  # task_id
    python_callable=task_5,  # 指定要執行的函数
    dag=dag,  # 指定歸屬的dag
)

#t2.set_upstream(t1)
# 表示t2這個任務只有在t1這個任務執行成功時才執行，
# 等同於 t1.set_downstream(t2)
# 同時等價於 dag.set_dependency('task_1', 'task_2')
t1 >> t2 

t2 >> t3
t2 >> t4

t4 >> t5
