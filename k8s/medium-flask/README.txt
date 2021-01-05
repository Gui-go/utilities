docker build -t flasktry:v7 .

docker run -d -p 5000:5000 flasktry:v7

docker tag flasktry:v6 guigo-13/flasktry:v7

docker commit container_id guigo13/flasktry:v7

docker push guigo13/flasktry:v7

gcloud container clusters get-credentials try-gke-cluster-3 --zone us-central1-c --project try-gke-300201

git clone https://github.com/Gui-go/hello-k8s-gcp.git

cd hello-k8s-gcp/medium-flask

kubectl apply -f manifest.yaml

kubectl get svc
kubectl get svc -o yaml

kubectl get svc -o json | grep ip | cut -d ':' -f2 | cut -d '"' -f2 --output-delimiter=''

kubectl delete all --all



