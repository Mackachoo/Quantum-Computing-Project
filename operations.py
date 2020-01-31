import numpy as np

A = np.array([[3,4],[7,2],[9,1]])
B = np.array([[1,2,3],[5,6,7]])
C = np.array([[2,3,6],[6,2,5],[3,6,3]])


### Matrix Addition!   -------------------------------------------------------------------------------------------------

def matrixAdder(matA,matB):
    if matA.shape != matB.shape:
        print("Non NxN matching matrices")
    else:
        matZ = np.zeros((matA.shape[0],matA.shape[1]))
        for i in range(matA.shape[0]):
            for j in range(matA.shape[1]):
                matZ[i][j] = matA[i][j]+matB[i][j]
        return matZ


### Matrix multiplication!   -------------------------------------------------------------------------------------------

def matrixMulti(matA,matB):
    if matA.shape[1] != matB.shape[0]:
        print("Non axN Nxb matching matrices")
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