import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from itertools import zip_longest

def epidemic(G,start_node,probability):
    I = []
    R = []  
    I = I + [start_node]
    frac = []
    while len(I) != 0:
        newI = []
        frac = frac + [len(I)/nx.number_of_nodes(G)]
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

    return frac


# lattice graph
figure1 = plt.figure(figsize=(15,5))
infected_avg = []
N=1000
for i in range(N):
    n = 15
    G = nx.grid_2d_graph(n,n)
    probability = 0.3
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac1 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac1)

infected_avg = []
N=1000
for i in range(N):
    n = 15
    G = nx.grid_2d_graph(n,n)
    probability = 0.5
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac2 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac2)

infected_avg = []
N=1000
for i in range(N):
    n = 15
    G = nx.grid_2d_graph(n,n)
    probability = 0.7
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac3 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac3)

plt.legend(('p=0.3','p=0.5','p=0.7'))
plt.xlabel('t')
plt.ylabel('fraction of infected')
plt.title('lattice graph')
plt.show()


# random graph
figure2 = plt.figure(figsize=(15,5))
infected_avg = []
N=1000
for i in range(N):
    n=100
    p=0.05
    G = nx.gnp_random_graph(n,p)
    probability = 0.3
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac1 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac1)

infected_avg = []
N=1000
for i in range(N):
    n=100
    p=0.05
    G = nx.gnp_random_graph(n,p)
    probability = 0.5
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac2 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac2)

infected_avg = []
N=1000
for i in range(N):
    n=100
    p=0.05
    G = nx.gnp_random_graph(n,p)
    probability = 0.7
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac3 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac3)

plt.legend(('p=0.3','p=0.5','p=0.7'))
plt.xlabel('t')
plt.ylabel('fraction of infected')
plt.title('random graph')
plt.show()


# watts-strogatz graph
figure3 = plt.figure(figsize=(15,5))
infected_avg = []
N=1000
for i in range(N):
    n=40
    k=4
    p=0.7
    G = nx.watts_strogatz_graph(n, k, p)
    probability = 0.3
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac1 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac1)

infected_avg = []
N=1000
for i in range(N):
    n=40
    k=4
    p=0.7
    G = nx.watts_strogatz_graph(n, k, p)
    probability = 0.5
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac2 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac2)

infected_avg = []
N=1000
for i in range(N):
    n=40
    k=4
    p=0.7
    G = nx.watts_strogatz_graph(n, k, p)
    probability = 0.7
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac3 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac3)

plt.legend(('p=0.3','p=0.5','p=0.7'))
plt.xlabel('t')
plt.ylabel('fraction of infected')
plt.title('watts-strogatz graph')
plt.show()


# barabasi-albert graph
figure3 = plt.figure(figsize=(15,5))
infected_avg = []
N=1000
for i in range(N):
    n=40
    m=4
    G = nx.barabasi_albert_graph(n, m)
    probability = 0.3
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac1 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac1)

infected_avg = []
N=1000
for i in range(N):
    n=40
    m=4
    G = nx.barabasi_albert_graph(n, m)
    probability = 0.5
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac2 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac2)

infected_avg = []
N=1000
for i in range(N):
    n=40
    m=4
    G = nx.barabasi_albert_graph(n, m)
    probability = 0.7
    start_node = random.choice(list(G.nodes()))
    infected = epidemic(G,start_node,probability)
    infected_avg.append((infected[:]))
avg_frac3 = [sum(n)/N for n in zip_longest(*infected_avg, fillvalue=0)]
plt.plot(avg_frac3)

plt.legend(('p=0.3','p=0.5','p=0.7'))
plt.xlabel('t')
plt.ylabel('fraction of infected')
plt.title('barabasi-albert graph')
plt.show()