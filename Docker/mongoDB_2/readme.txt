
# docker-compose tips
# https://devhints.io/docker-compose


sudo docker-compose up -d

# Interact with its shell
docker exec -it mongo_ctn bash

cat /data/db/df.csv

# Import a csv into it
mongoimport -u "root" -p "passwd" --authenticationDatabase "admin" --type csv -d db_test -c col_test --headerline --drop /data/db/df.csv

mongo -u root -p passwd
mongosh -u root -p passwd

# criar user com somente permissao de leitura

show dbs
use db_test
show collections
db.col_test.find()



docker inspect mongo_ctn | grep IPAddress

mongodb://root:example@mongo:27017/db_test
mongodb://root:example@mongo:27017/db