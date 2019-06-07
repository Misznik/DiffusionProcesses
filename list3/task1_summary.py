import statistics
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import powerlaw
import scipy.stats
import seaborn as sns
import math
from scipy.special import binom
import sys

def graph_summary(graph, N, graph_type, p = 0, K = 0, m0 =0, m = 0):
    nodes_count = len(graph.nodes())
    edges_count = len(graph.edges())
    degrees = list(graph.degree().values())
    print("No. of nodes: %d" % nodes_count)
    print("No. of edges: %d" % edges_count)
    print("Avg. degree: %.2f" % np.mean(degrees))
    print("Var. of the degree: %.2f" % np.var(degrees))
    print('Highest degrees:',sorted(graph.degree().items(), reverse = True, key=lambda x: x[1])[0:15])

    if graph_type == "Random":
        
        distribution = scipy.stats.binom(N, p)
        print("Theoritical:")
        print("No. of nodes: %d" % N)
        print("No. of edges: %d" % (p * N * (N - 1) / 2))
        print("Avg. degree: %.2f" % (p * (N - 1)))
        print("Var. of the degree: %.2f" % (p * (1 - p) * (N - 1)))
        
    elif graph_type == "Watts-Strogatz":
        xk = np.arange(50, dtype=int)
        K_half = int(K / 2)
        pk = [sum([binom(K_half, n) * (1 - p) ** n * p ** (K_half - n) * (p * K_half) ** 
                   (k - K_half - n) / math.factorial(k - K_half - n) * math.exp(-p * K_half) 
                   for n in range(min(k - K_half, K_half) + 1)]) 
                                for k in xk]
    
        distribution = scipy.stats.rv_discrete(values=(xk, pk))
        print("Theoritical:") #aint dat too fancy?
        print("No. of nodes: %d" % N)
        print("No. of edges: %d" % (K * N / 2))
        print("Avg. degree: %.2f" % distribution.mean())
        print("Var. of the degree: %.2f" % distribution.var())
        
    elif graph_type == "Barbasi-Albert":
        data = np.array(degrees)
        minimum = min(data)
        maximum = max(data)
        (alpha, loglikelihood) = powerlaw.distribution_fit(data, distribution="power_law",
                                                          xmin=minimum, xmax=maximum, discrete=True)

        xk = np.arange(minimum, maximum, dtype=int)
        pk = [(alpha[0] - 1) / minimum * (k / minimum) ** -alpha[0] for k in xk]
        
        distribution = scipy.stats.rv_discrete(values=(xk, [prob / sum(pk) for prob in pk]))
        print("Theoritical:")
        print("No. of nodes: %d" % N)
        print("No. of edges: %d" % (m0 + (N - m0) * m)) #m0 + m*t
        print("Avg. degree: %.2f" % distribution.mean())
        print("Var. of the degree: %.2f" % distribution.var())
        
    graph_histogram(degrees, graph_type, distribution)
        
    
def graph_histogram(degrees, graph_type, distribution):
    x = np.arange(distribution.ppf(0.0001), distribution.ppf(0.9999))
    draw_dens=True
    if graph_type == "Barbasi-Albert":
        x = np.arange(distribution.ppf(0.001), distribution.ppf(0.999))
    elif graph_type == "Watts-Strogatz":
        draw_dens=False
    sns.distplot(degrees, norm_hist=True, bins=x - 0.5, kde=draw_dens, label = "empirical")
    plt.title("graph degree distribution for %s" % graph_type)
    plt.plot(x, distribution.pmf(x), color="red", marker='o',markersize=5, 
             linestyle='none', label = "theoritical")
    plt.legend()
    plt.show()
