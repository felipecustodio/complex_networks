import networkx as nx
import matplotlib.pyplot as plt

def main():
    # read network files
    powergrid_file = open("./networks/opsahl-powergrid/out.opsahl-powergrid", "r")
    topology_file = open("./networks/topology/out.topology", "r")

    # generate graphs
    powergrid_graph = nx.Graph()
    topology_graph = nx.Graph()

    # read nodes from files
    for line in powergrid_file:
        powergrid_nodes = line.split()
        powergrid_graph.add_edge(powergrid_nodes[0], powergrid_nodes[1])

    for line in topology_file:
        topology_nodes = line.split()
        topology_graph.add_edge(topology_nodes[0], topology_nodes[1])

    nx.draw_networkx(powergrid_graph)
    plt.show()


    # calculations


    # close files
    powergrid_file.close()
    topology_file.close()

if __name__ == "__main__":
    main()
