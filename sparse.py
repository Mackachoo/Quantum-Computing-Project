import numpy as np

class Sparse():
    """
Class for Sparse matrices
TODO: Implement matrix product, matrix acting on vector and kronecker product for csr_Sparse matrices
Assume all matrices considered are square
    """

    def __init__(self, m, s = None): # Takes m which is a square matrix or dictionary and an optional parameter s for the size of matrix.
        if isinstance(m, np.ndarray):
            self.matrixDict = {}
            for x in range(len(m)):
                for y in range(len(m[0])):
                    if m[x][y] != 0:
                        self.matrixDict[(x,y)] = m[x][y]
            self.len = len(self.matrixDict)
            self.size = (len(m),len(m[0]))
        if isinstance(m, dict):
            self.matrixDict = m
            self.len = len(self.matrixDict)
            if s != None:
                self.size = s
            else:                    # Guesses the matrix size if none given.
                self.size = (0,0)
                for pos in m:
                    #print(self.size)
                    #print(pos)
                    if pos[0] > self.size[0]:
                        self.size[0] = pos[0]
                    if pos[1] > self.size[1]:
                        self.size[1] = pos[1]
                self.size[0] += 1
                self.size[1] += 1


    def asMatrix(self):
        output = np.zeros((self.size[0],self.size[1]))
        for pos in self.matrixDict:
            output[pos[0]][pos[1]] = self.matrixDict[pos]
        return output


    def __str__(self):
        return str(self.asMatrix())
