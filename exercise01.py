#!/bin/usr/env python3

import networkx as nx
from matplotlib import pyplot as pl


def stat_moment(graph, moment):
    measure = 0
    for node in graph.nodes_iter():
        measure += graph.degree(node) ** moment
    return measure / graph.number_of_nodes()

def process_graph(graph, name):
    print('\nprocessing graph: ' + name)
    ## measure
    degree_histogram = nx.degree_histogram(graph)
    number_of_nodes = graph.number_of_nodes()
    for bin in range(len(degree_histogram)):
        degree_histogram[bin] = degree_histogram[bin] / number_of_nodes
    m1 = stat_moment(graph, 1)
    m2 = stat_moment(graph, 2)
    variance = m2 - m1 ** 2
    ## print
    print('m1: {:.4f}'.format(m1))
    print('m2: {:.4f}'.format(m2))
    print('variance: {:.4f}'.format(variance))
    pl.title('degree distribution: ' + name)
    pl.loglog(degree_histogram, 'b.')
    pl.show()

with open('./assignment01/networks/opsahl-powergrid/out.opsahl-powergrid', 'rb') as f:
    next(f, '')
    next(f, '')
    Ga = nx.read_edgelist(f, nodetype=int)


Gb = nx.MultiGraph()
with open('./assignment01/networks/topology/out.topology', 'rb') as f:
    next(f, '')
    for line in f:
        items = line.split()
        for occurrence in range(int(items[2])):
            Gb.add_edge(items[0], items[1])

Gc = nx.Graph()
Gc.add_edge(1, 2)
Gc.add_edge(2, 3)
Gc.add_edge(2, 4)
Gc.add_edge(4, 3)
Gc.add_edge(3, 5)
Gc.add_edge(5, 6)
Gc.add_edge(5, 7)
Gc.add_edge(7, 6)
Gc.add_edge(7, 8)
Gc.add_edge(7, 9)
Gc.add_edge(7, 10)

process_graph(Ga, 'Power Grid')
process_graph(Gb, 'Internet Topology')
process_graph(Gc, 'Class Example')
nx.draw_circular(Gc)
pl.show()

print('\ndone')
