# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:17:05 2019

@author: micha
"""

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio
import math

rnd.seed(1)

def random_walk_path(graph, N, start_node):
    path = []
    for step in range(N):
        connections = graph.neighbors(start_node)
        target = rnd.choice(connections)
        path.append(target)
        start_node = target
    return path
        
def gif(graph, path):
    i = 0
    filenames = []
    images = []
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos = pos)
    for node in path:
        plt.plot(pos[node][0],pos[node][1], color = 'blue', marker = 'o', markersize = 18)
        name = '%d_slide.png' %i
        plt.savefig(name)
        filenames.append(name)
        plt.plot(pos[node][0],pos[node][1], color = 'red', marker = 'o', markersize = 18)
        i += 1
    for filename in filenames:
        images.append(imageio.imread(filename))
    kargs = { 'duration': 0.5 }
    imageio.mimsave('random_walk_in_network.gif', images, **kargs)

def hitting_time(graph, path, hit_time = {}):
    nodes = graph.nodes()
    appended = {}
    for node1 in nodes:
        appended[node1] = 0
        if node1 not in hit_time:
            hit_time[node1] = []
    for node1 in nodes:
        counter = 1
        for node2 in path:
            if node2 == node1:
                if appended[node1] == 0:
                    hit_time[node1].append(counter)
                    appended[node1] = 1
            counter += 1
    return hit_time

def multiple_hitting_time(graph, N, start_node, n=10):
    hit_time = {}
    for i in range(n):
        path = random_walk_path(graph = graph, N = N, start_node=start_node)
        hit_time = hitting_time(graph, path, hit_time = hit_time)
#    print(path)
    mean_hit_time = hit_time
    for key in hit_time:
        mean_hit_time[key] = np.mean(hit_time[key])
    return mean_hit_time

N = 20 #no of steps
start_node = 1

G = nx.watts_strogatz_graph(n=10, k=4, p=0.3, seed = 1)
#G = nx.barabasi_albert_graph(n = 10, m= 3, seed = 1)
#G = nx.complete_graph(n = 10)

#nx.draw_circular(G)

mean_hit_time = multiple_hitting_time(graph = G, N = N, start_node = start_node, n=10)
print(mean_hit_time)