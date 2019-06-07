# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:08:20 2019

@author: micha
"""
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio
import math


angles = np.linspace(0, 2*math.pi, 1000)
a=1
N = 1000
MCS = 100
time = [i for i in range(N)]

def trajectory(N, a, time):
    start = (0,0)
    path = []
    nodes = [start]
    for t in time:
        angle = rnd.choice(angles)
        x = a * math.cos(angle)
        y = a * math.sin(angle)
        target = (start[0]  + x, start[1] + y)
        path.append((start, target))
        nodes.append(target)
        start = target
    unzipped_x, unzipped_y = zip(*nodes)
    unzipped_x = list( unzipped_x)
    unzipped_y = list(unzipped_y)
    x_p = [i for i in unzipped_x if i > 0]
    xy_p = [i for i in unzipped_x if i > 0 and unzipped_y[unzipped_x.index(i)] > 0]
    return x_p, xy_p

x_plus = []
xy_plus = []
for i in range(MCS):
    x_p, xy_p = trajectory(N, a, time)
    x_plus.append(len(x_p))
    xy_plus.append(len(xy_p))

sns.distplot(x_plus, hist = True, kde = True)
sns.distplot(xy_plus, hist = True, kde = True)
    


#for j in range(len(path)):
#        plt.plot([path[j][0][0],path[j][1][0]], [path[j][0][1],path[j][1][1]], 'b')