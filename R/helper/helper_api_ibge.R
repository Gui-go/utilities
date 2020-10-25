# R-script 04-ibgeapi.R

# Setup -------------------------------------------------------------------
rm(list = ls())
gc()
options(stringsAsFactors = F)
theme_set(ggplot2::theme_minimal())

# Packages ----------------------------------------------------------------

if(!require("readr")){install.packages("readr")}
if(!require("plyr")){install.packages("plyr")}
if(!require("dplyr")){install.packages("dplyr")}
if(!require("ggplot2")){install.packages("ggplot2")}
if(!require("janitor")){install.packages("janitor")}
if(!require("sf")){install.packages("sf")}
if(!require("sp")){install.packages("sp")}
if(!require("st")){install.packages("st")}
if(!require("leaflet")){install.packages("leaflet")}
if(!require("mongolite")){install.packages("mongolite")}
if(!require("readxl")){install.packages("readxl")}
if(!require("janitor")){install.packages("janitor")}
if(!require("spdep")){install.packages("spdep")}
if(!require("vroom")){install.packages("vroom")}
if(!require("httr")){install.packages("httr")}
if(!require("jsonlite")){install.packages("jsonlite")}
if(!require("rgdal")){install.packages("rgdal")}

# API ---------------------------------------------------------------------
# Get everything
api_get <- GET(url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos")
api_content <- content(api_get, as = "text")
api_df <- fromJSON(api_content, flatten = TRUE)
# View(api_json)

# Ge everything related with this UF
UF = "SC"
url = paste0("https://servicodados.ibge.gov.br/api/v1/localidades/estados/", UF,"/distritos")
api_get <- GET(url = url)
api_content <- content(api_get, as = "text")
api_df <- fromJSON(api_content, flatten = TRUE)
# View(api_json)

# Malha 42
url_geojson = "http://servicodados.ibge.gov.br/api/v2/malhas/42?formato=application/vnd.geo+json"
api_get <- GET(url = url_geojson)
api_content <- content(x = api_get, as = "text", type = "geo+json", encoding = "UTF-8")
api_content_json <- toJSON(jsonlite::parse_json(api_content))
#
downloader::download(url = url_geojson, destfile = "/tmp/geojson.GeoJSON")
spatial_polygon <- readOGR(dsn = "/tmp/geojson.GeoJSON", layer = "OGRGeoJSON")
class(spatial_polygon)
plot(spatial_polygon)

# Testes
url1 = "https://servicodados.ibge.gov.br/api/v1/produtos/estatisticas"
url2 = "https://servicodados.ibge.gov.br/api/v3/calendario/"
url3 = "https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/-6/variaveis/616?localidades=N3[all]"
url4 = "http://servicodados.ibge.gov.br/api/v2/malhas/42"
url5 = "http://servicodados.ibge.gov.br/api/v2/malhas/42?formato=application/vnd.geo+json"
api_get <- GET(url = url5)
api_content <- content(x = api_get, as = "text", type = "json", encoding = "UTF-8")
api_df <- fromJSON(api_content, flatten = TRUE)
# View(api_df)




