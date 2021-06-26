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
filename="NDwww.net"
scriptpath = os.getcwd()
directory = 'graphs'
filepath = os.path.join(scriptpath,directory, filename)


print(' \n \n' + filename + ' graph \n ')
louvain_graph(filepath,typeG)

nbt, nbi, t0 = 250, 45000, 3


print('\n recuit simulé classique')
rs_graph(filepath,typeG, nbt, nbi, t0)


print('\n louvain + recuit simulé')
louvain_rs_graph(filepath,typeG, nbt, nbi, t0)

print(' \n  recuit simulé classique argmax')
rs_graph(filepath,typeG, nbt, nbi, t0, argmax=True)

print('\n louvain + recuit simulé argmax')
louvain_rs_graph(filepath,typeG, nbt, nbi, t0, argmax=True)
