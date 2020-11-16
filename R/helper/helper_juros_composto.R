# rm(list = ls())
# gc()

# Juros Composto
juros_composto <- function(vp=NULL, vf=NULL, txj=NULL, n=NULL){
 if(is.null(vf)){
   res = vp * (1 + txj) ^ n
 } else
   if(is.null(vp)){
     res =  (((1 + txj) ^ n) / vf) ^ (1 / -1)
   } else
     if(is.null(txj)){
       res = (vf / vp) ^ (1 / n) - 1
     } else
       if(is.null(n)){
         res = log10(vf / vp) / log10(1 + txj)
       } else {res = '* * * Vc deve deixar o output desejado como nulo e preencher as demais variaveis * * *' }
 return(res)
}

# Juros Composto
juros_composto <- function(vf = NULL, vp = NULL, txj = NULL, n = NULL){
 lista=list(vp, vf, txj, n)
 dothis = c('vp', 'vf', 'txj', 'n')[sapply(lista, is.null)]
 if(length(dothis) != 1){dothis = 'erro'}
 switch(dothis,
        vp = { res =  (((1 + txj) ^ n) / vf) ^ (1 / -1) },
        vf = { res = vp * (1 + txj) ^ n },
        txj = { res = (vf / vp) ^ (1 / n) - 1 },
        n = {res = log10(vf / vp) / log10(1 + txj) },
        stop('* * * Vc deve deixar o output desejado como nulo e preencher as demais variaveis * * *') )
 return(res)
}

# Run it
juros_composto(vp=100, vf=NULL, txj=.1, n=2)
juros_composto(vp=NULL, vf=121, txj=.1, n=2)
juros_composto(vp=100, vf=121, txj=NULL, n=2)
juros_composto(vp=100, vf=121, txj=.1, n=NULL)
juros_composto(vp=100, vf=121, txj=.1, n=2)