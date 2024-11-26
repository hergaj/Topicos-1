import numpy as np
import random

def lattice(n):
    lattice = np.zeros((n,n), dtype=int)
    return lattice

def vecinos(i,j, n, l):
    vecinos=[
        [(i-1)%n,j],
        [(i+1)%n,j],
        [i,(j-1)%n],
        [i,(j+1)%n]]
    return vecinos

def seed(n):
    l = lattice(n)
    for i in range(n):
        for j in range(n):
            l[i,j] = int(2*np.random.random())
    return l