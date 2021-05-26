FROM openanalytics/r-base

MAINTAINER "guilhermeviegas1993@gmail.com"

# system libraries of general use
RUN apt-get update && apt-get install -y \
    sudo \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    libssl-dev \
    libssh2-1-dev \
    libssl1.0.0 \
    xorg-dev \
    libxml2-dev \
    libmpfr-dev \
    htop \
    nano \
    openjdk-8-jre \
    libmagick++-dev \
    cargo \
    libudunits2-dev \
    libgdal-dev \
    python-pip \
    python3-pip \
    libmagick++-dev


# system library dependency for the euler app
RUN apt-get update && apt-get install -y \
    libmpfr-dev

# basic shiny functionality
RUN R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cloud.r-project.org/')"

# install dependencies of the euler app
RUN R -e "install.packages('Rmpfr', repos='https://cloud.r-project.org/')"

# basic R packages
RUN R -e "install.packages(c('XML', 'devtools', 'dplyr'))"
RUN R -e "install.packages(c('readr', 'xtable'))"

# additional R packages
RUN R -e "install.packages('shinyjs')"
RUN R -e "install.packages('arules')"
RUN R -e "install.packages('shinydashboard')"
RUN R -e "install.packages('shinycssloaders')"
RUN R -e "install.packages('shinyWidgets')"
RUN R -e "install.packages('devtools')"
RUN R -e "install.packages('tidyverse')"
RUN R -e "install.packages('sparklyr')"
RUN R -e "install.packages('rio')"
RUN R -e "install.packages('plyr')"
RUN R -e "install.packages('janitor')" 
RUN R -e "install.packages('bit64')"
RUN R -e "install.packages('DT')"

# chart R packages
RUN R -e "install.packages(c('googleVis','ggplot2'))"

# copy the app to the image
RUN mkdir /root/apps
COPY apps /root/apps

COPY Rprofile.site /usr/lib/R/etc/

EXPOSE 3838

CMD ["R", "-e", "shiny::runApp('/root/apps')"]


