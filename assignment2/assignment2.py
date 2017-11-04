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
import numpy as np
from matplotlib import pyplot as pp
import seaborn as sns


def pearson(x, y):
	# from: https://stackoverflow.com/a/5713856
	# Assume len(x) == len(y)
	n = len(x)
	sum_x = float(sum(x))
	sum_y = float(sum(y))
	sum_x_sq = sum(map(lambda x: pow(x, 2), x))
	sum_y_sq = sum(map(lambda x: pow(x, 2), y))
	psum = sum(imap(lambda x, y: x * y, x, y))
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
	return ig.Graph.Adjacency((nx.to_numpy_matrix(g) > 0).tolist())


def assortativity(graphs):
	print("ASSORTATIVITY")
	for name,graph in graphs.items():
		assortativity = nx.degree_assortativity_coefficient(graph)
		print("%s = %.4f" % (name, assortativity))


def plot_knn(graphs):
	
	for name, graph in graphs.items():

		knn = nx.average_degree_connectivity(graph)
		sns.set()

		# plot k x knn
		x = list(knn.keys())
		y = list(knn.values())

		pp.title("k x knn - %s" % name)
		pp.ylabel("Knn")
		pp.xlabel("K")
		pp.scatter(x, y, c=y, s = 100)
		
		pp.colorbar()
		pp.grid(False)
		pp.show()
		# pp.savefig(name+"-knn.png")


def modularities(graph):
	pass


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
assortativity(graphs)
plot_knn(graphs)
