library(igraph) # Load the igraph package

colors = c("chartreuse4", "chocolate1", "coral1", "darkred", "cadetblue", "darkorchid3", "coral1")
names = c("er", "ba", "ws0.001", "ws0.1", "ba0.5", "ba1.5", "ws0.05")



sir.immunize.model <- function(G, N = 1000, mu = 1, beta = 0.4, percent = 0.5, random = TRUE){
  #### SIR MODEL ####
  # states: S:0 I:1 R:2 M:3

  N.seeds = 10

  targetnodes = sample(1:N, N.seeds) # node that will be used as the seed nodes
  Tmax = 80
  Ninf = matrix(0,nrow = length(targetnodes), ncol = Tmax) # matrix that stores the number of infected nodes at each time step
  Nrec = matrix(0,nrow = length(targetnodes), ncol = Tmax) # matrix that stores the number of infected nodes at each time step

  # Ninf[i,t] yields the number of infected nodes at time t when the infection starts on i
  for(i in 1:length(targetnodes)){

    # is the seed node
    vstates = matrix(0, nrow = N, ncol = 1)

    if(random){
      vstates[sample(1:N, percent*N)] = 3 #Set the immunized nodes
    }else{
      nodes.idx = (sort(degree(G), dec = T, index.return = T)$ix)[1:(percent*N)]
      vstates[nodes.idx] = 3
    }

    print(paste('seed:', i))
    vstates[targetnodes[i]] = 1
    vinfected = which(vstates %in% 1)
    t = 1
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

      if(t > Tmax){
        Tmax = t
        Ninf = cbind(Ninf, rep(0,length(targetnodes)))
        Nrec = cbind(Nrec, rep(0,length(targetnodes)))

      }

      Ninf[i, t] = length(which(vstates %in% 1))/N # store the fraction of infected nodes at time t
      Nrec[i, t] = length(which(vstates %in% 2))/N # store the fraction of infected nodes at time t
      print(paste('t:', t, 'rhoi', length(which(vstates %in% 1))/N))
      t = t + 1
    }
  }

  rhoi = colMeans(Ninf) # average number if infected nodes from the result of each seed node
  rec = colMeans(Nrec) # average number if infected nodes from the result of each seed node

  t = seq(1,length(rhoi)) # time steps

  ret = list()
  ret$t = t
  ret$rhoi = rhoi
  ret$rec = max(rec)

  return (ret)
}

compare.sir <- function(Gs){
  #For SIR
  pdf(paste("./plots/sir_exercise1.pdf", sep=""))

  par(mfrow=c(2,3))

  for(i in 1:6){
    ret = sir.model(Gs[[names[i]]])
    plot.infecteds(ret$t, ret$rhoi, names[i], colors[i], length(ret$t), max(ret$rhoi))
  }

  dev.off()
}

exercise2 <- function(){

  N = 1000
  k.mean = 8
  m = k.mean/2

  n = c("ba", "er")

  Gs = list()

  Gs[[1]] = sample_pa(N, power = 1, m = m, directed = FALSE)
  Gs[[2]] = erdos.renyi.game(N, N*m, type = "gnm", directed = FALSE)

  xs = seq(0, 0.9, 0.1)

  random = matrix(0, nrow=2, ncol=length(xs))
  degree = matrix(0, nrow=2, ncol=length(xs))

  for(j in 1:length(xs)){

    pdf(paste("./plots/sir_immunization_", xs[j],".pdf", sep=""))

    par(mfrow=c(2,2))

    for(i in 1:2){
      ret = sir.immunize.model(Gs[[i]] , percent = xs[j])
      plot.infecteds(ret$t, ret$rhoi, n[i], colors[i], length(ret$t), max(ret$rhoi))

      random[i,j] = (ret$rec/N)


      ret = sir.immunize.model(Gs[[i]], percent = xs[j], random=FALSE)
      plot.infecteds(ret$t, ret$rhoi, n[i], colors[i], length(ret$t), max(ret$rhoi))

      degree[i,j] = (ret$rec/N)

    }

    dev.off()
  }

  pdf(paste("./plots/sir_immunization.pdf", sep=""))

    par(mfrow=c(2,2))

    plot(xs, random[1,], main = "BA (imunização aleatória)", xlab="Fração de Imunização", ylab="Fração de Recuperados", type="l", col = colors[1])
    plot(xs, random[2,], main = "ER (imunização aleatória)", xlab="Fração de Imunização", ylab="Fração de Recuperados", type="l", col = colors[2])
    plot(xs, degree[1,], main = "BA (imunização por grau)", xlab="Fração de Imunização", ylab="Fração de Recuperados", type="l", col = colors[3])
    plot(xs, degree[2,], main = "ER (imunização por grau)", xlab="Fração de Imunização", ylab="Fração de Recuperados", type="l", col = colors[4])

  dev.off()

}
