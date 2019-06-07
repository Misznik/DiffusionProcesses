# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:34:49 2019

@author: micha
"""

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio

size = 10
G = nx.grid_2d_graph( m = size, n = size)
pos = dict( (n, n) for n in G.nodes() )
labels = dict( ((i, j), i * 10 + j) for i, j in G.nodes() )
#nx.draw(G, pos=pos)
#nx.draw_networkx(G, pos=pos, labels=labels)
#plt.axis('off')
#plt.show()
nodes = list(G.nodes())

max_t = 30

idx = int(rnd.choice(len(nodes),1))
start = nodes[idx]
path = []
for t in range(max_t):
    neigbors = G.neighbors(start)
    idx = int(rnd.choice(len(neigbors),1))
    target = neigbors[idx]
    path.append([start,target])
    start = target

filenames = []
for i in range(len(path)):
    nx.draw(G, pos=pos)
    for j in range(i):
        plt.plot([path[j][0][0],path[j][1][0]], [path[j][0][1],path[j][1][1]], 'b')
    name = '%d_slide.png' %i
    plt.xlim((-1,size + 1))
    plt.ylim((-1,size + 1))
    plt.savefig(name)
    filenames.append(name)
    
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
kargs = { 'duration': 0.5 }
imageio.mimsave('random_walk.gif', images, **kargs)
