


# Locate command file:
which aws

# Check version:
aws --version

# To check if the AWS CLI is configured with credentials:
aws configure list

# To configure AWS CLI
aws configure
# AWS Access Key ID [None]: Access Key ID
# AWS Secret Access Key [None]: Secret Access Key
# Default region name [None]: sa-east-1
# Default output format [None]: json

# Set an AWS profile and configure it:
export AWS_PROFILE=user2
aws configure

# The configuration settings are stored:
cat ~/.aws/credentials
cat ~/.aws/config

# Check info:
aws configure list-profiles # To list all your profile names
aws configure get region # To get the region set










