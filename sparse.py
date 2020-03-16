import numpy as np

class sparse():
    """
Class for sparse matrices
TODO: Implement matrix product, matrix acting on vector and kronecker product for sparse matrices
Assume all matrices considered are square
    """

    def __init__(self, m): #m = matrix
        if isinstance(m, np.ndarray):
            self.matrixDict = {}
            for x in range(len(m)):
                for y in range(len(m[0])):
                    if m[x][y] != 0:
                        self.matrixDict[(x,y)] = m[x][y]
            self.len = len(self.matrixDict)
            self.size = len(m)
        if isinstance(m, dict):
            self.matrixDict = m
            self.len = len(self.matrixDict)
            self.size = 0
            for pos in m:
                #print(self.size)
                #print(pos)
                if pos[0] > self.size:
                    self.size = pos[0]
                if pos[1] > self.size:
                    self.size = pos[1]
            self.size += 1


    def asMatrix(self):
        output = np.zeros((self.size,self.size))
        for pos in self.matrixDict:
            output[pos[0]][pos[1]] = self.matrixDict[pos] 
        return output
        

    def __str__(self):
        return str(self.asMatrix())
