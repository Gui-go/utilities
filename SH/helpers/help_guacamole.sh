#!/bin/bash


# https://guacamole.apache.org/doc/gug/users-guide.html
# https://hub.docker.com/r/guacamole/guacamolels

docker run \
  -p 8080:8080 \
  -v /Documents/docker_dir/guac_test:/config \
  guacamole/guacamole

docker run \
  -p 8080:8080 \
  -v /Documents/docker_dir/guac_test:/config \
  -d oznu/guacamole



# Protocols

# SSH
# default port: 22


# RDP

# VNC (RDP for linux os) for accessing grafical interfaces
# default port: 5901