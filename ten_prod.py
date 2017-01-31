__author__ = 'jbernardin'
from sympy import Matrix, zeros


# A (X) B
def ten_prod(a, b):
    nj, nk = a.shape
    nl, nm = b.shape
    rows = nj * nl
    columns = nk * nm
    tp = zeros(rows, columns)
    for i in range(0, nj):
        for k in range(0, nk):
            for l in range(0, nl):
                for m in range(0, nm):
                    tp[i*nl+l, k*nk + m] = a[i, k]*b[l, m]
    return tp

