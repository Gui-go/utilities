#!/usr/bin/env Rscript

print("hello world!")

"This is an executable R script"

"Run the command bellow to turn it executable"

print("chmod +x exec.R")

"With this command you can also use arguments"
"arg <- commandArgs(trailingOnly=T)"

arg <- commandArgs(trailingOnly=T)

print(paste0("arg[1] = ", arg[1]))
print(paste0("arg[2] = ", arg[2]))

print("Feels good to execute these R scripts :)")