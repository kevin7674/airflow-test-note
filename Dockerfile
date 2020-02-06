FROM tiangolo/python-machine-learning:python3.7

RUN pip install apache-airflow
RUN airflow initdb

RUN mkdir /root/airflow/dags
RUN chmod 777 /root/airflow/dags
COPY dagbag.py /root/airflow/dags
COPY test_hello.py /root/airflow/dags
COPY airflow.cfg /root/airflow
#COPY test.py /opt/conda/lib/python3.7/site-packages/airflow/example_dags/test.py

#RUN airflow webserver -p 8080

EXPOSE 8080
