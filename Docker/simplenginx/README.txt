

docker build -t html-nginx-image:v1 .

docker run -d -p 80:80 html-nginx-image:v1

curl localhost:80al