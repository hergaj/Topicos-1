import numpy as np

from seed import vecinos

def trees(l,p):
    n = len(l)
    for i in range(n):
        for j in range(n):
            e = np.random.random()
            if p >= e and l[i][j] == 0:
                l[i,j] = 1.0
    return l

def fire(l,p):
    n = len(l)
    for i in range(n):
        for j in range(n):
            e = np.random.random()
            if p >= e and l[i,j] == 1:
                l[i,j] = 2.0
    return l


def wildfire(l):
    n = len(l)
    nl = l.copy()
    for i in range(n):
        for j in range(n):
            if l[i,j] == 2.0:
                for x,y in vecinos(i,j,n,l):
                    if l[x,y] == 1.0:
                        nl[x,y] = 2.0
    return nl

def heal(l):
    n = len(l)
    nl = l.copy()
    for i in range(n):
        for j in range(n):
            if not any(l[x,y] == 1.0 for x,y in vecinos(i,j,n,l)) and l[i,j] == 2.0:
                nl[i,j] = 0.0
    return nl