import numpy as np
from scipy.sparse import csr_matrix

class Csr_sparse():
    """
Class for sparse matrices
TODO: Implement matrix product, matrix acting on vector and kronecker product for sparse matrices
Assume all matrices considered are square
    """

    def __init__(self, m): #m = matrix
        self.val = []
        self.row_pntr = []
        self.col = []
        self.dims = len(m)

        for i in range(len(m)):
            self.row_pntr.append(len(self.val))
            for j in range(len(m[i])):
                if m[i][j] != 0:
                    self.val.append(m[i][j])
                    self.col.append(j)
        self.row_pntr.append(len(self.val))

    def mult_vec(self, v): #multiply self with v, a vector
        P = [0]*self.dims
        for i in range(self.dims):
            for k in range(self.row_pntr[i], self.row_pntr[i+1]):
                P[i] += self.val[k]*v[self.col[k]]
        return P

    def mult_mat(self, m): #multiply self with m, another Csr_sparse matrix
        

m = 3*np.identity(5)
print(m)
s = Csr_sparse(m)
v = [1,0,0,0,0]
p = s.mult_vec(v)
print(p)
