# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:43:33 2019

@author: micha
"""

import networkx as nx
import  numpy.random as rnd
import task1_summary

def RandomGraph(N, prob):
    G = nx.Graph()
    nodes = range(N)
    G.add_nodes_from(nodes)
    nodes = G.nodes()
    for i in G.nodes():
        for j in nodes:
            p = rnd.random()
            if p < prob and i != j:
                G.add_edge(i,j)
        nodes.remove(i)
    return G

#N= 2000
#prob = 0.1
#G = RandomGraph(N, prob)
#task1_summary.graph_summary(graph = G, N=N, graph_type="Random", p = prob)


def Watts_Strogatz(N, prob = 0.1):
    G = nx.Graph()
    nodes = range(N)
    G.add_nodes_from(nodes)
    for i in nodes: #creation of graph
        indeks = nodes.index(i)
        if indeks == 0:
            G.add_edge(i, nodes[indeks+1])
            G.add_edge(i, nodes[-1])
            G.add_edge(nodes[indeks+1], nodes[-1])
        elif indeks == len(nodes)-1:
            G.add_edge(i, nodes[indeks-1])
            G.add_edge(i, nodes[0])
            G.add_edge(nodes[indeks-1], nodes[0])
        else:
            G.add_edge(i, nodes[indeks+1])
            G.add_edge(i, nodes[indeks-1])
            G.add_edge(nodes[indeks+1], nodes[indeks-1])
    for ed in G.edges():
        p=rnd.random()
        if p < prob:
            G.remove_edge(ed[0],ed[1])
            possible_edges = [node for node in nodes if
                                    node != ed[0] and not G.has_edge(ed[0], node)]
            G.add_edge(ed[0], rnd.choice(possible_edges, size = 1)[0])
    return G

#N=2000
#prob = 0.2
#G = Watts_Strogatz(N, prob)
#task1_summary.graph_summary(graph = G, N=N, graph_type="Watts-Strogatz", p = prob, K = 4)


def Barabasi_Albert(N, m, m0):
    G = nx.Graph()
#    if m > start_nodes:
#        raise Exception("")
    nodes = range(N)
    start = nodes[:m0]
    nodes = nodes[m0:]
    for i in start: #tworzenie startowych wierzcholkow, laczenie wszystkich
        for j in start:
            if i != j:
                G.add_edge(i,j)
    for i in nodes:
        other_nodes = G.nodes()
        total_degree = sum(list(G.degree().values()))
        G.add_node(i)
        counter = 0
        while len(G.edges(i)) < m: 
            for j in other_nodes:
                prob = G.degree(j)/total_degree
                p = rnd.random()
                if p < prob:
                     G.add_edge(i,j)
                     counter+=1
    return G

N=2000
m = 2
m0 = 3
G = Barabasi_Albert(N, m, m0)
task1_summary.graph_summary(graph = G, N=N, graph_type="Barbasi-Albert", m0 = m0, m = m)


