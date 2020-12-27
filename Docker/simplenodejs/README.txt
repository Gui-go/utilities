
docker build -t kubia .

docker run --name kubia-container -p 8080:8080 -d kubia

docker stop kubia-container

docker rm kubia-container