docker stop mooongo_py
docker rm mooongo_py
docker run -p 8080:8080 -d --name mooongo_py koshi8bit/mooongo_py