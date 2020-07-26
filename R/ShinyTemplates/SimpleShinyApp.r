# R script - Simplest Shiny App

# Setup -------------------------------------------------------------------
# rm(list = ls())
gc()
options(encoding = "UTF-8", stringsAsFactors = F)

# UI ----------------------------------------------------------------------
ui <- fluidPage(
  h1("Hello Shiny!")
)
# Server ------------------------------------------------------------------
server <- function(input, output) {}
# App ---------------------------------------------------------------------
shinyApp(ui, server)