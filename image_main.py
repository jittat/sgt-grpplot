from pylab import *
from random import random
from scipy import misc

from mat import adjmat, degmat
from generators import gen_random, gen_line
from grpplot import plot


def graph_data_from_image(image_filename):

    def node_num(x,y,sx,sy):
        return y*sx + x

    def randedge(cdiff):
        TR = 2.
        prob = (1.0 - (cdiff/255.)*TR)
        print prob,
        return random() <= prob

    img = misc.imread(image_filename)
    sy,sx = img.shape
    n = sx*sy

    DIRS = [(1,0),(0,1),(1,1),(-1,1)]

    adj = []
    for i in range(sx):
        for j in range(sy):
            c = int(img[j][i])
            num = node_num(i,j,sx,sy)

            for dx,dy in DIRS:

                ni = i + dx
                nj = j + dy
                if (ni >= sx) or (nj >= sy):
                    continue
                if (ni < 0) or (nj < 0):
                    continue
                
                nnum = node_num(ni,nj,sx,sy)
                nc = int(img[nj][ni])
                if randedge(abs(c - nc)):
                    adj.append((num, nnum))

    return n,adj,sx,sy

def sort_eig(w,v):
    indexing = w.argsort()
    return w[indexing], [transpose(vi) for vi in transpose(v[:,indexing])]

def main():
    n,adjlist,sx,sy = graph_data_from_image('ccc-s.png')
    print n, len(adjlist)

    a = adjmat(n,adjlist)
    d = degmat(n,adjlist)
    la = d - a
    w,v = eig(la)
    w,v = sort_eig(w,v)

    e2 = v[1]
    #e3 = v[2]

    px = []
    py = []
    for i in range(n):
        x = i % sx
        y = i / sx
        px.append(x)
        py.append(y)

    aa = adjmat(n,[])
    plot(n,aa,px,py,[e2[i,0]*100 for i in range(n)])
    raw_input()

if __name__ == '__main__':
    main()
