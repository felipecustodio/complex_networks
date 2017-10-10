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
from math import sqrt
import sys
import powerlaw
from matplotlib import pyplot as pl


def read_graph(filename):
    graph = nx.Graph()
    with open(filename, 'rb') as f:
        for line in f:
            nodes = line.split()
            graph.add_edge(nodes[0], nodes[1])
    graph = graph.to_undirected()
    return graph


def draw_graph(graph):
    nx.draw(graph)
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
    distribution = sorted(degrees.values())
    return distribution


def is_scale_free(graph):

    distribution = degree_distribution(graph)
    distribution = [x for x in distribution if x != 0]

    np.seterr(divide='ignore', invalid='ignore')
    fit = powerlaw.Fit(distribution)
    coefficient = fit.power_law.alpha

    print("Coeficiente de distribuição de grau: %.4f" % (coefficient))
    if (coefficient >= 2 and coefficient <= 3):
        print("Rede livre de escala")
    else:
        print("Rede não é livre de escala")


def centrality_distribution(centrality):
    dists = {}
    for value in centrality.values():
        if value not in dists:
            dists[value] = 0
        dists[value] += 1
    return list(dists.values())


def centralities_histogram(graphs):
    i = 0
    # configurar gráfico
    for graph in graphs:
        fig, ((ax0, ax1), (ax2, ax3))  = pl.subplots(2, 2)  
        if (i == 0):
            ax0.set_title("Euroroad\nDistribuição das medidas de centralidade\n")
        if (i == 1):
            ax0.set_title("Hamster\nDistribuição das medidas de centralidade\n")
        if (i == 2):
            ax0.set_title("Powergrid\nDistribuição das medidas de centralidade\n")
        if (i == 3):   
            ax0.set_title("Airports\nDistribuição das medidas de centralidade\n")
        
        # medidas de centralidade
        betweenness_centrality = centrality_distribution(nx.betweenness_centrality(graph))
        closeness_centrality = centrality_distribution(nx.closeness_centrality(graph))
        eigenvector_centrality = centrality_distribution(nx.eigenvector_centrality(graph, max_iter=1000))
        pagerank = centrality_distribution(nx.pagerank(graph))

        # normalizar
        betweenness_centrality = [x/max(betweenness_centrality) for x in betweenness_centrality]
        closeness_centrality = [x/max(closeness_centrality) for x in closeness_centrality]
        eigenvector_centrality = [x/max(eigenvector_centrality) for x in eigenvector_centrality]
        pagerank = [x/max(pagerank) for x in pagerank]
        
        # plotar distribuições
        ax0.plot(betweenness_centrality, color='#FF7676', marker='None')
        ax0.set_xlabel('Betweenness Centrality')
        ax1.plot(closeness_centrality, color='#F6F49D', marker='None')
        ax1.set_xlabel('Closeness Centrality')
        ax2.plot(eigenvector_centrality, color='#5DAE8B', marker='None')
        ax2.set_xlabel('Eigenvector Centrality')
        ax3.plot(pagerank, color='#466C95', marker='None')
        ax3.set_xlabel('PageRank')

        pl.legend(loc='upper right')
        pl.subplots_adjust(hspace=0.5)
        pl.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

        # exibir e salvar
        if (i == 0):
            pl.savefig("euroroad_centralities.png")
        if (i == 1):
            pl.savefig("hamster_centralities.png")
        if (i == 2):
            pl.savefig("powergrid_centralities.png")
        if (i == 3):   
            pl.savefig("airports_centralities.png")
        pl.show()
        i += 1


def entropy(graph):
    entropy = 0
    distribution = degree_distribution(graph)

    for value in distribution:
        if value > 0:
            val = (value / graph.number_of_nodes())
            entropy -= (val) * math.log2(val)
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
    print("Diâmetro: %.1f" % (nx.diameter(graph)))


def shortest_paths_distribution(graph):
    lengths = nx.shortest_path_length(graph)
    frequences = {}
    # pegar todas as distancias entre todos os nós
    for source, targets in lengths.items():
        for target in targets:
            
            length = lengths[source][target]

            if length not in frequences:
                frequences[length] = 0
            frequences[length] += 1

    return list(frequences.values())


def shortest_paths_histograms(graphs):
    
    plot = pl.subplot()
    pl.title("Distribuição dos menores caminhos")

    dists = {}
    current = 0
    # encontrar distribuições
    for graph in graphs:
        dists[graph] = shortest_paths_distribution(graph)
        print("Found distribution for ", current)
        current += 1
        # normalizar
        dists[graph] = [x/sum(dists[graph]) for x in dists[graph]]

    # plotar distribuições
    x = np.linspace(0, nx.diameter(graphs[euroroad]) + 1, len(dists[euroroad]))
    plot.plot(x, dists[euroroad], color='#FF7676', marker='None', label='euroroad')
    x = np.linspace(0, nx.diameter(graphs[hamster]) + 1, len(dists[hamster]))
    plot.plot(x, dists[hamster], color='#F6F49D', marker='None', label='hamster')
    x = np.linspace(0, nx.diameter(graphs[powergrid]) + 1, len(dists[powergrid]))
    plot.plot(x, dists[powergrid], color='#5DAE8B', marker='None', label='powergrid')
    x = np.linspace(0, nx.diameter(graphs[airports]) + 1, len(dists[airports]))
    plot.plot(x, dists[airports], color='#466C95', marker='None', label='airports')
    
    # configurar visual do gráfico
    plot.spines['right'].set_visible(False)
    plot.spines['top'].set_visible(False)
    plot.yaxis.set_ticks_position('left')
    plot.xaxis.set_ticks_position('bottom')
    
    pl.xlabel('distância')
    pl.ylabel('probabilidade')

    pl.legend(loc='upper right')
    pl.subplots_adjust(hspace=0.5)
    
    # exibir e salvar
    pl.show()


def clustering_distribution(graph):
    coefficients = list((nx.clustering(graph)).values())
    dist = {}
    for value in coefficients:
        if value not in dist:
            dist[value] = 0
        dist[value] += 1
    return list(dist.values())


def clustering_histograms(graphs):
    plot = pl.subplot()
    pl.title("Distribuição acumulada do coeficiente de aglomeração local")

    dists = {}
    # encontrar distribuições
    for graph in graphs:
        dists[graph] = clustering_distribution(graph)
        # normalizar
        dists[graph] = [x/sum(dists[graph]) for x in dists[graph]]
        # fazer distribuição acumulada
        dists[graph] = np.cumsum(dists[graph])

    x = np.linspace(0, 1, len(dists[euroroad]))
    plot.plot(x, dists[euroroad], color='#FF7676',label='euroroad')
    x = np.linspace(0, 1, len(dists[hamster]))
    plot.plot(x, dists[hamster], color='#F6F49D',label='hamster')
    x = np.linspace(0, 1, len(dists[powergrid]))
    plot.plot(x, dists[powergrid], color='#5DAE8B',label='powergrid')
    x = np.linspace(0, 1, len(dists[airports]))
    plot.plot(x, dists[airports], color='#466C95',label='airports')

    # configurar visual do gráfico
    plot.spines['right'].set_visible(False)
    plot.spines['top'].set_visible(False)
    plot.yaxis.set_ticks_position('left')
    plot.xaxis.set_ticks_position('bottom')
    
    pl.xlabel('coeficiente de aglomeração local')
    pl.ylabel('probabilidade')

    pl.legend(loc='lower right')
    pl.subplots_adjust(hspace=0.5)
    
    # exibir e salvar
    pl.show()


def pearson(x, y):
    nx = len(x)
    ny = len(y)

    if nx != ny:
        print("TAMANHOS DIFERENTES")

    sum_x = sum([float(a) for a in x])
    sum_y = sum([float(b) for b in y])

    sum_xy = sum([a * b for a, b  in zip(x,y)])

    sum_x2 = sum([a ** 2 for a in x])
    sum_y2 = sum([b ** 2 for b in x])

    top = nx * sum_xy - (sum_x * sum_y)

    bottom_1 = (nx * sum_x2 - sum_x ** 2) ** .5
    bottom_2 = (ny * sum_y2 - sum_y ** 2) ** .5
    result = top / (bottom_1 * bottom_2)

    return result.real

def pearson_scatter(graphs):
    i = 0
    for graph in graphs:

        plot = pl.subplot()

        print("Calculando centralidades")
        # medidas de centralidade
        betweenness_centrality = list((nx.betweenness_centrality(graph)).values())
        closeness_centrality = list((nx.closeness_centrality(graph)).values())
        eigenvector_centrality = list((nx.eigenvector_centrality(graph, max_iter=1000)).values())
        pagerank = list((nx.pagerank(graph)).values())

        print("Calculando coeficientes de Pearson")
        
        c1 = (pearson(betweenness_centrality, closeness_centrality))
        c2 = (pearson(betweenness_centrality, eigenvector_centrality))
        c3 = (pearson(betweenness_centrality, pagerank))
        c4 = (pearson(closeness_centrality, eigenvector_centrality))
        c5 = (pearson(closeness_centrality, pagerank))
        c6 = (pearson(eigenvector_centrality, pagerank))

        coefficients = []
        coefficients.extend((c1,c2,c3,c4,c5,c6))
        for value in coefficients:
            if value > 0:
                print(value)

        print("Ordenar valores")
        sorted_coefficients = sorted(coefficients)

        # 0 = betweenness
        # 1 = closeness
        # 2 = eigenvector
        # 3 = pagerank

        if (sorted_coefficients[0] == c1):
            index_a = 0
            index_b = 1
        if (sorted_coefficients[0] == c2):
            index_a = 0
            index_b = 2
        if (sorted_coefficients[0] == c3):
            index_a = 0
            index_b = 3
        if (sorted_coefficients[0] == c4):
            index_a = 1
            index_b = 2
        if (sorted_coefficients[0] == c5):
            index_a = 1
            index_b = 3
        if (sorted_coefficients[0] == c6):
            index_a = 2
            index_b = 3

        # pegar medidas para serem plotadas e configurar legenda
        if (index_a == 0):
            a = betweenness_centrality
            label_a = "Betweenness Centrality"
        if (index_a == 1):
            a = closeness_centrality
            label_a = "Closeness Centrality"
        if (index_a == 2):
            a = eigenvector_centrality
            label_a = "Eigenvector Centrality"
        if (index_a == 3):
            a = pagerank
            label_a = "PageRank"

        if (index_b == 0):
            b = betweenness_centrality
            label_b = "Betweenness Centrality"
        if (index_b == 1):
            b = closeness_centrality
            label_b = "Closeness Centrality"
        if (index_b == 2):
            b = eigenvector_centrality
            label_b = "Eigenvector Centrality"
        if (index_b == 3):
            b = pagerank
            label_b = "PageRank"

        # scatter plot das duas medidas
        print("Configurando gráfico")
        # configurar título
        if (i == 0):
            pl.title("Euroroad\nMaiores centralidades por coeficiente de Pearson")
        if (i == 1):
            pl.title("Hamster\nMaiores centralidades por coeficiente de Pearson")
        if (i == 2):
            pl.title("Powergrid\nMaiores centralidades por coeficiente de Pearson")
        if (i == 3):   
            pl.title("Airports\nMaiores centralidades por coeficiente de Pearson")

        print("Plotando")
        # plotar
        pl.plot(a, color='#FF7676', linestyle='None', marker='o', label=label_a)
        pl.plot(b, color='#466C95', linestyle='None', marker='o', label=label_b)

        # configurar gráfico
        pl.legend(loc='upper right')
        pl.subplots_adjust(hspace=0.5)

        # configurar visual do gráfico
        plot.spines['right'].set_visible(False)
        plot.spines['top'].set_visible(False)
        plot.yaxis.set_ticks_position('left')
        plot.xaxis.set_ticks_position('bottom')

        # exibir e salvar
        if (i == 0):
            pl.savefig("euroroad_pearson.png")
        if (i == 1):
            pl.savefig("hamster_pearson.png")
        if (i == 2):
            pl.savefig("powergrid_pearson.png")
        if (i == 3):   
            pl.savefig("airports_pearson.png")
        pl.show()
        i += 1




# # set python to print to file
# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f

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

# histograms
# shortest_paths_histograms(giants)
# clustering_histograms(giants)
# centralities_histogram(giants)

# pearson
pearson_scatter(giants)

# measures

# print("---------------------")
# print("EuroRoad")
# measures(giants[euroroad])
# print("Entropia de Shannon: %.4f" % (entropy(giants[euroroad])))
# is_scale_free(giants[euroroad])
# print("---------------------")

# print("Hamster")
# measures(giants[hamster])
# print("Entropia de Shannon: %.4f" % (entropy(giants[hamster])))
# is_scale_free(giants[hamster])
# print("---------------------")

# print("Powergrid")
# measures(giants[powergrid])
# print("Entropia de Shannon: %.4f" % (entropy(giants[powergrid])))
# is_scale_free(giants[powergrid])
# print("---------------------")

# print("Airports")
# measures(giants[airports])
# print("Entropia de Shannon: %.4f" % (entropy(giants[airports])))
# is_scale_free(giants[airports])
# print("---------------------")

# close file
# sys.stdout = orig_stdout
# f.close()