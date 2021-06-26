import networkx as nx

import matplotlib.cm as cm
import matplotlib.pyplot as plt

from math import exp

import networkx as nx
import numpy as np

from community_status import Status

from community_louvain_Recuit import *

from community_ana import *

import os

typeG="edgelist"
filename="arxiv.txt"
scriptpath = os.getcwd()
directory = 'graphs'
filepath = os.path.join(scriptpath,directory, filename)


print(' \n \n' + filename + ' graph \n')
louvain_graph(filepath,typeG)

nbt, nbi, t0 = 1000, 1000, 3


print('\n recuit simulé classique')
rs_graph(filepath,typeG, nbt, nbi, t0)


print('\n louvain + recuit simulé')
louvain_rs_graph(filepath,typeG, nbt, nbi, t0)


print('\n louvain complet + recuit simulé')
completelouvain_rs_graph(filepath ,typeG, nbt, nbi, t0)

""" print(' \n  recuit simulé classique argmax')
rs_graph(filepath,typeG, nbt, nbi, t0, argmax=True)

print('\n louvain + recuit simulé argmax')
louvain_rs_graph(filepath,typeG, nbt, nbi, t0, argmax=True) """


 
""" 
Output: 

arxiv.txt graph 

ce graphe a 9377 sommets 
 
 louvain
time:  1.5236257149954326 secondes
modularity:  0.8143357349573429

 recuit simulé classique
time:  92.76065235799615 secondes
modularity:  0.7733281954060508

 louvain + recuit simulé
time:  341.1067785500054 secondes
modularity:  0.8001397146286021
 
  recuit simulé classique argmax
time:  106.18354641999758 secondes
modularity:  0.7727413899394063

 louvain + recuit simulé argmax
time:  358.59661056500045 secondes
modularity:  0.7997257336321888 """