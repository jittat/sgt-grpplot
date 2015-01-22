from pylab import *

def adjmat(n, adjlist, is_asymmetric=False):
    adj = [[0 for i in range(n)] for j in range(n)]
    for u,v in adjlist:
        adj[u][v] += 1
        if not is_asymmetric:
            adj[v][u] += 1
    return matrix(adj)

def degmat(n, adjlist, is_asymmetric=False):
    deg = [[0 for i in range(n)] for j in range(n)]
    for u,v in adjlist:
        deg[u][u] += 1
        if not is_asymmetric:
            deg[v][v] +=1
    return matrix(deg)

