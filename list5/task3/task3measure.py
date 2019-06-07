import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def measures(G,probability,N):
    S_list = []
    frac_list = []
    time_list = []
    time_to_max_list = []
    for p in probability:
        I = []
        R = []
        start_node = random.choice(list(G.nodes()))
        I = I + [start_node]
        frac = []
        time = 0
        time_to_max = 1
        for j in range(N):
            while len(I) != 0:
                newI = []
                frac = frac + [len(I)/nx.number_of_nodes(G)]

                for i in range(len(I)):
                    infecting = I[i]
                    S = list(set(G.neighbors(infecting))-set(I)-set(R))
                    for k in S:
                        if k not in newI:
                            if random.random() < p:
                                if k not in newI:
                                    newI.append(k)
                
                time = time + 1
                if len(frac)>1:                    
                    if max(frac)>max(frac[:-1]):
                        time_to_max = time

                R = R + I
                I = newI
            S = nx.number_of_nodes(G) - len(I) - len(R)
        S_list.append(S)
        frac_list.append(frac)
        time_list.append(time)
        time_to_max_list.append(time_to_max)
            
    return S_list, time_list, time_to_max_list

n = 100
p0 = 0.1
N=100
p = np.linspace(0,1,20)

# random graph
figure1 = plt.figure(figsize=(10,5))
G = nx.gnp_random_graph(n,p0)
[S_list, time_list, time_to_max_list] = measures(G,p,N)
plt.plot(p,S_list)
plt.plot(p,time_list)
plt.plot(p,time_to_max_list)
plt.xlabel("p")
plt.legend(('S', 't', 't to max'))
plt.title('random graph')
plt.show()

# lattice graph
figure2 = plt.figure(figsize=(10,5))
G = nx.grid_2d_graph(10,10)
[S_list, time_list, time_to_max_list] = measures(G,p,N)
plt.plot(p,S_list)
plt.plot(p,time_list)
plt.plot(p,time_to_max_list)
plt.xlabel("p")
plt.legend(('S', 't', 't to max'))
plt.title('lattice graph')
plt.show()

# barabasi_albert graph
figure3 = plt.figure(figsize=(10,5))
m=4
G = nx.barabasi_albert_graph(n, m)
[S_list, time_list, time_to_max_list] = measures(G,p,N)
plt.plot(p,S_list)
plt.plot(p,time_list)
plt.plot(p,time_to_max_list)
plt.xlabel("p")
plt.legend(('S', 't', 't to max'))
plt.title('barabasi albert graph')
plt.show()

# watts_strogatz graph
figure4 = plt.figure(figsize=(10,5))
k=4
G = nx.watts_strogatz_graph(n, k, p0)
[S_list, time_list, time_to_max_list] = measures(G,p,N)
plt.plot(p,S_list)
plt.plot(p,time_list)
plt.plot(p,time_to_max_list)
plt.xlabel("p")
plt.legend(('S', 't', 't to max'))
plt.title('watts strogatz graph')
plt.show()