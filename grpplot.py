from pylab import *

def plot(n, adjmat, px, py, c=None):
    lines = []
    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            if adjmat[i,j]!=0:
                #print i,j
                #print ((px[i],py[i]),(px[j],py[j]))
                lines.append(((px[i],py[i]),(px[j],py[j])))
    ax = gca()
    ax.add_collection(matplotlib.collections.LineCollection(lines))
    if c:
        ax.scatter(px, py, c=c)
    else:
        ax.scatter(px, py)
    plt.ion()
    plt.draw_if_interactive()
    plt.hold(True)

