
# Build the image
docker build -t simple-nginx-gcp-image:v1 .

# test the image
docker run -d -p 80:80 --name simple-nginx-gcp-container simple-nginx-gcp-image:v1
curl localhost:80

# Tag the image
docker tag simple-nginx-gcp-image:v1 guigo-13/simple-nginx-gcp-image:v1

# Commit the image
docker commit simple-nginx-gcp-container guigo13/simple-nginx-gcp-image:v1

# Push the image to DockerHub
docker push guigo13/simple-nginx-gcp-image:v1

minikube start

kubectl create -f webserver.yaml

kubectl get pods
kubectl get pods --show-labels
kubectl get pods -L creation_method,env

kubectl expose pod web-server --type LoadBalancer --port 80 --target-port 80

kubectl logs web-server

kubectl delete pod web-server

kubectl delete all --all






