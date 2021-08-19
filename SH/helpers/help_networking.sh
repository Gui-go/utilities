# Network commands


# ip - show / manipulate routing, network devices, interfaces and tunnel
ip address  # windowns
ifconfig

# ifconfig - configura uma interface de rede
# ifconfig é usado para configurar (e posteriormente manter) as interfaces de rede. É usado durante o boot para configurar  a maioria   delas  para  um  estado  usável.  Depois  disto,  é normalmente somente necessário durante depurações  ou  quando for necessária uma configuração fina do sistema.
# Se  nenhum argumento for informado, ifconfig somente mostra o estado  das  interfaces  correntemente   definidas.   Se   um argumento  interface  for  informado,  ele  mostra  somente o estado da interface informada. De outra forma ele assume  que os parâmetros devem ser configurados.
ifconfig

# iwconfig - configure a wireless network interface
iwconfig


# ping - send ICMP ECHO_REQUEST to network hosts
ping
ping www.google.com
ping www.google.com -c 1 | grep "64 bytes" | cut -d " " -f 5 | tr -d "():" # -f 5 (para versão em pt)

# arp - manipula o cache ARP do sistema
arp -a 

# netstat - Mostra conexões de rede, tabelas de roteamento, estatísticas de interface e conexões mascaradas.
netstat -ano # checks every open port
netstat -ano | grep 8787 # check whether port 8787 is been used
netstat -ano | sort -k 5 # check all used port ordered by port



# route - mostra / manipula a tabela de roteamento IP
route


# nmap - Ferramenta de exploração de rede e segurança / scanner de portas
nmap scanme.nmap.org


