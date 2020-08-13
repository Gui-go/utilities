# References
# https://superset.incubator.apache.org/installation.html

# recomenda-se rodar com sudo su antes 
mkdir /opt/superset

cp installation-superset/start-superset.sh /opt/superset

cd /opt/superset

sudo apt-get update

sudo apt-get install build-essential libssl-dev libffi-dev python3.6-dev python-pip libsasl2-dev libldap2-dev

pip install virtualenv

sudo apt-get install python3-venv

python3 -m venv venv
. venv/bin/activate

pip install --upgrade setuptools pip

# Install superset
pip install apache-superset

# Initialize the database
superset db upgrade

# Create an admin user (you will be prompted to set a username, first and last name before setting a password)
export FLASK_APP=superset
superset fab create-admin

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init

# To start a development web server on port 8088, use -p to bind to another port
superset run -p 8088 --with-threads --reload --debugger
