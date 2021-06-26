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

typeG="adjlist"
filename="NDyeast.net"
scriptpath = os.getcwd()
directory = 'graphs'
filepath = os.path.join(scriptpath,directory, filename)


print(' \n \n' + filename + ' graph \n ')
louvain_graph(filepath,typeG)

nbt, nbi, t0 = 250, 15000, 3


print('\n recuit simulé classique')
rs_graph(filepath,typeG, nbt, nbi, t0)


print('\n louvain + recuit simulé')
louvain_rs_graph(filepath,typeG, nbt, nbi, t0)

print(' \n  recuit simulé classique argmax')
rs_graph(filepath,typeG, nbt, nbi, t0, argmax=True)

print('\n louvain + recuit simulé argmax')
louvain_rs_graph(filepath,typeG, nbt, nbi, t0, argmax=True)


""" Output:

NDyeast.net graph 
 
ce graphe a 1873 sommets 
 
louvain
time :  0.19080102499719942 secondes
modularity :  0.8483321591186747

 recuit simulé classique
time :  18.35242026499327 secondes
modularity :  0.8322465103085508

 louvain + recuit simulé
time :  35.66328853500454 secondes
modularity :  0.7955185146929712
 
  recuit simulé classique argmax
time :  18.66160275600123 secondes
modularity :  0.827729509504586

 louvain + recuit simulé argmax
time :  36.27400788200612 secondes
modularity :  0.7901644041836986 """