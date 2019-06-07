# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:20:00 2019

@author: micha
"""

import networkx as nx
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt


def NNspin(G, p_ind, q, spinsons = {}):
    nodes = G.nodes()
    if spinsons == {}:
        for node in nodes:
#            spinsons[node] = rnd.choice([1,-1], p =[0.5,0.5]) #if we want a random starting condition
            spinsons[node] = 1 # we inititate with a positive consensus
    
    start_spinson = rnd.choice(nodes)
    nbrs = G.neighbors(start_spinson)
    if len(nbrs) < q: # if a node has less nbrs than q then we adjust to it
        choice = nbrs
    else:
        choice = list(rnd.choice(nbrs, size = q, replace = False))
    suma = 0
    
    if rnd.random() < p_ind: # case of independence
        if rnd.random() < 0.5:
            spinsons[start_spinson] = -spinsons[start_spinson]
    else:    # case of conformity
        for qc in choice:
            suma += spinsons[qc]
        if suma == len(choice): #if all agree
            spinsons[start_spinson] = 1
        elif suma == -len(choice):
            spinsons[start_spinson] = -1

    return spinsons

def MCsteps_magnetization(M, G, q, N, p_ind = list): #magnetization for p list
    magnetization = []
    for pi in p_ind:
        temp = []
        for i in range(M):
            spinsons = {}
            for j in range(N):
                spinsons = NNspin(G = G, p_ind= pi, q = q, spinsons=spinsons)
            pos = [node for node in spinsons if spinsons[node] == 1]
            neg = [node for node in spinsons if spinsons[node] == -1]
            temp.append((len(pos)-len(neg))/len(spinsons)) #magnetization
        magnetization.append(np.mean(temp)) #average magnetization
    return magnetization


N = 1000
p_ind = np.arange(0, 0.5, 0.02)
M = 1000

G = nx.barabasi_albert_graph(n = 100, m = 4)
magnetization1 = MCsteps_magnetization(M = M, G = G, q = 3, N=N, p_ind= p_ind)
magnetization2 = MCsteps_magnetization(M = M, G = G, q = 4,N=N, p_ind= p_ind)

G = nx.watts_strogatz_graph(n = 100, k = 4, p= 0.01)
magnetization3 = MCsteps_magnetization(M = M, G = G, q = 3,N=N, p_ind= p_ind)
magnetization4 = MCsteps_magnetization(M = M, G = G, q = 4,N=N, p_ind= p_ind)

G = nx.watts_strogatz_graph(n = 100, k = 4, p= 0.2)
magnetization5 = MCsteps_magnetization(M = M, G = G, q = 3,N=N, p_ind= p_ind)
magnetization6 = MCsteps_magnetization(M = M, G = G, q = 4,N=N, p_ind= p_ind)

G = nx.complete_graph(n = 100)
magnetization7 = MCsteps_magnetization(M = M, G = G, q = 3,N=N, p_ind= p_ind)
magnetization8 = MCsteps_magnetization(M = M, G = G, q = 4,N=N, p_ind= p_ind)

p_ind = np.arange(0, 0.5, 0.02)
fig1 = plt.figure(1)
plt.plot(p_ind,magnetization1)
plt.plot(p_ind,magnetization3)
plt.plot(p_ind,magnetization5)
plt.plot(p_ind,magnetization7)
plt.legend(("BA(N = 100, m = 4)","WS(N = 100, k = 4, p = 0.01)", "WS(N = 100, k = 4, p = 0.2)", "Complete(100)"))
plt.xlabel('p_independence')
plt.ylabel('magentization')
plt.title("Magnetization for q = 3")
plt.show()

fig2 = plt.figure(2)
plt.plot(p_ind,magnetization2)
plt.plot(p_ind,magnetization4)
plt.plot(p_ind,magnetization6)
plt.plot(p_ind,magnetization8)
plt.legend(("BA(N = 100, m = 4)","WS(N = 100, k = 4, p = 0.01)", "WS(N = 100, k = 4, p = 0.2)", "Complete(100)"))
plt.xlabel('p_independence')
plt.ylabel('magentization')
plt.title("Magnetization for q = 4")
plt.show()

G = nx.watts_strogatz_graph(n = 100, k = 4, p= 0.01)
magnetization11 = MCsteps_magnetization(M = M, G = G, q = 1,N=N, p_ind= p_ind)
magnetization12 = MCsteps_magnetization(M = M, G = G, q = 2,N=N, p_ind= p_ind)
magnetization13 = MCsteps_magnetization(M = M, G = G, q = 3,N=N, p_ind= p_ind)
magnetization14 = MCsteps_magnetization(M = M, G = G, q = 4,N=N, p_ind= p_ind)
magnetization15 = MCsteps_magnetization(M = M, G = G, q = 5,N=N, p_ind= p_ind)
magnetization16 = MCsteps_magnetization(M = M, G = G, q = 6,N=N, p_ind= p_ind)

fig3 = plt.figure(3)
plt.plot(p_ind,magnetization11)
plt.plot(p_ind,magnetization12)
plt.plot(p_ind,magnetization13)
plt.plot(p_ind,magnetization14)
plt.plot(p_ind,magnetization15)
plt.plot(p_ind,magnetization16)
plt.legend(("q=1","q=2","q=3","q=4","q=5","q=6"))
plt.xlabel('p_independence')
plt.ylabel('magentization')
plt.title("Magnetization for WS(N = 100, k = 4, p = 0.01)")
plt.show()


def magnetization_time(T, G, q, p_ind): #single trajectory in time, T steps
    magnetization = []
    spinsons ={}
    for t in range(T):
        spinsons = NNspin(G = G, p_ind= p_ind, q = q, spinsons=spinsons)
        pos = [node for node in spinsons if spinsons[node] == 1]
        neg = [node for node in spinsons if spinsons[node] == -1]
        magnetization.append((len(pos)-len(neg))/len(spinsons)) #magnetization
    return magnetization

p_ind = 0.5
T = 1000
fig4 = plt.figure(4)
G = nx.watts_strogatz_graph(n = 100, k = 4, p= 0.01)
magnetization = magnetization_time(T = T, G = G, q = 4, p_ind= p_ind)
plt.plot(range(T),magnetization)
plt.xlabel("t")
plt.ylabel('magentization')
plt.title("time evolution for WS(N = 100, k = 4, p = 0.01)")
plt.show()



def MCsteps_magnetization_time(M, G, q, T, p_ind): #average magnetization in time, M times, T steps
    magnetization = [0]*T
    for i in range(M):
        spinsons = {}
        for t in range(T):
            spinsons = NNspin(G = G, p_ind= p_ind, q = q, spinsons=spinsons)
            pos = [node for node in spinsons if spinsons[node] == 1]
            neg = [node for node in spinsons if spinsons[node] == -1]
            magnetization[t] += ((len(pos)-len(neg))/len(spinsons)) #magnetization
    magnetization = [magnet / M for magnet in magnetization]
    return magnetization

p_ind = 0.5
T = 1000

G = nx.barabasi_albert_graph(n = 100, m = 4)
magnetization111 = MCsteps_magnetization_time(M = M, G = G, q = 3, T = T, p_ind= p_ind)
magnetization112 = MCsteps_magnetization_time(M = M, G = G, q = 4, T = T, p_ind= p_ind)

G = nx.watts_strogatz_graph(n = 100, k = 4, p= 0.01)
magnetization113 = MCsteps_magnetization_time(M = M, G = G, q = 3, T = T, p_ind= p_ind)
magnetization114 = MCsteps_magnetization_time(M = M, G = G, q = 4, T = T, p_ind= p_ind)

G = nx.watts_strogatz_graph(n = 100, k = 4, p= 0.2)
magnetization115 = MCsteps_magnetization_time(M = M, G = G, q = 3, T = T, p_ind= p_ind)
magnetization116 = MCsteps_magnetization_time(M = M, G = G, q = 4, T = T, p_ind= p_ind)

G = nx.complete_graph(n = 100)
magnetization117 = MCsteps_magnetization_time(M = M, G = G, q = 3, T = T, p_ind= p_ind)
magnetization118 = MCsteps_magnetization_time(M = M, G = G, q = 4, T = T, p_ind= p_ind)


fig5 = plt.figure(5)
plt.plot(range(T),magnetization111)
plt.plot(range(T),magnetization113)
plt.plot(range(T),magnetization115)
plt.plot(range(T),magnetization117)
plt.xlabel("t")
plt.ylabel('average magentization')
plt.title("Magnetization time evolution for q = 3")
plt.legend(("BA(N = 100, m = 4)","WS(N = 100, k = 4, p = 0.01)", "WS(N = 100, k = 4, p = 0.2)", "Complete(100)"))
plt.show()


fig6 = plt.figure(6)
plt.plot(range(T),magnetization112)
plt.plot(range(T),magnetization114)
plt.plot(range(T),magnetization116)
plt.plot(range(T),magnetization118)
plt.xlabel("t")
plt.ylabel('average magentization')
plt.title("Magnetization time evolution for q = 4")
plt.legend(("BA(N = 100, m = 4)","WS(N = 100, k = 4, p = 0.01)", "WS(N = 100, k = 4, p = 0.2)", "Complete(100)"))
plt.show()

