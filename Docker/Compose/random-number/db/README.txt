
docker build -t postgres_image .

docker run -d --name postgres_container postgres_image

docker exec -it postgres_container psql -U guigo -a dbexample




____________________________________

# docker run -d --name postgis_container postgis_image

# docker exec -it postgis_container psql -U guigo -a dbexample -c 'CREATE EXTENSION IF NOT EXISTS postgis;'


ENV POSTGRES_PASSWORD=pgpasswd \
    POSTGRES_USER=guigo \
    POSTGRES_DB=dbexample \
    POSTGRES_HOME=/var/lib/postgresql