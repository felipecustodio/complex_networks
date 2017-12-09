closeAllConnections()
graphics.off()
rm(list=ls()) #clear all variables

library(igraph) # Load the igraph package

#### MODEL PARAMETERS ####
N = 1000; #number of nodes
av.dg = 8; #average degree
m = av.dg/2; # parameter of the BA model
p = av.dg/N # probability in the ER model

# BA network
G <- barabasi.game(N, m = av.dg/2, directed = FALSE)
# # ER network
#G <- erdos.renyi.game(N,p, type =c("gnp"))
