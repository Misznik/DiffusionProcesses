# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:37:22 2019

@author: micha
"""

import pickle
import requests
import networkx as nx
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def snowball(username, connection_dict ={}, max_depth = 2):
    counter_depth = 1
    depth = max_depth
    while counter_depth <= depth:
        connections = user_connections(username)
        connection_dict[username] = connections
        for connection in connections:
            snowball(connection, connection_dict, max_depth = depth - counter_depth)
        counter_depth += 1
    return connection_dict

def user_connections(username):
    request = requests.get("http://www.livejournal.com/misc/fdata.bml?user=%s" % username)
    return request.text.replace(" ", "").replace("\n", "").split(">")[1:-1]


username_main = "valerois"
#temp = snowball(username_main, connection_dict ={}, max_depth = 2)
#pickle.dump(temp, open("connections","wb"))

connections_data = pickle.load( open("connections", "rb"))

graph = nx.Graph()
for (username, username_connections) in connections_data.items():
    for connection in username_connections:
        graph.add_edge(username, connection)

nodes_count = len(graph.nodes())
edges_count = len(graph.edges())
degrees = list(graph.degree().values())
celebrities = sorted(graph.degree().items(), reverse = True, key=lambda x: x[1])
print("No. of nodes: %d" % nodes_count)
print("No. of edges: %d" % edges_count)
print("Avg. degree: %.2f" % np.mean(degrees))
print("Var. of the degree: %.2f" % np.var(degrees))
print("Celebrities of the network:", celebrities[0:5])
        

x = np.arange(celebrities[-1][1], celebrities[0][1], 100, dtype=int)
sns.distplot((degrees), bins=x - 0.5, hist =False, kde = True, label = "density",
                 hist_kws={"rwidth":0.5,'edgecolor':'black', 'alpha':0.5})
plt.title("graph degree distribution of user: %s" % username_main)
plt.legend()
plt.show()

#betweenness = nx.betweenness_centrality(graph, k=20)
#pickle.dump(betweenness, open("betweenness_file","wb"))

betweenness_data = pickle.load( open("betweenness_file", "rb"))
bottlenecks = sorted(betweenness_data.items(), reverse = True, key=lambda x: x[1])
print("Bottlenecks of the network:", bottlenecks[0:5])