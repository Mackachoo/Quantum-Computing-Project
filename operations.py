import numpy as np
import quantum_states as qs
import math as m
from time import time
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

sgates = {

    'H' : sp.Sparse(gates['H']),
    'I' : sp.Sparse(gates['I']),
    'X' : sp.Sparse(gates['X']),
    'Y' : sp.Sparse(gates['Y']),
    'Z' : sp.Sparse(gates['Z'])

}



### Matrix Addition!   -------------------------------------------------------------------------------------------------

def matrixSum(matA,matB):
    """ Function summing two matrices.

    Parameters
    ----------
    matA : numpy array or sp.Sparse
        First matrix in sum.
    matB : numpy array or sp.Sparse
        Second matrix in sum.

    Returns
    -------
    numpy array or sp.Sparse
        Sum of matA + matB.
    """

    if isinstance(matA, np.ndarray) & isinstance(matA, np.ndarray):
        if matA.shape != matB.shape:
            print("Non NxN matching matrices")
        else:
            matZ = np.zeros((matA.shape[0],matA.shape[1]))
            for i in range(matA.shape[0]):
                for j in range(matA.shape[1]):
                    matZ[i][j] = matA[i][j]+matB[i][j]
            return matZ
    elif isinstance(matA, sp.Sparse) & isinstance(matA, sp.Sparse):
        for b in matB.matrixDict:
            if b in matA.matrixDict:
                matA.matrixDict[b] += matB.matrixDict[b]
            else:
                matA.matrixDict[b] = matB.matrixDict[b]
        return matA
    else:
        print("ERROR 0 : Incorrect type for one or more matrices.")

### Matrix multiplication!   -------------------------------------------------------------------------------------------

def matrixProduct(matA,matB):
    """Two matrix multiplication function.

    Parameters
    ----------
    matA : numpy array or sp.Sparse
        Leftmost matrix in product.
    matB : numpy array or sp.Sparse
        Rightmost matrix in product.

    Returns
    -------
    numpy array or sp.Sparse
        Matrix being a product of (matA x matB).
    """

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
    elif isinstance(matA, sp.Sparse) & isinstance(matB, sp.Sparse):
        matZ = {}
        for a in matA.matrixDict:
            for b in matB.matrixDict:
                if a[0] == b[1]:
                    if (b[0],a[1]) in matZ:
                        matZ[(b[0],a[1])] += matA.matrixDict[a]*matB.matrixDict[b]
                    else:
                        matZ[(b[0],a[1])] = matA.matrixDict[a]*matB.matrixDict[b]
        return sp.Sparse(matZ, (matA.size[0],matB.size[1]))
    else:
        print("ERROR 1 : Incorrect type for one or more matrices.")


### Determinant of Matrix!   -------------------------------------------------------------------------------------------

def matrixDet(mat):
    """Calculates determinant of n-dimensional square matrix.

    Parameters
    ----------
    mat : numpy array or sp.Sparse
        Square matrix whose dterminant will be found.

    Returns
    -------
    int
        Determinant of inputted square matrix (mat).
    """

    if isinstance(mat, np.ndarray):
        return determinant(mat)
    elif isinstance(mat, sp.Sparse):
        #cons = np.array([ (-1)**((x+1)//2) for x in range(m.factorial(mat.size))])
        return determinant(mat.asMatrix)
    else:
        print("ERROR 2 : Incorrect type for matrix.")

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
    """
     Find the matrix inverse for square matrix mat.

    Parameters
    ----------
    mat : numpy array or sp.Sparse
        Matrix whose inverse will be found.

    Returns
    -------
    numpy array or sp.Sparse
        Inverted matrix whose operation reverses that of mat.
    """
    if isinstance(mat, np.ndarray):
        return inverter(mat[0])
    elif isinstance(mat, sp.Sparse):
        #cons = np.array([ (-1)**((x+1)//2) for x in range(m.factorial(mat.size))])
        return sp.Sparse(inverter(mat.asMatrix))
    else:
        print("ERROR 3 : Incorrect type for matrix.")


def inverter(mat):
    if mat.shape[0] != mat.shape[1]:
        print("ERROR 4 : Non NxN matrices")
    else:
        det = matrixDet(mat)
        matZ = np.zeros(mat.shape)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[0]):
                matN = np.delete(mat, i, 1)
                matN = np.delete(matN, j, 0)
                matZ[i][j] = (1/det)*(1-2*((i+j)%2))*matrixDet(matN)
        size = (mat.shape[0],mat.shape[1])
        return matZ, size


### Tensor Product   ---------------------------------------------------------------------------------------------------
#Input lists (e.g. if in 4d space, |2> = [0,0,1,0])
def tensorProduct(vecA,vecB):
    """Function calculating tensor product of two vectors in vectorial form

    Parameters
    ----------
    vecA : numpy array
        Leftmost vector in tensor product.
    vecB : numpy array
        Rightmost vector in tensor product.

    Returns
    -------
    numpy array
        Vector representing tensor product of vecA (x) vecB
    """

    lA = len(vecA)
    lB = len(vecB)
    T = np.zeros(lA*lB)
    for i in range (lA):
        for j in range (lB):
            T[i*lB+j] = vecA[i]*vecB[j]
    return T


def kroneckerProduct(matA,matB):
    """Function calculating the kronecker product between two matrices

    I.e. higher-dimensional tensor product.

    Parameters
    ----------
    matA : numpy array or sp.Sparse
        Leftmost matrix in kronecker product.
    matB : numpy array or sp.Sparse
        Rightmost array in product.

    Returns
    -------
    numpy array or sp.Sparse
        Kronecker product of matA (x) matB.
    """
    if isinstance(matA, np.ndarray) & isinstance(matB, np.ndarray):
        matZ = np.zeros((matA.shape[0]*matB.shape[0], matA.shape[1]*matB.shape[1]))
        for i in range(matZ.shape[0]):
            for j in range(matZ.shape[1]):
                matZ[i][j] = matA[i//matB.shape[0]][j//matB.shape[1]]*matB[i%matB.shape[0]][j%matB.shape[1]]
        return matZ
    elif isinstance(matA, sp.Sparse) & isinstance(matB, sp.Sparse):
        matZ = {}
        for a in matA.matrixDict:
            for b in matB.matrixDict:
                matZ[( b[0]+a[0]*matB.size[0] , b[1]+a[1]*matB.size[1] )] = matA.matrixDict[a]*matB.matrixDict[b]
        return sp.Sparse(matZ, (matA.size[0]*matB.size[0],matA.size[1]*matB.size[1]))
    else:
        print("ERROR 5 : Incorrect type for one or more matrices.")

### Helper Functions ----------------------------------------------------------------------------------------------------
def vecMatProduct(mat,vec):
    """ TODO: takes a matrix and a single array vector and formats them for the matrixProduct() function.

    Parameters
    ----------
    mat : numpy array or sp.Sparse
        2D Matrix.
    vec : numpy array or sp.Sparse
        1D Vector.

    Returns
    -------
    numpy array or sp.Sparse
        Formatted product.
    """
    if isinstance(mat, np.ndarray):
        vecR = np.resize(vec,(len(vec),1))
        return matrixProduct(mat,vecR)[:,0]
    elif isinstance(mat, sp.Sparse):           # Not entirely sure if this works.
        V = [0]*len(vec)
        for i in mat.matrixDict:
            V[i[0]] += mat.matrixDict[i]*vec[i[1]]
        return np.array(V)
    else:
        print("ERROR 6 : Incorrect type for matrix and/or vector.")


def constructGate(code, Sparse = False):
    """ Function constructing matrix representing gate dynamically

    Works by parsing a carefully formatted string representing the gate
    at each qubit and returns an array representing the operation

    Parameters
    ----------
    code : str
        Sequence/"code" used to generate specific gate matrix.

    Returns
    -------
    numpy array
        Matrix which when acted on a particular register will have the same
        effect as applying the theoretical quantum gate.
    """

    matrix = np.array([[1]])
    if Sparse:
        matrix = sp.Sparse(matrix)
    TofN = 0
    for char in code:
        if char.isdigit():
            TofN = int(str(TofN)+char)
        elif TofN != 0:
            if Sparse:
                gate = sgates[char]
                l = 2**TofN-gate.size[0]
                Tof = sp.Sparse(np.identity(l), (l+gate.size[0],l+gate.size[0]))
                for pos in gate.matrixDict:
                    Tof.matrixDict[((Tof.size[0])-(gate.size[0])+pos[0]%(gate.size[0]) , (Tof.size[1])-(gate.size[1])+pos[1]%(gate.size[1]))] = gate.matrixDict[(pos[0]%(gate.size[0]),pos[1]%(gate.size[1]))]
            else:
                Tof = np.identity(2**TofN)
                gate = gates[char]
                for x in range(len(gates)):
                    for y in range(len(gates)):
                        Tof[len(Tof)-len(gate)+x%len(gate)][len(Tof)-len(gate)+y%len(gate)] = gate[x%len(gate)][y%len(gate)]
            matrix = kroneckerProduct(matrix,Tof)
            TofN = 0
        else:
            if Sparse:
                matrix = kroneckerProduct(matrix,sgates[char])
            else:
                matrix = kroneckerProduct(matrix,gates[char])
    return matrix


"""
t0 = time()
X = constructGate('4Z')
t1 = time()
sX = constructGate('4Z', Sparse = True)
t2 = time()

#print(f"Original in {t1-t0} secs:\nNew in {t2-t1} secs:\n")
#print(f"{t0} -> {t1} -> {t2}")
#print(f"{len(X)}\n{sX.size}")
"""