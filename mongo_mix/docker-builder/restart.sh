docker stop {container_name}
docker rm {container_name}
docker run -p 8080:8080 -d --name {container_name} {dockerhub_login}/{container_name}