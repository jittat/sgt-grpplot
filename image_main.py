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
        prob = (1.0 - (cdiff/256.))*10
        return random() <= prob

    img = misc.imread(image_filename)
    sy,sx = img.shape
    n = sx*sy

    adj = []
    for i in range(sx):
        for j in range(sy):
            c = int(img[j][i])
            num = node_num(i,j,sx,sy)
            if i != sx - 1:
                rnum = node_num(i+1,j,sx,sy)
                rc = int(img[j][i+1])
                if randedge(abs(c - rc)):
                    adj.append((num, rnum))
            if j != sy - 1:
                dnum = node_num(i,j+1,sx,sy)
                dc = int(img[j+1][i])
                if randedge(abs(c - dc)):
                    adj.append((num, dnum))
    return n,adj,sx,sy

def sort_eig(w,v,n):
    data = [(w[i],i) for i in range(n)]
    sdata = sorted(data)
    outw = [sdata[i][0] for i in range(n)]
    outv = [v[:,sdata[i][1]] for i in range(n)]
    return outw, outv

def main():
    n,adjlist,sx,sy = graph_data_from_image('lena-s.png')
    print n, len(adjlist)

    a = adjmat(n,adjlist)
    d = degmat(n,adjlist)
    la = d - a
    w,v = eig(la)
    print w
    w,v = sort_eig(w,v,n)
    print w

    e2 = v[1]
    e3 = v[2]
    
    px = [e2[i,0] for i in range(n)]
    py = [random() for i in range(n)]

    plot(n,a,px,py)
    raw_input()

if __name__ == '__main__':
    main()
