FROM tiangolo/python-machine-learning:python3.7

RUN pip install apache-airflow
RUN airflow initdb
#RUN airflow webserver -p 8080

EXPOSE 8080
