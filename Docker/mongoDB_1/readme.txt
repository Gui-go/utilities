

sudo apt update && sudo apt upgrade -y

sudo systemctl status docker

sudo docker search mongodb

# Build mongodb image
docker build . -t mongodb:v20210808

# Run mongodb container 
docker run --rm --name mongodb_ctn -d -v $(pwd)/volume/:/data/db -p 27017:27017 mongodb:v20210808

# Interact with its shell
docker exec -it mongodb_ctn bash

# Import a csv into it
mongoimport --type csv -d db_test -c col_test --headerline --drop /data/db/df.csv

# Run mongo
mongo

# Show databases
show dbs

# Use a DB
use db_test

# Show all collections
show collections

# Show all users
show users

# Show all roles
show roles

# Show all profiles
show profile

# Show all databases
show databases

# load(db.auth())

# Find values 
db.col_test.find()