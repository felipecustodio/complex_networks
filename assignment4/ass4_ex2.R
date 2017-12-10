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


#### SIR MODEL ####
# states: S:0 I:1 R:2

## Parameters of the SIR model
mu = 1 # probability of recovering
beta = 0.4 # probability of transmission

targetnodes = seq(1,10) # node that will be used as the seed nodes
Tmax = 20
Ninf = matrix(0,nrow = length(targetnodes), ncol = Tmax) # matrix that stores the number of infected nodes at each time step
Nvac = matrix(0,nrow = length(targetnodes), ncol = Tmax) # matrix that stores the number of vaccinated nodes at each time step


# Ninf[i,t] yields the number of infected nodes at time t when the infection starts on i
for(i in targetnodes){
  # is the seed node
  vstates = matrix(0, nrow = N, ncol = 1)

  vstates[i] = 1
  vinfected = which(vstates %in% 1)
  t = 1

  #immunize
  #vaccinated random 10%
  #imm = sample(1:N, (0.1)* N)
  #vaccinated hubs 10%
  imm = (sort(degree(G), dec = T, index.return = T)$ix)[1:(0.1*N)]

  vstates[imm] = 2

  while(length(vinfected) > 0){ # while there are infected nodes
    vinfected = which(vstates %in% 1)
    # try to recover all infected nodes at step (t+1)
    for(j in vinfected){
      if(runif(1,0,1) <= mu){
        vstates[j] = 2
      }
    }
    # try to infect all the neighbors of infected nodes at step t
    for(j in vinfected){
      ng = neighbors(G, j)
      for(k in ng){
        if(runif(1,0,1) <= beta){
          if(vstates[k] == 0){# infect only susceptible nodes
            vstates[k] = 1
          }
        }
      }
    }
    Ninf[i, t] = length(which(vstates %in% 1))/N # store the fraction of infected nodes at time t
    Nvac[i, t] = length(which(vstates %in% 2))/N # store the fraction of infected nodes at time t

    #print(paste('t:', t, 'rhoi', length(which(vstates %in% 1))/N))
    t = t + 1
  }
}

rhoi = colMeans(Ninf) # average number if infected nodes from the result of each seed node
vacc = colMeans(Nvac) # average number if vaccinated nodes from the result of each seed node

#tesr = colMeans(vacc)
t = seq(1,length(rhoi)) # time steps
t2 = seq(1,length(vacc)) # time steps
#Fracao de infectados rhoi/ fracao de recuperados



#Plot simple -- fraction infected x Time and immunize x time
#plot(t2, vacc, xlab = "Time", ylab = "Fraction of infected nodes ER 10% imm hubs",
#     col = 'red', lwd=2,ylim = c(0,2), xlim = c(0,Tmax), pch = 21,  bg = "blue", type="o")
