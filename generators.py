from random import random, randint

def gen_random(n,m):
    adjlist = []
    for i in range(m):
        if random() > 0.95:
            adjlist.append((randint(0,n-1),randint(0,n-1)))
        else:
            if random()>0.5:
                adjlist.append((randint(0,n/2 - 1),randint(0,n/2 - 1)))
            else:
                adjlist.append((randint(n/2,n-1),randint(n/2,n-1)))
    return adjlist

def gen_line(n):
    adjlist = []
    for i in range(n-1):
        adjlist.append((i,i+1))
    return adjlist

