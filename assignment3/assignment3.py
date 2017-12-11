#!/bin/usr/env python3
# -*- coding: utf-8 -*-

'''
Dynamical Processes in Complex Networks
University of Sao Paulo
Professor Francisco Aparecido Rodrigues

Students:
Felipe Scrochio Custódio - 9442688
Gabriel Henrique Scalici - 9292970


Assignment 3 - Modelling complex networks, failures and attacks
'''

# networks
import networkx as nx
import igraph as ig

# data processing
import numpy as np
from sklearn.preprocessing import normalize

# plotting
from matplotlib import pyplot as pp
import seaborn as sns

# tools
import math
import random
import progressbar

# plot colors
colors = ["#1abc9c", "#2ecc71", "#3498db", "#f1c40f", "#e67e22", "#e74c3c", "#2c3e50"]

# graph functions
def giant_component(graph):
    return nx.Graph(max(nx.connected_component_subgraphs(graph), key=len))


def stat_moment(graph, moment):
    measure = 0
    for node in graph.nodes_iter():
        measure += graph.degree(node) ** moment
    return measure / graph.number_of_nodes()


def degree_distribution(graph):
    degrees = {}
    for node in graph.nodes_iter():
        degree = graph.degree(node)
        if degree not in degrees:
            degrees[degree] = 0
        degrees[degree] += 1
    distribution = sorted(degrees.values())
    return distribution

def average_degree(graph):
    degrees = graph.degree().values()
    average = sum(degrees)/len(degrees)
    return average

def entropy(graph):
    entropy = 0
    distribution = degree_distribution(graph)

    for value in distribution:
        if value > 0:
            val = (value / graph.number_of_nodes())
            entropy -= (val) * math.log2(val)
    return entropy

# helper functions
def nx_to_ig(graph):
    g = ig.Graph.TupleList(graph.edges(), directed=False)
    return g

def ig_to_nx(graph):
    A = graph.get_edgelist()
    g = nx.Graph(A)
    return g

# assignment functions

# 1
def network_models():
    erdos = []
    watts = []
    barabasi = []
    # generate 30 networks of each model
    print("Generating networks...")
    bar = progressbar.ProgressBar(max_value=30)
    for i in range(30):
        bar.update(i)
        erdos.append(nx.erdos_renyi_graph(500, 0.1))
        watts.append(nx.watts_strogatz_graph(1000, 10, 0.1))
        barabasi.append(nx.barabasi_albert_graph(2000, 10))
    bar.finish()

    # degree distribution (one of each)
    print("Finding degree distributions...")
    dists = {}
    dists["Erdös-Rényi"] = degree_distribution(erdos[0])
    dists["Watts-Strogatz"] = degree_distribution(watts[0])
    dists["Barabási-Albert"] = degree_distribution(barabasi[0])

    # plot
    print("Plotting...")
    sns.set()

    pp.title("Erdös-Rényi - Degree Distribution")
    pp.hist(list(erdos[0].degree().values()), dists["Erdös-Rényi"], color=colors[0])
    pp.ylabel("Frequency")
    pp.xlabel("Degree (k)")
    pp.grid(False)
    pp.savefig('plots/erdos-degree-dist.png')
    pp.clf()

    pp.title("Watts-Strogatz - Degree Distribution")
    pp.hist(list(watts[0].degree().values()), dists["Watts-Strogatz"], color=colors[1])
    pp.ylabel("Frequency")
    pp.xlabel("Degree (k)")
    pp.grid(False)
    pp.savefig('plots/watts-degree-dist.png')
    pp.clf()

    pp.title("Barabási-Albert - Degree Distribution")
    pp.hist(list(barabasi[0].degree().values()), dists["Barabási-Albert"], color=colors[2])
    pp.ylabel("Frequency")
    pp.xlabel("Degree (k)")
    pp.grid(False)
    pp.savefig('plots/barabasi-degree-dist.png')
    pp.clf()
    print("Done plotting.")

    # table
    print("Taking measures...")
    lens = {}
    lens["erdos"] = []
    lens["watts"] = []
    lens["barabasi"] = []

    degrees = {}
    degrees["erdos"] = []
    degrees["watts"] = []
    degrees["barabasi"] = []

    clusterings = {}
    clusterings["erdos"] = []
    clusterings["watts"] = []
    clusterings["barabasi"] = []

    assortativities = {}
    assortativities["erdos"] = []
    assortativities["watts"] = []
    assortativities["barabasi"] = []

    shortest_paths = {}
    shortest_paths["erdos"] = []
    shortest_paths["watts"] = []
    shortest_paths["barabasi"] = []

    entropies = {}
    entropies["erdos"] = []
    entropies["watts"] = []
    entropies["barabasi"] = []

    moments = {}
    moments["erdos"] = []
    moments["watts"] = []
    moments["barabasi"] = []

    print("Calculating Erdös-Rényi measurements...")
    for graph in erdos:
        lens["erdos"].append(len(graph))
        degrees["erdos"].append(average_degree(graph))
        clusterings["erdos"].append(nx.average_clustering(graph))
        assortativities["erdos"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["erdos"].append(nx.average_shortest_path_length(graph))
        entropies["erdos"].append(entropy(graph))
        moments["erdos"].append(stat_moment(graph, 2))

    print("Calculating Watts-Strogatz measurements...")
    for graph in watts:
        lens["watts"].append(len(graph))
        degrees["watts"].append(average_degree(graph))
        clusterings["watts"].append(nx.average_clustering(graph))
        assortativities["watts"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["watts"].append(nx.average_shortest_path_length(graph))
        entropies["watts"].append(entropy(graph))
        moments["watts"].append(stat_moment(graph, 2))

    print("Calculating Barabási-Albert measurements...")
    for graph in barabasi:
        lens["barabasi"].append(len(graph))
        degrees["barabasi"].append(average_degree(graph))
        clusterings["barabasi"].append(nx.average_clustering(graph))
        assortativities["barabasi"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["barabasi"].append(nx.average_shortest_path_length(graph))
        entropies["barabasi"].append(entropy(graph))
        moments["barabasi"].append(stat_moment(graph, 2))

    print("Measurements for Erdös-Rényi networks")
    # median
    print("Median of...")
    print("Number of nodes = %d" % np.median((lens["erdos"])))
    print("Degrees = %.4f" % np.median((degrees["erdos"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["erdos"])))
    print("Assortativity = %.4f" % np.median((assortativities["erdos"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["erdos"])))
    print("Shannon entropies = %.4f" % np.median((entropies["erdos"])))
    print("Second stat moments = %.4f" % np.median((moments["erdos"])))

    # deviation
    print("Standard Deviation of...")
    print("Number of nodes = %d" % np.std((lens["erdos"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["erdos"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["erdos"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["erdos"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["erdos"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["erdos"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["erdos"]), ddof=1))

    print("Measurements for Watts-Strogatz networks")
    # median
    print("Median of...")
    print("Number of nodes = %d" % np.median((lens["watts"])))
    print("Degrees = %.4f" % np.median((degrees["watts"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["watts"])))
    print("Assortativity = %.4f" % np.median((assortativities["watts"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["watts"])))
    print("Shannon entropies = %.4f" % np.median((entropies["watts"])))
    print("Second stat moments = %.4f" % np.median((moments["watts"])))

    # deviation
    print("Standard Deviation of...")
    print("Number of nodes = %d" % np.std((lens["watts"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["watts"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["watts"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["watts"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["watts"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["watts"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["watts"]), ddof=1))

    print("Measurements for Barabási-Albert networks")
    # median
    print("Median of...")
    print("Number of nodes = %d" % np.median((lens["barabasi"])))
    print("Degrees = %.4f" % np.median((degrees["barabasi"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["barabasi"])))
    print("Assortativity = %.4f" % np.median((assortativities["barabasi"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["barabasi"])))
    print("Shannon entropies = %.4f" % np.median((entropies["barabasi"])))
    print("Second stat moments = %.4f" % np.median((moments["barabasi"])))

    # deviation
    print("Standard Deviation of...")
    print("Number of nodes = %d" % np.std((lens["barabasi"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["barabasi"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["barabasi"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["barabasi"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["barabasi"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["barabasi"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["barabasi"]), ddof=1))

# 2
def ER_model():
    giants = {}
    degrees = np.arange(1.0, 5.0, 0.1) # increase degree from 1 to 5 in 0.1 steps
    # degrees = np.arange(0.0, 1.0, 0.1)

    print("Finding giant components for different average degrees...")
    bar = progressbar.ProgressBar(max_value=5)
    for p in degrees:
        bar.update(p)
        # generate ER networks
        current = nx.erdos_renyi_graph(1000, p)
        # store size of giant component for current p
        giants[p] = len(giant_component(current))
    bar.finish()

    # normalize data
    y1 = (np.asarray(list(giants.values()))).reshape(1, -1)
    y1 = normalize(y1, norm='l1', axis=1)
    x = degrees.reshape(1,-1)

    # plot
    print("Plotting...")
    sns.set()
    # pp.plot(x[0], y1[0], color=colors[6])
    pp.plot(x, y1, color=colors[6])
    pp.xlabel("Connection probability")
    pp.ylabel("Size of giant component")
    pp.grid(False)
    pp.savefig('plots/ER-evolution.png')
    pp.clf()

# 3
def WS_model():
    clusterings = []
    paths = []

    bar = progressbar.ProgressBar(max_value=1)
    print("Generating WS networks...")
    # generate WS networks
    for p in np.arange(0.0, 1.0, 0.001):
        network = nx.watts_strogatz_graph(1000, 5, p)
        clusterings.append(nx.average_clustering(network))
        paths.append(nx.average_shortest_path_length(network))
        bar.update(p)
    bar.finish()

    # plot
    print("Plotting...")

    # list to numpy array
    y1 = (np.asarray(clusterings)).reshape(1, -1)
    y2 = (np.asarray(paths)).reshape(1, -1)

    # normalize data
    y1 = normalize(y1, norm='l1', axis=1)
    y2 = normalize(y2, norm='l1', axis=1)

    x = (np.arange(0, 1, 0.001)).reshape(1,-1)

    sns.set()
    pp.title("Watts-Strogatz - Small World")
    pp.xscale('log')
    # pp.yscale('log')

    pp.plot(x[0], y1[0], color=colors[5], label="clustering coefficient")
    pp.plot(x[0], y2[0], color=colors[6], label="mean vertex-vertex distance")
    pp.xlabel("rewiring probability")
    pp.ylabel("coefficient or distance")
    pp.grid(False)
    pp.legend()
    pp.savefig('plots/WS-evolution.png')
    pp.clf()

 # 4
def BA_model():
    barabasi05 = []
    barabasi10 = []
    barabasi15 = []
    barabasi20 = []
    # generate 30 networks, do the same as one
    for i in range(10):
        #generate Barabasi network with p = power
        barabasi05.append(ig_to_nx(ig.Graph.Barabasi(500, 10, power=0.5)))
        barabasi10.append(ig_to_nx(ig.Graph.Barabasi(500, 10, power=1)))
        barabasi15.append(ig_to_nx(ig.Graph.Barabasi(500, 10, power=1.5)))
        barabasi20.append(ig_to_nx(ig.Graph.Barabasi(500, 10, power=2)))

    print("Finding degree distributions...")
    dists = {}
    dists["barabasi05"] = degree_distribution(barabasi05[0])
    dists["barabasi10"] = degree_distribution(barabasi10[0])
    dists["barabasi15"] = degree_distribution(barabasi15[0])
    dists["barabasi20"] = degree_distribution(barabasi20[0])

    # table
    print("Taking measures...")

    lens = {}
    lens["barabasi05"] = []
    lens["barabasi10"] = []
    lens["barabasi15"] = []
    lens["barabasi20"] = []

    degrees = {}
    degrees["barabasi05"] = []
    degrees["barabasi10"] = []
    degrees["barabasi15"] = []
    degrees["barabasi20"] = []

    clusterings = {}
    clusterings["barabasi05"] = []
    clusterings["barabasi10"] = []
    clusterings["barabasi15"] = []
    clusterings["barabasi20"] = []

    assortativities = {}
    assortativities["barabasi05"] = []
    assortativities["barabasi10"] = []
    assortativities["barabasi15"] = []
    assortativities["barabasi20"] = []

    shortest_paths = {}
    shortest_paths["barabasi05"] = []
    shortest_paths["barabasi10"] = []
    shortest_paths["barabasi15"] = []
    shortest_paths["barabasi20"] = []

    entropies = {}
    entropies["barabasi05"] = []
    entropies["barabasi10"] = []
    entropies["barabasi15"] = []
    entropies["barabasi20"] = []

    moments = {}
    moments["barabasi05"] = []
    moments["barabasi10"] = []
    moments["barabasi15"] = []
    moments["barabasi20"] = []

    for graph in barabasi05:
        lens["barabasi05"].append(len(graph))
        degrees["barabasi05"].append(average_degree(graph))
        clusterings["barabasi05"].append(nx.average_clustering(graph))
        assortativities["barabasi05"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["barabasi05"].append(nx.average_shortest_path_length(graph))
        entropies["barabasi05"].append(entropy(graph))
        moments["barabasi05"].append(stat_moment(graph, 2))

    for graph in barabasi10:
        lens["barabasi10"].append(len(graph))
        degrees["barabasi10"].append(average_degree(graph))
        clusterings["barabasi10"].append(nx.average_clustering(graph))
        assortativities["barabasi10"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["barabasi10"].append(nx.average_shortest_path_length(graph))
        entropies["barabasi10"].append(entropy(graph))
        moments["barabasi10"].append(stat_moment(graph, 2))

    for graph in barabasi15:
        lens["barabasi15"].append(len(graph))
        degrees["barabasi15"].append(average_degree(graph))
        clusterings["barabasi15"].append(nx.average_clustering(graph))
        assortativities["barabasi15"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["barabasi15"].append(nx.average_shortest_path_length(graph))
        entropies["barabasi15"].append(entropy(graph))
        moments["barabasi15"].append(stat_moment(graph, 2))

    for graph in barabasi20:
        lens["barabasi20"].append(len(graph))
        degrees["barabasi20"].append(average_degree(graph))
        clusterings["barabasi20"].append(nx.average_clustering(graph))
        assortativities["barabasi20"].append(nx.degree_assortativity_coefficient(graph))
        shortest_paths["barabasi20"].append(nx.average_shortest_path_length(graph))
        entropies["barabasi20"].append(entropy(graph))
        moments["barabasi20"].append(stat_moment(graph, 2))

    print("Calculating Barabási-Albert measurements for alfa = 0.5...")
    # median
    print("Median of Barabasi alfa = 0.5")
    print("Number of nodes = %d" % np.median((lens["barabasi05"])))
    print("Degrees = %.4f" % np.median((degrees["barabasi05"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["barabasi05"])))
    print("Assortativity = %.4f" % np.median((assortativities["barabasi05"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["barabasi05"])))
    print("Shannon entropies = %.4f" % np.median((entropies["barabasi05"])))
    print("Second stat moments = %.4f" % np.median((moments["barabasi05"])))

    # deviation
    print("Standard Deviation of Barabasi alfa = 0.5")
    print("Number of nodes = %d" % np.std((lens["barabasi05"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["barabasi05"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["barabasi05"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["barabasi05"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["barabasi05"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["barabasi05"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["barabasi05"]), ddof=1))

    print("Calculating Barabási-Albert measurements for alfa = 1.0...")
    # median
    print("Median of Barabasi alfa = 1.0")
    print("Number of nodes = %d" % np.median((lens["barabasi10"])))
    print("Degrees = %.4f" % np.median((degrees["barabasi10"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["barabasi10"])))
    print("Assortativity = %.4f" % np.median((assortativities["barabasi10"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["barabasi10"])))
    print("Shannon entropies = %.4f" % np.median((entropies["barabasi10"])))
    print("Second stat moments = %.4f" % np.median((moments["barabasi10"])))

    # deviation
    print("Standard Deviation of Barabasi alfa = 1.0")
    print("Number of nodes = %d" % np.std((lens["barabasi10"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["barabasi10"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["barabasi10"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["barabasi10"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["barabasi10"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["barabasi10"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["barabasi10"]), ddof=1))

    print("Calculating Barabási-Albert measurements for alfa = 1.5...")
    # median
    print("Median of Barabasi alfa = 1.5")
    print("Number of nodes = %d" % np.median((lens["barabasi15"])))
    print("Degrees = %.4f" % np.median((degrees["barabasi15"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["barabasi15"])))
    print("Assortativity = %.4f" % np.median((assortativities["barabasi15"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["barabasi15"])))
    print("Shannon entropies = %.4f" % np.median((entropies["barabasi15"])))
    print("Second stat moments = %.4f" % np.median((moments["barabasi15"])))

    # deviation
    print("Standard Deviation of Barabasi alfa = 1.5")
    print("Number of nodes = %d" % np.std((lens["barabasi15"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["barabasi15"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["barabasi15"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["barabasi15"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["barabasi15"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["barabasi15"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["barabasi15"]), ddof=1))

    print("Calculating Barabási-Albert measurements for alfa = 2.0...")
    # median
    print("Median of Barabasi alfa = 2.0")
    print("Number of nodes = %d" % np.median((lens["barabasi20"])))
    print("Degrees = %.4f" % np.median((degrees["barabasi20"])))
    print("Clustering coefficient = %.4f" % np.median((clusterings["barabasi20"])))
    print("Assortativity = %.4f" % np.median((assortativities["barabasi20"])))
    print("Shortest paths = %.4f" % np.median((shortest_paths["barabasi20"])))
    print("Shannon entropies = %.4f" % np.median((entropies["barabasi20"])))
    print("Second stat moments = %.4f" % np.median((moments["barabasi20"])))

    # deviation
    print("Standard Deviation of Barabasi alfa = 2.0")
    print("Number of nodes = %d" % np.std((lens["barabasi20"]), ddof=1))
    print("Degrees = %.4f" % np.std((degrees["barabasi20"]), ddof=1))
    print("Clustering coefficient = %.4f" % np.std((clusterings["barabasi20"]), ddof=1))
    print("Assortativity = %.4f" % np.std((assortativities["barabasi20"]), ddof=1))
    print("Shortest paths = %.4f" % np.std((shortest_paths["barabasi20"]), ddof=1))
    print("Shannon entropies = %.4f" % np.std((entropies["barabasi20"]), ddof=1))
    print("Second stat moments = %.4f" % np.std((moments["barabasi20"]), ddof=1))

# # 5
def stress_test():
    # random removals
    lens = {}
    erdos = nx.erdos_renyi_graph(500, 0.1)
    lens["erdos"] = len(erdos)
    barabasi = nx.barabasi_albert_graph(2000, 10)
    lens["barabasi"] = len(barabasi)

    giant_sizes = {}
    giant_sizes["erdos"] = []
    giant_sizes["barabasi"] = []

    while (len(erdos) > 1):
        erdos.remove_node(erdos.nodes()[random.randint(0,len(erdos)-1)])
        giant_sizes["erdos"].append(len(giant_component(erdos)))

    while (len(barabasi) > 1):
        # remove vertex
        barabasi.remove_node(barabasi.nodes()[random.randint(0,len(barabasi)-1)])
        giant_sizes["barabasi"].append(len(giant_component(barabasi)))

    # plot stress test
    sns.set()
    pp.plot(lens["erdos"], giant_sizes["erdos"], color=colors[0])
    pp.xlabel("Number of removals")
    pp.ylabel("Size of giant component")
    pp.grid(False)
    pp.savefig('plots/ER-stress-test-random.png')
    pp.clf()

    sns.set()
    pp.plot(lens["barabasi"], giant_sizes["barabasi"], color=colors[0])
    pp.xlabel("Number of removals")
    pp.ylabel("Size of giant component")
    pp.grid(False)
    pp.savefig('plots/BA-stress-test-random.png')
    pp.clf()

    # remove from most connected to least connected
    lens.clear()
    erdos = nx.erdos_renyi_graph(500, 0.1)
    lens["erdos"] = len(erdos)
    barabasi = nx.barabasi_albert_graph(2000, 10)
    lens["barabasi"] = len(barabasi)

    erdos_sorted = sorted(erdos.degree_iter(),key=itemgetter(1),reverse=True)
    barabasi_nodes = sorted(erdos.degree_iter(),key=itemgetter(1),reverse=True)

    giant_sizes.clear()
    giant_sizes["erdos"] = []
    giant_sizes["barabasi"] = []
    
    i = 0
    while (len(erdos) > 1):
        # remove vertex
        erdos.remove_node(erdos_sorted[i])
        giant_sizes["erdos"].append(len(giant_component(erdos)))
        i += 1

    i = 0
    while (len(barabasi) > 1):
        # remove vertex
        barabasi.remove_node(barabasi_sorted[i])
        giant_sizes["barabasi"].append(len(giant_component(barabasi)))
        i += 1

    # plot stress test
    sns.set()
    pp.plot(lens["erdos"], giant_sizes["erdos"], color=colors[0])
    pp.xlabel("Number of removals")
    pp.ylabel("Size of giant component")
    pp.grid(False)
    pp.savefig('plots/ER-stress-test-sorted.png')
    pp.clf()

    sns.set()
    pp.plot(lens["barabasi"], giant_sizes["barabasi"], color=colors[0])
    pp.xlabel("Number of removals")
    pp.ylabel("Size of giant component")
    pp.grid(False)
    pp.savefig('plots/BA-stress-test-sorted.png')
    pp.clf()


def main():
    network_models()
    ER_model()
    WS_model()
    BA_model()
    stress_test()
    print("done")

if __name__ == "__main__":
    main()
