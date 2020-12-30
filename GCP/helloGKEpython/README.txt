mkdir helloworld-gke
cd helloworld-gke

gcloud config get-value project

gcloud builds submit --tag gcr.io/gke-try/helloworld-gke .

gcloud container clusters create helloworld-gke \
   --num-nodes 1 \
   --enable-basic-auth \
   --issue-client-certificate \
   --zone southamerica-east1-a



