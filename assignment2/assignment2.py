#!/bin/usr/env python3
# -*- coding: utf-8 -*-

'''
Dynamical Processes in Complex Networks
University of Sao Paulo
Professor Francisco Aparecido Rodrigues

Students: 
Felipe Scrochio Custódio - 9442688
Gabriel Henrique Scalici - 9292970


Assignment 2 - Correlation and Communities
'''

import networkx as nx
import igraph as ig

from itertools import *

import numpy as np
from matplotlib import pyplot as pp
import seaborn as sns

from subprocess import call

# plot colors
colors = ["#1abc9c", "#2ecc71", "#3498db", "#f1c40f", "#e67e22", "#e74c3c"]

def pearson(x, y):
    n = len(x)
    sum_x = float(sum(x))
    sum_y = float(sum(y))
    sum_x_sq = sum(map(lambda x: pow(x, 2), x))
    sum_y_sq = sum(map(lambda x: pow(x, 2), y))
    psum = sum(map(lambda x, y: x * y, x, y))
    num = psum - (sum_x * sum_y/n)
    den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
    if den == 0: return 0
    return num / den


def giant_component(graph):
    return nx.Graph(max(nx.connected_component_subgraphs(graph), key=len))


def read_graph(filename):
    graph = nx.Graph()
    with open(filename, 'rb') as f:
        for line in f:
            nodes = line.split()
            graph.add_edge(nodes[0], nodes[1])
    graph = graph.to_undirected()
    return giant_component(graph)


def nx_to_ig(graph):
    g = ig.Graph.TupleList(graph.edges(), directed=False)
    return g


def assortativity(graphs):
    print("ASSORTATIVITY")
    for name,graph in graphs.items():
        assortativity = nx.degree_assortativity_coefficient(graph)
        print("%s: %.4f" % (name, assortativity))


def k_x_knn(graphs):
    print("K X KNN")
    i = 0
    for name, graph in graphs.items():
        print(name)
        knn = nx.average_degree_connectivity(graph)

        sns.set()
        # plot k x knn
        x = list(knn.keys())
        y = list(knn.values())

        pp.title("k x knn - %s" % name)
        pp.ylabel("Knn(K)")
        pp.xlabel("K")
        pp.scatter(x, y, c=colors[i], s = 100)
        
        pp.grid(False)

        pp.savefig('plots/' + name + "-kxknn.png")
        pp.clf()
        i += 1

        # correlation
        correlation = pearson(graph.degree().values(), knn.values())
        print("correlation: %.4f" % correlation)


def modularities(graphs):
    print("MODULARITIES")
    
    for name, graph in graphs.items():
        print(name)    
        # convert to igraph
        g = nx_to_ig(graph)
        # edge betweenness centrality
        community = g.community_edge_betweenness(directed=False).as_clustering()
        print("edge betweenness centrality: %.4f" % (community.modularity))
        # fast-greedy
        community = g.community_fastgreedy().as_clustering()
        print("fast greedy: %.4f" % (community.modularity))
        # eigenvectors of matrices
        community = g.community_leading_eigenvector()
        print("eigenvectors of matrices: %.4f" % (community.modularity))
        # walktrap
        community = g.community_walktrap().as_clustering()
        print("walktrap: %.4f" % (community.modularity))
        print("\n")


def plot_modularity_evolution():
    pass


def communities():
    print("COMMUNITY DETECTION")

    # initialize NMI vectors
    nmi = {}
    nmi["edge_bet"] = []
    nmi["fastgreedy"] = []
    nmi["eigenvector"] = []
    nmi["walktrap"] = []

    # varying mu from 0.1 to 1.0
    mu = np.arange(0.1, 1.1, 0.1)
    for i in mu:
        print("Running for mu = %.1f" % i)

        # run package / generate communities
        call(['./binary_networks/benchmark', '-N', '300', '-k', '8', '-maxk', '30', '-mu', str(i)])

        # read generated graph
        g = nx.read_edgelist('./network.dat')
        # the membership vector should contain the community id of each vertex
        # read generated memberships vector
        memberships = []
        mems = open('./community.dat')
        for line in mems:
            memberships.append(int(line.split()[1])) # append community id 

        # apply detection algorithms and get new memberships vectors
        print("running detection...")
        g = nx_to_ig(g)
        print("edge_bet")
        # edge betweenness centrality
        detection_edge_bet = g.community_edge_betweenness(directed=False).as_clustering().membership
        # fast-greedy
        print("fastgreedy")
        detection_fastgreedy = g.community_fastgreedy().as_clustering().membership
        # eigenvectors of matrices
        print("eigenvector")
        detection_eigenvector = g.community_leading_eigenvector().membership
        # walktrap
        print("walktrap")
        detection_walktrap = g.community_walktrap().as_clustering().membership

        # NMI 
        # compare generated membership with the ones generated
        # by the detection algorithms
        print("finding NMIs...")
        nmi["edge_bet"].append(ig.compare_communities(memberships,detection_edge_bet))
        nmi["fastgreedy"].append(ig.compare_communities(memberships,detection_fastgreedy))
        nmi["eigenvector"].append(ig.compare_communities(memberships,detection_eigenvector))
        nmi["walktrap"].append(ig.compare_communities(memberships,detection_walktrap))

    # plot
    print("plotting...")
    sns.set()

    pp.plot(mu, nmi["edge_bet"], color=colors[0],linestyle='solid', marker='o', label='edge betweenness centrality')
    pp.plot(mu, nmi["fastgreedy"],color=colors[1], linestyle='solid', marker='o', label='fastgreedy')
    pp.plot(mu, nmi["eigenvector"],color=colors[3], linestyle='solid', marker='o', label='eigenvetor matrices')
    pp.plot(mu, nmi["walktrap"],color=colors[5], linestyle='solid', marker='o', label='walktrap')

    # pp.title("NMI")
    pp.ylabel("NMI")
    pp.xlabel("Mixing parameter µ")        
    pp.legend()
    pp.grid(False)

    pp.savefig('plots/community_detection.png')

# read networks
graphs = {}
graphs["Euroroad"] = read_graph("./networks/euroroad.txt")
graphs["Hamster"] = read_graph("./networks/hamster.txt")
graphs["Airports"] = read_graph("./networks/USairports.txt")
graphs["Cortical Human"] = read_graph("./networks/cortical-human.txt")
graphs["Cortical Cat"] = read_graph("./networks/cortical-cat.txt")
graphs["Cortical Monkey"] = read_graph("./networks/cortical-monkey.txt")

# measures
# assortativity(graphs)
# k_x_knn(graphs)
# modularities(graphs)
communities()
print("done")