closeAllConnections()
graphics.off()
rm(list=ls()) #clear all variables

library(igraph) # Load the igraph package

#### MODEL PARAMETERS ####
N = 1000; #number of nodes
av.dg = 8; #average degree
m = av.dg/2; # parameter of the BA model
q = 0.1 # rewiring probability in the WS model
p = av.dg/N # probability in the ER model

## MODELS ###
# BA network
#G <- barabasi.game(N, m = av.dg/2, directed = FALSE)
# # ER network
G <- erdos.renyi.game(N,p, type =c("gnp"))

grau = mean(degree(G))

print(paste(grau))
#### SIR MODEL - RUMOR ####
# states: S:0 I:1 R:2
## Parameters of the SIR model
mu = 1 # probability of recovering
beta = 0.4 # probability of transmission

targetnodes = seq(1,10) # node that will be used as the seed nodes
Tmax = 20
Ninf = matrix(0,nrow = length(targetnodes), ncol = Tmax) # matrix that stores the number of infected nodes at each time step
Nrec = matrix(0,nrow = length(targetnodes), ncol = Tmax)

recs = c()

for(i in targetnodes){
  # is the seed node
  vstates = matrix(0, nrow = N, ncol = 1)
  #print(paste('seed:', i))
  vstates[i] = 1
  vinfected = which(vstates %in% 1)
  t = 1
  #imm = sample(1:N, 10) #vaccination
  #vstates[imm] = 2
  while(length(vinfected) > 0){ # while there are infected nodes
    vinfected = which(vstates %in% 1)
    # try to infect all the neighbors of infected nodes at step t
    for(j in vinfected){
      ng = neighbors(G, j)
      for(k in ng){
        if(runif(1,0,1) <= beta){
          if(vstates[k] == 0){# infect only susceptible nodes
            vstates[k] = 1
          }else{
            if(runif(1,0,1) <= mu){# if the spreader meets an informed node, it can become stifler.
              vstates[j] = 2
              break
            }
          }
        }
      }
    }
    Ninf[i, t] = length(which(vstates %in% 1))/N # store the fraction of infected nodes at time t
    Nrec[i, t] = length(which(vstates %in% 2))/N # store the fraction of recupered nodes at time t

    #print(paste('t:', t, 'rhoi', length(which(vstates %in% 1))/N))
    t = t + 1
  }
  recs[i] = length(which(vstates %in% 2))/N
}

#Plots
#order = sort(x1, index.return = TRUE)$ix

rhoi = colMeans(Ninf)
frec = colMeans(Nrec)
#t = seq(1,length(rhoi)) # time steps

rec = mean(recs)






plot(grau, rec, xlab = "degree", ylab = "Fraction of infected nodes",
     col = 'red', lwd=2,ylim = c(0,0.2), xlim = c(0,Tmax), pch = 21,  bg = "blue", type="o")
