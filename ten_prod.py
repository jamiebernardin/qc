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
                    # print("i= " + str(i) + " k= " + str(k) + " l= " + str(l) + " m= " + str(m))
                    # print (str(i*nl+l) + " , " + str(k*nk +m))
                    tp[i*nl+l, k*nm + m] = a[i, k]*b[l, m]
    return tp