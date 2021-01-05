
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

# Fetch a kubeconfig to entry the cluster
gcloud container clusters get-credentials try-gke-cluster-2 --zone us-central1-c

# Apply both service and deployment through the same manifest.yaml
kubectl apply -f manifest.yaml

# Now there should be a service running
kubectl get services
kubectl get services -o yaml

# You can now curl to
kubectl get services -o json | grep ip | cut -d ':' -f2 | cut -d '"' -f2 --output-delimiter=''

# Delete everything in your way out
kubectl delete all --all

