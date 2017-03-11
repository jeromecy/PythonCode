# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:08:23 2017

@author: zcao
"""

import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])

G.nodes()

G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
G.add_edge("u","w")
G.edges()

G.remove_node(2)

G.number_of_edges()


G = nx.karate_club_graph()

import matplotlib.pyplot as plt

nx.draw(G,with_labels = True, node_color = "lightblue",edge_color="gray")
plt.savefig("karate_graph.pdf")

G.degree()[33]

G.degree(0) is G.degree()[0]  ## True


from scipy.stats import bernoulli
bernoulli.rvs(p = 0.2)
  
N = 20      
p = 0.2



def er_graph(N,p):
    """ ER graph """
# loop over all pairs of nodes add an edge with prob p.
    G = nx.Graph() #empty graph
    G.add_nodes_from(range(N))
            
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p) == True:
                G.add_edge(node1,node2)
    return G


nx.draw(er_graph(50,0.08),node_size = 40, node_color="gray")
plt.savefig("ER1.pdf")


def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()),histtype="step")
    plt.xlabel("df $K$")
    plt.ylabel("$P(k)$")
    plt.title("df distribution")


G1 = er_graph(500,0.08)
plot_degree_distribution(G1)

G2 = er_graph(500,0.08)
plot_degree_distribution(G2)

G3 = er_graph(500,0.08)
plot_degree_distribution(G3)

plt.savefig("3df.pdf")



import numpy as np
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv",delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv",delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    print("Average degree %.2f" % np.mean(list(G.degree().values())))


basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)


## finding the largest connected component
gen = nx.connected_component_subgraphs(G1)

g = gen.__next__()

g.number_of_nodes()
len(gen.__next__())

len(G1)



G1_LCC = max(nx.connected_component_subgraphs(G1),key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2),key=len)

len(G1_LCC)
G1_LCC.number_of_nodes()

len(G2_LCC)
G2_LCC.number_of_nodes()


G1_LCC.number_of_nodes()/G1.number_of_nodes()
G2_LCC.number_of_nodes()/G2.number_of_nodes()


plt.figure()
nx.draw(G1_LCC, node_color="red",edge_color="gray",node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green",edge_color="gray",node_size=20)
plt.savefig("village2.pdf")


