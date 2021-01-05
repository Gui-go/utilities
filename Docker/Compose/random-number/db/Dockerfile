FROM postgres:latest

LABEL maintainer="guilhermeviegas1993@gmail.com"

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install postgis -y

ENV POSTGRES_PASSWORD=secret \
    POSTGRES_USER=username \
    POSTGRES_DB=database \
    POSTGRES_HOME=/var/lib/postgresql

# COPY init.sql /docker-entrypoint-initdb.d/
# COPY ./ ${PG_APP_HOME}/
# VOLUME . /myvol
COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432

WORKDIR ${POSTGRES_HOME}
