#!/bin/usr/env python3
# -*- coding: utf-8 -*-

'''
Dynamical Processes in Complex Networks
University of Sao Paulo
Professor Francisco Aparecido Rodrigues

Students:
Felipe Scrochio Custódio - 9442688
Gabriel Henrique Scalici - 9292970


Assignment 4 - 
'''

import networkx as nx
import igraph as ig

import numpy as np
from matplotlib import pyplot as pp
import seaborn as sns

# plot colors
colors = ["#1abc9c", "#2ecc71", "#3498db", "#f1c40f", "#e67e22", "#e74c3c", "#2c3e50"]

# graph functions
def giant_component(graph):
    return nx.Graph(max(nx.connected_component_subgraphs(graph), key=len))

# helper functions
def nx_to_ig(graph):
    g = ig.Graph.TupleList(graph.edges(), directed=False)
    return g

# assignment functions

def main():
    print("done")

if __name__ == "__main__":
    main()