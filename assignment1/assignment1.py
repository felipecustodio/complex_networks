#!/bin/usr/env python3
# -*- coding: utf-8 -*-

'''
Dynamical Processes in Complex Networks
University of Sao Paulo
Professor Francisco Aparecido Rodrigues

Students: 
Felipe Scrochio Custódio - 9442688
Gabriel Henrique Scalici - 9292970


Assignment 1 - Complex Networks caracterization
'''

import networkx as nx
import numpy as np
import math
import sys
import powerlaw
from matplotlib import pyplot as pl


def read_graph(filename):
    graph = nx.Graph()
    with open(filename, 'rb') as f:
        for line in f:
            nodes = line.split()
            graph.add_edge(nodes[0], nodes[1])
    return graph


def draw_graph(graph):
    nx.draw(graph)
    # pl.savefig(filename)
    pl.show()


def stat_moment(graph, moment):
    measure = 0
    for node in graph.nodes_iter():
        measure += graph.degree(node) ** moment
    return measure / graph.number_of_nodes()


def giant_component(graph):
    return nx.Graph(max(nx.connected_component_subgraphs(graph), key=len))


def degree_distribution(graph):
    degrees = {}
    for node in graph.nodes_iter():
        degree = graph.degree(node)
        if degree not in degrees:
            degrees[degree] = 0
        degrees[degree] += 1
    distribution = sorted(degrees.items())
    return distribution


def is_scale_free(graph):
    distribution = np.asarray(degree_distribution(graph))
    # fit = powerlaw.Fit(distribution)]
    fit = powerlaw.Fit(distribution)
    exponent = fit.power_law.alpha
    if (exponent >= 2 and exponent <= 3):
        return True
    else:
        return False


def centralities(graph):
    # medidas de centralidade
    betweenness_centrality = nx.betweenness_centrality(graph)
    closeness_centrality = nx.closeness_centrality(graph)
    eigenvector_centrality = nx.eigenvector_centrality(graph)
    pagerank = nx.pagerank(graph)


def entropy(graph):
    entropy = 0
    distribution = degree_distribution(graph)
    for value in distribution:
        if value[1] > 0:
            entropy += value[1] * math.log2(value[1])
    return entropy


def average_degree(graph):
    degrees = graph.degree().values()
    average = sum(degrees)/len(degrees)
    return average


def measures(graph):
    print("MEDIDAS")
    print("Número de vértices: ",len(graph))
    print("Grau médio: %.4f" % (average_degree(graph)))
    print("Segundo momento da distribuição do grau: %.4f" % (stat_moment(graph, 2)))
    print("Média do coef. de aglomeração local: %.4f" % (nx.average_clustering(graph)))
    print("Transitividade: %.4f" % (nx.transitivity(graph)))
    print("Média dos menores caminhos: %.4f" % (nx.average_shortest_path_length(graph)))
    print("Diâmetro: %.4f" % (nx.diameter(graph)))

def shortest_paths_distribution(graph):
    pass

def shortest_paths_histograms(graphs):
    
    plot = pl.subplot()
    pl.title("Distribuição dos menores caminhos")

    dists = {}
    # encontrar distribuição
    for graph in graphs:
        dists[graph] = shortest_paths_distribution(graph)
 
    # plotar distribuições em escala log
    plot.loglog(dists[euroroad], color='#D45C7E', marker='None', label='euroroad')
    plot.loglog(dists[hamster], color='#C9533E', marker='None', label='hamster')
    plot.loglog(dists[powergrid], color='#45415C', marker='None', label='powergrid')
    plot.loglog(dists[airports], color='#DC7B28', marker='None', label='airports')
    
    # configurar visual do gráfico
    plot.spines['right'].set_visible(False)
    plot.spines['top'].set_visible(False)
    plot.yaxis.set_ticks_position('left')
    plot.xaxis.set_ticks_position('bottom')
    
    pl.xlabel('distância')
    pl.ylabel('frequência')

    pl.legend(loc='upper right')
    pl.subplots_adjust(hspace=0.5)
    
    # exibir e salvar
    pl.show()
    # pl.savefig("shortest_paths_histograms.png")


def clustering_distribution(graph):
    pass

def clustering_histograms(graphs):
    plot = pl.subplot()
    pl.title("Distribuição acumulada do coeficiente de aglomeração local")

    dists = {}
    # encontrar distribuição
    for graph in graphs:
        dists[graph] = clustering_distribution(graph)

    # plotar distribuições em escala log
    plot.loglog(dists[euroroad], color='#D45C7E', marker='None', label='euroroad')
    plot.loglog(dists[hamster], color='#C9533E', marker='None', label='hamster')
    plot.loglog(dists[powergrid], color='#45415C', marker='None', label='powergrid')
    plot.loglog(dists[airports], color='#DC7B28', marker='None', label='airports')

    # configurar visual do gráfico
    plot.spines['right'].set_visible(False)
    plot.spines['top'].set_visible(False)
    plot.yaxis.set_ticks_position('left')
    plot.xaxis.set_ticks_position('bottom')
    
    pl.xlabel('coeficiente de aglomeração local')
    pl.ylabel('frequência')

    pl.legend(loc='upper right')
    pl.subplots_adjust(hspace=0.5)
    
    # exibir e salvar
    pl.show()
    # pl.savefig("clustering_histograms.png")


def pearson(measures):
    pass
    # scatter plots


# set python to print to file
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

# read networks
euroroad = read_graph("./networks/euroroad.txt")
hamster = read_graph("./networks/hamster.txt")
powergrid = read_graph("./networks/us-powergrid.txt")
airports = read_graph("./networks/us-airports.txt")

graphs = []
graphs.append(euroroad)
graphs.append(hamster)
graphs.append(powergrid)
graphs.append(airports)

# get biggest component
giants = {}
for graph in graphs:
    giants[graph] = giant_component(graph)

# shortest_paths_histograms(giants)
# clustering_histograms(giants)

# measures
print("---------------------")
print("EuroRoad")
measures(giants[euroroad])
print("Entropia de Shannon: %.4f" % (entropy(giants[euroroad])))
print("---------------------")

print("Hamster")
measures(giants[hamster])
print("Entropia de Shannon: %.4f" % (entropy(giants[hamster])))
print("---------------------")

print("Powergrid")
measures(giants[powergrid])
print("Entropia de Shannon: %.4f" % (entropy(giants[powergrid])))
print("---------------------")

print("Airports")
measures(giants[airports])
print("Entropia de Shannon: %.4f" % (entropy(giants[airports])))
print("---------------------")


# close file
sys.stdout = orig_stdout
f.close()