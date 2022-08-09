





# To spin up a python server at port 3306
# 1:14:00 https://www.youtube.com/watch?v=lZAoFs75_cs&t=2s
# https://cursos.alura.com.br/forum/topico-usr-bin-python3-no-module-named-simplehttpserver-89637
python3 -m http.server 3306





# nslookup - query Internet name servers interactively
nslookup scame.nmap.org
nslookup 45.33.49.119 # by ip_address (scanme.nmap.org ip_address)
nslookup www.google.com
# Search for "who is <ip_address>"

# Wget - The non-interactive network downloader.
wget -qO- "http://wttr.in/" # -q quiet, O- returns stdout (Returns the wheather prediction as stdout on the terminal)



# route - show / manipulate the IP routing table
# sudo apt install net-tools
route -n 


# Returns the public IP address
curl https://ipinfo.io/ip


# nslookup - query Internet name servers interactively
# Check whether a DNS is taken (connected) or not
nslookup google.com
