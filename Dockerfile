FROM tiangolo/python-machine-learning:python3.7

RUN pip install apache-airflow
RUN airflow initdb

RUN mkdir /root/airflow/dags
COPY dagbag.py /root/airflow/dags

#RUN airflow webserver -p 8080

EXPOSE 8080
