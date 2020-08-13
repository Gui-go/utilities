# Shell script for creating a docker with PostgreSQL and PostGIS

# Instalar o PostgreSQL
docker run -p 5432:5432 -d \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=db-example \
    -v pgdata:/var/lib/postgresql/data \
    --name postgres-gis-docker \
    postgres

docker run -i postgres apt-get update | echo helloooooooooo

# docker exec -it postgres-gis-docker psql -U postgres db-example | apt-get update | apt-get upgrade | apt-get install postgis

