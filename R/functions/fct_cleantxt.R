cleantxt <- function(text){
  text <- iconv(text, to='ASCII//TRANSLIT')
  text <- gsub("[^[:alnum:]]", "", text)
  text <- gsub(" ", "", text)
  text <- tolower(text)
  return(text)
}