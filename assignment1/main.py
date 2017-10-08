from os import path
import networkx as nx
import powerlaw as pl
from matplotlib import pyplot as pp

#
# read all networks
#

all_graphs = {}
all_giants = {}
current_path = path.join('networks', 'hamster.txt')
with open(current_path, 'rb') as current_file:
    graph = nx.read_edgelist(current_file)
    all_graphs['hamster'] = graph
    all_giants['hamster'] = max(nx.connected_component_subgraphs(graph), key=len)

current_path = path.join('networks', 'euroroad.txt')
with open(current_path, 'rb') as current_file:
    graph = nx.read_edgelist(current_file)
    all_graphs['euroroad'] = graph
    all_giants['euroroad'] = max(nx.connected_component_subgraphs(graph), key=len)

current_path = path.join('networks', 'us-airports.txt')
with open(current_path, 'rb') as current_file:
    graph = nx.Graph()
    for line in current_file:
        items = line.split()
        graph.add_edge(items[0], items[1])
    all_graphs['us-airports'] = graph
    all_giants['us-airports'] = max(nx.connected_component_subgraphs(graph), key=len)

current_path = path.join('networks', 'us-powergrid.txt')
with open(current_path, 'rb') as current_file:
    graph = nx.Graph()
    for line in current_file:
        items = line.split()
        graph.add_edge(items[0], items[1])
    all_graphs['us-powergrid'] = graph
    all_giants['us-powergrid'] = max(nx.connected_component_subgraphs(graph), key=len)

#
# degree distributions
#

all_pdfs = {}
graph = all_giants['hamster']
n_nodes = graph.number_of_nodes()
all_pdfs['hamster'] = list(map(lambda x: x / n_nodes, nx.degree_histogram(graph)))
graph = all_giants['euroroad']
n_nodes = graph.number_of_nodes()
all_pdfs['euroroad'] = list(map(lambda x: x / n_nodes, nx.degree_histogram(graph)))
graph = all_giants['us-airports']
n_nodes = graph.number_of_nodes()
all_pdfs['us-airports'] = list(map(lambda x: x / n_nodes, nx.degree_histogram(graph)))
graph = all_giants['us-powergrid']
n_nodes = graph.number_of_nodes()
all_pdfs['us-powergrid'] = list(map(lambda x: x / n_nodes, nx.degree_histogram(graph)))

all_fits = {}
all_fits['hamster'] = pl.Fit(all_pdfs['hamster'])
print('hamster:\n\talpha:{:.4f}'.format(all_fits['hamster'].alpha))
all_fits['euroroad'] = pl.Fit(all_pdfs['euroroad'])
print('euroroad:\n\talpha:{:.4f}'.format(all_fits['euroroad'].alpha))
all_fits['us-airports'] = pl.Fit(all_pdfs['us-airports'])
print('us-airports:\n\talpha:{:.4f}'.format(all_fits['us-airports'].alpha))
all_fits['us-powergrid'] = pl.Fit(all_pdfs['us-powergrid'])
print('us-powergrid:\n\talpha:{:.4f}'.format(all_fits['us-powergrid'].alpha))

#
# show graphs
#

pp.title('degree probability distributions')
p1, = pp.loglog(all_pdfs['hamster'], 'r-', label='hamster')
p2, = pp.loglog(all_pdfs['euroroad'], 'g-', label='euroroad')
p3, = pp.loglog(all_pdfs['us-airports'], 'b-', label='us-airports')
p4, = pp.loglog(all_pdfs['us-powergrid'], 'y-', label='us-powergrid')
#pp.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
pp.legend(handles=[p1,p2,p3,p4], loc=1)
pp.grid(True)
pp.show()
pp.clf()
