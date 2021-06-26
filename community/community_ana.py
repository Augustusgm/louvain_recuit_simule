import networkx as nx
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time
from community_status import Status
from community_louvain_Recuit import *

def g_nx(name, typeG):
    if typeG == "edgelist":
        return nx.read_edgelist(name, nodetype=int)
    if typeG == 'adjlist':
        return nx.read_adjlist(name)

def ttt(t):
    return 0.9*t


def rs_graph(name,typeG, nbt, nbi, t0, tt=ttt, show=True, plot=False, timit=True, argmax=False):
    """find partition using Recuit simulé

    Parameters
    ----------
    name : str | name of the file containing the graph
    typeG : str | edgelist if graph stored in edgelist format or adjlist if graph stored as adjlist
    show : True | bool | to give the modularity of the partition
    plot : False | bool | to plot the partition
    timit: True | bool | print time taken for partitioning
    """
    G=g_nx(name,typeG)
    if timit:
        t1=time.perf_counter()
    partition = best_partition_rs(G, nbt, nbi, t0, tt, argmax)
    if timit:
        t2=time.perf_counter()
        print('time: ', t2-t1, 'secondes')
    if show:
        print('modularity: ',modularity(partition, G))
    if plot:
        pos = nx.spring_layout(G)
        cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
        nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, 
                                cmap=cmap, node_color=list(partition.values()))
        nx.draw_networkx_edges(G, pos, alpha=0.5)
        plt.title(name + '  rs')
        plt.show()
    return #G, partition


def louvain_graph(name,typeG, show=True, plot=False, timit=True):
    """find partition using thelouvain algorithm

    Parameters
    ----------
    name : str | name of the file containing the graph
    typeG : str | edgelist if graph stored in edgelist format or adjlist if graph stored as adjlist
    show : True | bool | to give the modularity of the partition
    plot : False | bool | to plot the partition
    timit: True | bool | print time taken for partitioning

    """
    G=g_nx(name,typeG)
    print('ce graphe a ' + str(len(G.nodes())) + ' sommets \n \n louvain')
    if timit:
        t1=time.perf_counter()
    partition = best_partition(G)
    if timit:
        t2=time.perf_counter()
        print('time: ', t2-t1, 'secondes')
    if show:
        print('final modularity: ', modularity(partition, G))
    if plot:
        pos = nx.spring_layout(G)
        cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
        nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, 
                                cmap=cmap, node_color=list(partition.values()))
        nx.draw_networkx_edges(G, pos, alpha=0.5)
        plt.title(name + '  louvain')
        plt.show()
    return #G, partition

def louvain_rs_graph(name,typeG, nbt, nbi, t0, tt=ttt, show=True, plot=False, timit=True, argmax=False):
    """find partition using louvain and then Recuit simulé at each level

    Parameters
    ----------
    name : str | name of the file containing the graph
    typeG : str | edgelist if graph stored in edgelist format or adjlist if graph stored as adjlist
    show : True | bool | to give the modularity of the partition
    plot : False | bool | to plot the partition
    timit: True | bool | print time taken for partitioning
    """
    G=g_nx(name,typeG)
    if timit:
        t1=time.perf_counter()
    partition = best_partition_louvain_rs(G, nbt, nbi, t0, tt, argmax)
    if timit:
        t2=time.perf_counter()
        print('time: ', t2-t1, 'secondes')
    if show:
        print('modularity: ',modularity(partition, G))
    if plot:
        pos = nx.spring_layout(G)
        cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
        nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, 
                                cmap=cmap, node_color=list(partition.values()))
        nx.draw_networkx_edges(G, pos, alpha=0.5)
        plt.title(name + '  louvain+rs')
        plt.show()
    return #G, partition


def completelouvain_rs_graph(name,typeG, nbt, nbi, t0, tt=ttt, show=True, plot=False, timit=True, argmax=False):
    """find partition using louvain and then recuit simulé with initial state the final partition of louvain

    Parameters
    ----------
    name : str | name of the file containing the graph
    typeG : str | edgelist if graph stored in edgelist format or adjlist if graph stored as adjlist
    show : True | bool | to give the modularity of the partition
    plot : False | bool | to plot the partition
    timit: True | bool | print time taken for partitioning
    """
    G=g_nx(name,typeG)
    if timit:
        t1=time.perf_counter()
    partition = best_partition_louvain_then_rs(G, nbt, nbi, t0, tt, argmax)
    if timit:
        t2=time.perf_counter()
        print('time: ', t2-t1, 'secondes')
    if show:
        print('modularity: ',modularity(partition, G))
    if plot:
        pos = nx.spring_layout(G)
        cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
        nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, 
                                cmap=cmap, node_color=list(partition.values()))
        nx.draw_networkx_edges(G, pos, alpha=0.5)
        plt.title(name + '  louvain+rs')
        plt.show()
    return #G, partition
