import networkx as nx
import matplotlib.pyplot as plt

def main():

    # generate graphs
    graph = nx.Graph()

    graph.add_edge(1, 2)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 5)
    graph.add_edge(5, 1)
    graph.add_edge(3, 5)
    
    # draw graph
    nx.draw(graph)
    plt.show()

if __name__ == "__main__":
    main()

