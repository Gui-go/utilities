#!/bin/bash
apt update
apt -y install apache2
echo "Hello World, from my Engine Machine Virtual Machine $(hostname) $(hostname -i)" > /var/www/html/index.html