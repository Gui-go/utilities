



# To lounch interactive gcloud console
gcloud beta interactive

# Get list of all projects
gcloud projects list

# To get current project
gcloud config get-value project

# To delete gcp project
gcloud projects delete PROJECT_ID

# To restore/undelete gcp project
gcloud projects undelete PROJECT_ID

# Set new project
gcloud config set project PROJECT_ID

# To get project number
gcloud projects list \
--filter="project_id:$PROJECT" \
--format="value(project_number)"

# To check whether the billing is enabled
gcloud beta billing projects describe \
$(gcloud config get-value project) \
--format="value(billingEnabled)"

# To get authentity token
gcloud auth print-identity-token

# To check locally gcp unathorized curl
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
https://myapp-123_APPCODE_321.a.run.app

# To list all verified domains
gcloud domains list-user-verified

# Mapping a domain to a service
gcloud beta run domain-mappings create --service SERVICE --domain DOMAIN

