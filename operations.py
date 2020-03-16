import numpy as np
import quantum_states as qs
import math as m
import sparse as sp

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
    if isinstance(matA, np.ndarray) & isinstance(matA, np.ndarray):
        if matA.shape != matB.shape:
            print("Non NxN matching matrices")
        else:
            matZ = np.zeros((matA.shape[0],matA.shape[1]))
            for i in range(matA.shape[0]):
                for j in range(matA.shape[1]):
                    matZ[i][j] = matA[i][j]+matB[i][j]
            return matZ
    elif isinstance(matA, sp.sparse) & isinstance(matA, sp.sparse):
        for b in matB.matrixDict:
            if b in matA.matrixDict:
                matA.matrixDict[b] += matB.matrixDict[b]
            else:
                matA.matrixDict[b] = matB.matrixDict[b]
        return matA
    else:
        print("ERROR : Incorrect type for one or more matrices.")

### Matrix multiplication!   -------------------------------------------------------------------------------------------

def matrixProduct(matA,matB):
    if isinstance(matA, np.ndarray) & isinstance(matB, np.ndarray):
        if matA.shape[1] != matB.shape[0]:
            print(f"Non axN Nxb matching matrices : {matA.shape[0]}x{matA.shape[1]} and {matB.shape[0]}x{matB.shape[1]}")
        else:
            matZ = np.zeros((matA.shape[0],matB.shape[1]))
            for i in range(matZ.shape[0]):
                for j in range(matZ.shape[1]):
                    for n in range(matA.shape[1]):
                        matZ[i][j] += matA[i][n]*matB[n][j]
            return matZ
    elif isinstance(matA, sp.sparse) & isinstance(matB, sp.sparse):
        matZ = {}
        for a in matA.matrixDict:
            for b in matB.matrixDict:
                if a[0] == b[1]:
                    if (b[0],a[1]) in matZ:
                        matZ[(b[0],a[1])] += matA.matrixDict[a]*matB.matrixDict[b]
                    else:
                        matZ[(b[0],a[1])] = matA.matrixDict[a]*matB.matrixDict[b]   
        return sp.sparse(matZ)            
    else:
        print("ERROR : Incorrect type for one or more matrices.")


### Determinant of Matrix!   -------------------------------------------------------------------------------------------

def matrixDet(mat):
    if isinstance(mat, np.ndarray):
        return determinant(mat)
    elif isinstance(mat, sp.sparse):
        #cons = np.array([ (-1)**((x+1)//2) for x in range(m.factorial(mat.size))])
        return determinant(mat.matrixDict)
    else:
        print("ERROR : Incorrect type for matrix.")
            
def determinant(mat):
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
    if isinstance(mat, np.ndarray):
        return inverter(mat)
    elif isinstance(mat, sp.sparse):
        #cons = np.array([ (-1)**((x+1)//2) for x in range(m.factorial(mat.size))])
        return sp.sparse(inverter(mat.matrixDict))
    else:
        print("ERROR : Incorrect type for matrix.")


def inverter(mat):
    if mat.shape[0] != mat.shape[1]:
        print("ERROR : Non NxN matrices")
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
def vecMatProduct(mat,vec):
    """TODO: takes a matrix and a single array vector and formats them for the matrixProduct() function."""
    vecR = np.resize(vec,(len(vec),1))
    return matrixProduct(mat,vecR)[:,0]


def constructGate(code):
    """ This takes a code representing the gate at each qubit and returns an array representing the operation"""
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

"""

a = 3*np.identity(4)
b = np.array([[1,0,0,1],[5,6,0,0],[0,0,0,0],[0,0,5,0]])
#print(a)
#print(b)
sa = sp.sparse(a)
sb = sp.sparse(b)
print(f"{sa}\n\n  X\n\n{sb}\n\n  =\n\n")
print(f"Correct:\n{matrixProduct(a,b)}\n\nTest:\n{matrixProduct(sa,sb)}")

"""

