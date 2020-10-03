# R Script - vis_correlation_matrix.R
# Matrix de correlação

# Setup
if(!require("GGally")){install.packages("GGally")}
if(!require("ggfortify")){install.packages("ggfortify")}

# Example
ggpairs(mtcars, upper = list(continuous = wrap("cor", size = 6)))+
  labs(title = "Matriz de correlação")+
  theme_gray()+
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        strip.text = element_text(size = 10, face = "bold"))
