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

# plot helpers
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
		pp.ylabel("Knn")
		pp.xlabel("K")
		pp.scatter(x, y, c=colors[i], s = 100)
		
		pp.grid(False)

		# pp.savefig(name + "-kxknn.png")
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


def generate_communities():
	pass


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
k_x_knn(graphs)
# modularities(graphs)