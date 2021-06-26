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


filename="karate.txt"
scriptpath = os.getcwd()
directory = 'graphs'
filepath = os.path.join(scriptpath,directory, filename)


typeG="edgelist"
print(' \n \n' + filename + ' graph \n')
louvain_graph(filepath,typeG)

nbt, nbi, t0 = 300, 200, 20


print('\n recuit simulé classique')
rs_graph(filepath,typeG, nbt, nbi, t0)


print('\n louvain + recuit simulé')
louvain_rs_graph(filepath ,typeG, nbt, nbi, t0) 

print('\n louvain complet + recuit simulé')
completelouvain_rs_graph(filepath ,typeG, nbt, nbi, t0)

"""
print(' \n  recuit simulé classique argmax')
rs_graph(filepath ,typeG, nbt, nbi, t0, argmax=True)

print('\n louvain + recuit simulé argmax')
louvain_rs_graph(filepath ,typeG, nbt, nbi, t0, argmax=True)
 """

""" 
Output:

 
karate.txt graph 

ce graphe a 34 sommets 
 
louvain
time:  0.002226700999017339 secondes
modularity:  0.4269691347613425

 recuit simulé classique
time:  0.4536876359998132 secondes
modularity:  0.3831168831168831

 louvain + recuit simulé
time:  0.4215870359985274 secondes
modularity:  0.3831168831168831
 
  recuit simulé classique argmax
time:  0.44197298400104046 secondes
modularity:  0.3831168831168831

 louvain + recuit simulé argmax
time:  0.41822954400413437 secondes
modularity:  0.3831168831168831
"""