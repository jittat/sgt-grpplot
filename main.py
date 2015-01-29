from pylab import *
from random import random

from mat import adjmat, degmat
from generators import gen_random, gen_line
from grpplot import plot

def sort_eig(w,v):
    indexing = w.argsort()
    return w[indexing], [transpose(vi) for vi in transpose(v[:,indexing])]

def main():
    n = 100
    #adjlist = gen_line(n)
    adjlist = gen_random(n,500)
    a = adjmat(n,adjlist)
    d = degmat(n,adjlist)
    la = d - a
    w,v = eig(la)
    w,v = sort_eig(w,v)
    print w

    e2 = v[1]
    e3 = v[2]
    
    px = [e2[i,0] for i in range(n)]
    #py = [random() for i in range(n)]
    py = [e3[i,0] for i in range(n)]

    plot(n,a,px,py)
    raw_input()

if __name__ == '__main__':
    main()
