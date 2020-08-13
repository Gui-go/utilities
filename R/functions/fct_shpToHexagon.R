# Rscript - shpToHexagon.R

# Setup -------------------------------------------------------------------

rm(list = ls())
gc()

# Packages ----------------------------------------------------------------

if(!require(dplyr)){install.packages("dplyr")}
if(!require(ggplot2)){install.packages("ggplot2")}
if(!require(st)){install.packages("st")}
if(!require(sf)){install.packages("sf")}
if(!require(leaflet)){install.packages("leaflet")}

# Function ----------------------------------------------------------------

shpToHexagon <- function(shp, cellsize = 0.8, square = F, crs = 4326){
  hex <- sf::st_make_grid(
    shp, 
    cellsize = cellsize, 
    square = square
  ) %>% 
    base::data.frame(., sector = paste0("Hexágono ", 1:length(.))) %>% 
    sf::st_as_sf() %>% 
    sf::st_set_crs(crs)
  return(hex)
}

# Example -----------------------------------------------------------------

# SHP
shp <- sf::st_read("data/shp_data/br_unidades_da_federacao/BR_UF_2019.shp")
sc <- shp %>% dplyr::filter(SIGLA_UF == "SC")

hexsc <- shpToHexagon(sc, cellsize = .5)

plot(hexsc$geometry)
