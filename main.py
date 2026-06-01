from utile import *
from dijkstra import *
from bellman_ford import *

M = graphe2(5, 0.4, -5, 10)
print(M)
bellman_ford_pp(M, 0)