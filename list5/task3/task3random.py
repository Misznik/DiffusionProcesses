import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import os
import imageio
import re

n=30
p=0.2
probability = 0.7
G = nx.gnp_random_graph(n,p)

start_node = random.choice(list(G.nodes()))
I = []
R = []  
I = I + [start_node]
time = 1


plt.cla()
nx.draw_shell(G,node_color='g')
nx.draw_shell(G,nodelist=I,node_color='r',alpha=1)
nx.draw_shell(G,nodelist=R,node_color='b',alpha=1)
plt.savefig(r'C:\Users\micha\Desktop\Programs\DiffProcess\list5\random\\'+str(0)+'.png', dpi=100)

time = 1

while len(I) != 0:
    newI = []
    for i in range(len(I)):
        infecting = I[i]
        S = list(set(G.neighbors(infecting))-set(I)-set(R))
        for k in S:
            if k not in newI:
                if random.random() < probability:
                    if k not in newI:
                        newI.append(k)    
    R = R + I
    I = newI

    
        

    nx.draw_shell(G,node_color='g')
    nx.draw_shell(G,nodelist=I,node_color='r',alpha=1)
    nx.draw_shell(G,nodelist=R,node_color='b',alpha=1)
    plt.savefig(r'C:\Users\micha\Desktop\Programs\DiffProcess\list5\random\\'+str(time)+'.png', dpi=100)
    time = time + 1
    


png_dir = r'C:\Users\micha\Desktop\Programs\DiffProcess\list5\random'

# creating the gifs

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

alist = os.listdir(png_dir)
alist.sort(key=natural_keys)

images = []
for file_name in alist:
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave(r'C:\Users\micha\Desktop\Programs\DiffProcess\list5\gif_random.gif', images, duration = 0.5)