# settings
imagename="airflow:20200204"
containername="airflow"

docker stop $containername
docker rm $containername
docker build -t $imagename .
docker run -ti -d -p 30001:8080 \
	--name $containername \
	$imagename /bin/bash
	
docker exec -ti airflow bash
