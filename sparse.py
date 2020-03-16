import numpy as np
import scipy.sparse as sp

class Csr_sparse():
    """
Class for sparse matrices
TODO: Implement matrix product, matrix acting on vector and kronecker product for csr_sparse matrices
Assume all matrices considered are square
    """

    def __init__(self, m): #m = matrix
        self.csr = sp.csr_matrix(m)

    def mult_vec(self, v): #multiply self with v, a vector
        return Csr_sparse(self.csr.dot(v))

    def mult_mat(self, m): #multiply self with m, a Csr_matrix
        return Csr_sparse(self.csr.dot(m.csr))

    def kronecker(self, m): #returns the kronecker product with anoher Csr_sparse
        val = self.csr.data
        row_pntr = self.csr.indptr
        col = self.csr.indices
        d = self.csr.shape[0]
        v = []
        rp = []
        c = []
        for i in range(d):
            for k in range(row_pntr[i], row_pntr[i+1]):




m = 3*np.identity(5)

s = Csr_sparse(m)
p = s.mult_mat(s)
s.kronecker(s)
