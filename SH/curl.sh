





# Lists the files within the ftp server of the PDET
# MINISTÉRIO DO TRABALHO
# PDET - PROGRAMA DE DISSEMINAÇÃO DAS ESTATÍSTICAS DO TRABALHO
# http://pdet.mte.gov.br/microdados-rais-e-caged

curl ftp://ftp.mtps.gov.br/pdet/microdados/

curl ftp://ftp.mtps.gov.br/pdet/microdados/CAGED/2019/

curl ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/

# To get information about a file:
curl -I ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_SUL.7z
curl -I www.google.com
curl -I http://www.google.com/

# Download the file with the same name as remote/original
curl ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_SUL.7z -O

# Download file with new name (outputName)
curl ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/RAIS_VINC_PUB_SUL.7z -o outputName