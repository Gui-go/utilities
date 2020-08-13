labs <- function(df, var_selected){
  lab <- paste0("<b>UF: </b>", as.character(df[["var1"]]), "<br/>", 
                "<b>Região: </b>", as.character(df[["var2"]]), "<br/>",
                "<b>Nome do Estado: </b>", as.character(df[["var1"]]), "<br/>",
                "<b>Estatístiva: </b>", as.character(df[[var_selected]]))
  return(lab)
}