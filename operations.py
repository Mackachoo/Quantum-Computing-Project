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
    """ Function summing two matrices.

    Parameters
    ----------
    matA : numpy array
        First matrix in sum.
    matB : numpy array
        Second matrix in sum.

    Returns
    -------
    numpy array
        Sum of matA + matB.
    """
    
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
    """Two matrix multiplication function.

    Parameters
    ----------
    matA : numpy array
        Leftmost matrix in product.
    matB : numpy array
        Rightmost matrix in product.

    Returns
    -------
    numpy array
        Matrix being a product of (matA x matB).
    """

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
    """Calculates determinant of n-dimensional square matrix.

    Parameters
    ----------
    mat : numpy array
        Square matrix whose dterminant will be found.

    Returns
    -------
    int
        Determinant of inputted square matrix (mat).
    """

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
    """Find the matrix inverse for square matrix mat.

    Parameters
    ----------
    mat : numpy array
        Matrix whose inverse will be found.

    Returns
    -------
    numpy array
        Inverted matrix whose operation reverses that of mat.
    """

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
    matA : numpy array
        Leftmost matrix in kronecker product.
    matB : numpy array
        Rightmost array in product.

    Returns
    -------
    numpy array
        Kronecker product of matA (x) matB.
    """

    matZ = np.zeros((matA.shape[0]*matB.shape[0], matA.shape[1]*matB.shape[1]))
    for i in range(matZ.shape[0]):
        for j in range(matZ.shape[1]):
            matZ[i][j] = matA[i//matB.shape[0]][j//matB.shape[1]]*matB[i%matB.shape[0]][j%matB.shape[1]]
    return matZ


### Helper Functions ----------------------------------------------------------------------------------------------------
def vecMatProduct(mat,vec):
    """ TODO: takes a matrix and a single array vector and formats them for the matrixProduct() function.

    Parameters
    ----------
    mat : numpy array
        2D Matrix.
    vec : numpy array
        1D Vector.

    Returns
    -------
    numpy array
        Formatted product.
    """

    vecR = np.resize(vec,(len(vec),1))
    return matrixProduct(mat,vecR)[:,0]


def constructGate(code):
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
