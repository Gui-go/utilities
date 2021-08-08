

# install.packages("mongolite")
# mongo_set <- mongolite::mongo(db = "db_test", collection = "colec_test", url = "mongodb://root:passwd@172.21.0.1", verbose = TRUE)
# mongo_set$find()
# df <-data.frame(a=c(1:9), b=c(9:1))
# mongo_set$insert(df)
# try(mongo_set <- mongolite::mongo(db = "db_test", collection = "colec_test", url = "mongodb://root:passwd@172.21.0.1", verbose = TRUE))

library(shiny)
library(ggplot2)
library(mongolite)

ui <- shiny::fluidPage(
  shiny::h2("Hello"),
  shiny::uiOutput(outputId = "output_ui_1")
)

server <- function(input, output) {
  
  mongo_set <- mongolite::mongo(db = "db_test", collection = "colec_test", url = "mongodb://root:passwd@172.21.0.1", verbose = TRUE)
  df <- mongo_set$find()

  output$output_ui_1 <- renderPrint({
    df
  })
}

shiny::shinyApp(ui, server)
