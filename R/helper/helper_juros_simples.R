# rm(list = ls())
# gc()

# Juros Simples
juros_simples <- function(vp = NULL, vf = NULL, txj = NULL){
 if(is.null(vf)){
   res = (1 + txj) * vp
 } else
   if(is.null(vp)){
     res = vf * (1 + txj) ^ (1 / -1)
   } else
     if(is.null(txj)){
       res = (vf / vp) - 1
     } else {res = '* * * Vc deve deixar o output desejado como nulo e preencher as demais variaveis* * *'}
 
 return(res)
}

# Juros Simples
juros_simples <- function(vp = NULL, vf = NULL, txj = NULL){
 lista=list(vp, vf, txj)
 dothis = c('vp', 'vf', 'txj')[sapply(lista, is.null)]
 if(length(dothis) != 1){dothis = 'erro' }
 switch(dothis,
        vp = {res <- vf * (1 + txj) ^ (1 / -1) },
        vf = {res <- (1 + txj) * vp },
        txj = {res = (vf / vp) - 1 },
        stop('* * * Vc deve deixar o output desejado como nulo e preencher as demais variaveis* * *') )
 return(res)
}

# Run it
juros_simples(vp=100, vf=NULL, txj=.1)
juros_simples(vp=NULL, vf=110, txj=.1)
juros_simples(vp=100, vf=110, txj=NULL)
juros_simples(vp=100, vf=110, txj=.1)
