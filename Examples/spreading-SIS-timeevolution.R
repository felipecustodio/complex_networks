closeAllConnections()
graphics.off()
rm(list=ls()) #clear all variables
set.seed(101) #start the random seed

# set the working directory
#setwd("~/Dropbox/0Programs/R/Networks/Epidemics")

library(igraph) # Load the igraph package
#get( getOption( "device" ) )()

#### MODEL PARAMETERS ####
N = 1000; #number of nodes
av.dg = 8; #average degree
m = av.dg/2; # parameter of the BA model
q = 0.1 # rewiring probability in the WS model
p = av.dg/N # probability in the ER model

## MODELS ###
# BA network
G <- barabasi.game(N, m = av.dg/2, directed = FALSE)
str = "BA"
#G <- sample_pa(N, power = 1, m = av.dg/2)
# # ER network
#G <- erdos.renyi.game(N,p, type =c("gnp"))
#str = "ER"
# # WS network
#G <- sample_smallworld(dim=1,size=N, nei = av.dg/2, p = q)
#str = "WS"
# ###### READ FROM FILE ####
#net <- read.table("test-star.txt")
#G <- graph.data.frame(net, directed=FALSE)
#plot(G, layout=layout.kamada.kawai, vertex.color="green")

#G <- make_graph("Zachary") # you can use the Zachary karate club network to test

#### SIS MODEL ####
# states: S:0 I:1
## Parameters of the SIS model
Tmax = 50; # maximum number of iterations in the SIS model
mu = 1 # probability of recovering
beta = 0.2 # probability of transmission

targetnodes = seq(1,N) # node that will be used as the seed nodes
Ninf = matrix(0,nrow = length(targetnodes), ncol = Tmax) # matrix that stores the number of infected nodes at each time step
# Ninf[i,t] yields the number of infected nodes at time t when the infection starts on i
for(i in targetnodes){
  # is the seed node
  vstates = matrix(0, nrow = N, ncol = 1)
  #print(paste('seed:', i))
  vstates[i] = 1
  for(t in 1:Tmax){
    vinfected = which(vstates %in% 1)
    # try to recover all infected nodes at step (t+1)
    for(j in vinfected){
      if(runif(1,0,1) <= mu){
        vstates[j] = 0
      }
    }
    # try to infect all the neighbors of infected nodes at step t
    for(j in vinfected){
      ng = neighbors(G, j)
      for(k in ng){
        if(runif(1,0,1) < beta){
          if(vstates[k] == 0){# infect only susceptible nodes
            vstates[k] = 1
          }
        }
      }
    }
    Ninf[i, t] = length(which(vstates %in% 1))/N # store the fraction of infected nodes at time t
    #print(length(which(vstates %in% 1))/N)
  }
}
rhoi = colMeans(Ninf) # average number if infected nodes from the result of each seed node
t = seq(1,length(rhoi)) # time steps
plot(t, rhoi, xlab = "Time", ylab = "Fraction of infected nodes SIS BA",
     col = 'blue', lwd=2, xlim = c(0,Tmax), pch = 21,  bg = "blue", type="o")
