# Airflow

## Install Airflow container
* https://github.com/apache/airflow
```shell=
## Install 
$ sh auto_build.sh
$ docker exec -ti airflow bash
$ airflow webserver -p 8080
```

#export AIRFLOW_HOME="/opt/conda/lib/python3.7/site-packages/airflow/example_dags/"
export AIRFLOW_HOME="/opt/conda/lib/python3.7/site-packages/airflow/example_dags/"


![](https://i.imgur.com/A6TQ6IW.png)
* browser use localhost:30001
![](https://i.imgur.com/ejcejWj.png)


## ref
* https://kubernetes.io/blog/2018/06/28/airflow-on-kubernetes-part-1-a-different-kind-of-operator/
* https://getintodevops.com/blog/building-your-first-docker-image-with-jenkins-2-guide-for-developers
* https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+with+Docker
