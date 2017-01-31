__author__ = 'jbernardin'
import numpy as np


# A (X) B
def ten_prod(a, b):
    nj, nk = a.shape
    nl, nm = b.shape
    rows = nj + nl
    columns = nk + nm
    tp = np.zeros((rows, columns))
    for j in range(0, nj):
        for k in range(0, nk):
            for l in range(0, nl):
                for m in range(0, nm):
                    tp[(j-1)*nl+l, (k-1)*nk + m] = a[j, k]*b[l, m]
    return tp

