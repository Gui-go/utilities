#0 Get into the gcloud project

#1 enable App Engine Admin API

#2 Start the App
gcloud app create
-> Select us-central or any other location you are interested

# Get the app into the gcloud environment
-> Open the Cloud Shell Editor
-> Write a simple python app there
-> install requirements
-> Specify app.yaml runtime
-> Save in a organized fashion 

# Deploy the app
gcloud app deploy app/app.yaml
-> press y to confirm and continue 

# Check the results
https://PROJECT_ID.uc.r.appspot.com

# Get some description of the app 
gcloud app describe

# If you need some logs
gcloud app logs tail

# To Stop/Desable the app go to the Console