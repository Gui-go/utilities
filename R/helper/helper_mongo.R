# R helper for connecting into MongoDB with R

# Libraries ---------------------------------------------------------------
library(mongolite)

# All collections
mongo(url = "mongodb+srv://USER:PASSWORD@cluster0-vckod.gcp.mongodb.net/test?retryWrites=true&w=majority")$run('{"listCollections":1}')$cursor$firstBatch %>% as_tibble()

# Metadata on a collection
db = mongo(collection = "collection1", url = "mongodb+srv://USER:PASSWORD@cluster0-vckod.gcp.mongodb.net/test?retryWrites=true&w=majority")

# Finding the data
data <- db$find()