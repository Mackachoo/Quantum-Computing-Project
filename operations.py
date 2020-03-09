import numpy as np
import quantum_states as qs
import math as m

gates = {

    'H' : 1/m.sqrt(2)*np.array([[1,1],
                                [1,-1]]),
    'I' : np.identity(2),
    'X' : np.array([[0,1],
                    [1,0]]),
    'Y' : np.array([[0,-1j],
                    [1j,0]]),
    'Z' : np.array([[1,0],
                    [0,-1]])

}

### Matrix Addition!   -------------------------------------------------------------------------------------------------

def matrixSum(matA,matB):
    if matA.shape != matB.shape:
        print("Non NxN matching matrices")
    else:
        matZ = np.zeros((matA.shape[0],matA.shape[1]))
        for i in range(matA.shape[0]):
            for j in range(matA.shape[1]):
                matZ[i][j] = matA[i][j]+matB[i][j]
        return matZ


### Matrix multiplication!   -------------------------------------------------------------------------------------------

def matrixProduct(matA,matB):
    if matA.shape[1] != matB.shape[0]:
        print(f"Non axN Nxb matching matrices : {matA.shape[0]}x{matA.shape[1]} and {matB.shape[0]}x{matB.shape[1]}")
    else:
        matZ = np.zeros((matA.shape[0],matB.shape[1]))
        for i in range(matZ.shape[0]):
            for j in range(matZ.shape[1]):
                for n in range(matA.shape[1]):
                    matZ[i][j] += matA[i][n]*matB[n][j]
        return matZ


### Determinant of Matrix!   -------------------------------------------------------------------------------------------

def matrixDet(mat):
    if mat.shape[0] != mat.shape[1]:
        print("Non NxN matrices")
    else:
        if mat.shape[1] == 1:
            return mat[0][0]
        elif mat.shape[1] == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        else:
            tempNum = 0
            for rNum, rItem in enumerate(mat[0]):
                matN = np.delete(mat, 0, 0)
                matN = np.delete(matN, rNum, 1)
                tempNum += (1 - 2 * (rNum % 2)) * rItem * matrixDet(matN)
            return tempNum



### Matrix Inversion!   ------------------------------------------------------------------------------------------------

def matrixInv(mat):
    if mat.shape[0] != mat.shape[1]:
        print("Non NxN matrices")
    else:
        det = matrixDet(mat)
        matZ = np.zeros(mat.shape)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[0]):
                matN = np.delete(mat, i, 1)
                matN = np.delete(matN, j, 0)
                matZ[i][j] = (1/det)*(1-2*((i+j)%2))*matrixDet(matN)
        return matZ


### Tensor Product   ---------------------------------------------------------------------------------------------------
#Input lists (e.g. if in 4d space, |2> = [0,0,1,0])
def tensorProduct(vecA,vecB):
    lA = len(vecA)
    lB = len(vecB)
    T = np.zeros(lA*lB)
    for i in range (lA):
        for j in range (lB):
            T[i*lB+j] = vecA[i]*vecB[j]
    return T


def kroneckerProduct(matA,matB):
    #print()
    matZ = np.zeros((matA.shape[0]*matB.shape[0], matA.shape[1]*matB.shape[1]))
    #print(matA.shape[0],matA.shape[1],matB.shape[0],matB.shape[1])
    for i in range(matZ.shape[0]):
        for j in range(matZ.shape[1]):
            #print(i,j)
            matZ[i][j] = matA[i//matB.shape[0]][j//matB.shape[1]]*matB[i%matB.shape[0]][j%matB.shape[1]]
    return matZ


### Helper Functions ----------------------------------------------------------------------------------------------------
def vecToState(vec):
    """TODO: takes vector spits out tuple (denary, dimension)"""
    pass


def vecMatProduct(mat,vec):
    """TODO: takes a matrix and a single array vector and formats them for the matrixProduct() function."""
    vecR = np.resize(vec,(len(vec),1))
    return matrixProduct(mat,vecR)[:,0]


def constructGate(code):
    matrix = np.array([[1]])
    TofN = 0
    for char in code:
        if char.isdigit():
            TofN = int(char)
        elif TofN != 0:
            Tof = np.identity(2**TofN)
            gate = gates[char]
            for x in range(len(gates)):
                for y in range(len(gates)):
                    Tof[len(Tof)-len(gate)+x%len(gate)][len(Tof)-len(gate)+y%len(gate)] = gate[x%len(gate)][y%len(gate)]
            matrix = kroneckerProduct(matrix,Tof)
            TofN = 0
        else:
            matrix = kroneckerProduct(matrix,gates[char])
    return matrix
