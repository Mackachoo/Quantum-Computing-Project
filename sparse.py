import numpy as np

class Sparse():
    """ Class used for custom handling of sparse matrices.

    Parameters
    ----------
    m : numpy array or dictionary
        normal sparse matrix (including 0s) to convert to efficient representation.
    s : tuple
        optional (default None), denotes size of matrix (width, height).

    Attributes
    ----------
    matrixDict : dictionary
        efficient representation of sparse matrix as dictionary.
    len : int
        length of matrixDict, i.e. number of key:value pairs (non-zero elements).
    size : tuple
        stores size of original matrix, i.e. including 0s, as (width, height).

    Methods
    -------
    asMatrix(self)
        returns original matrix as a numpy array, i.e including 0 elements.
    __str__(self)
        string representation of the sparse matrix. I.e as original numpy array
        stringified and including 0 elements.
    """

    def __init__(self, m, s = None):

        if isinstance(m, np.ndarray):
            self.matrixDict = {}
            for x in range(len(m)):
                for y in range(len(m[0])):
                    if m[x][y] != 0:
                        self.matrixDict[(x,y)] = m[x][y]
        elif isinstance(m, dict):
            self.matrixDict = m
        else:
            raise TypeError("To create sparse matrix need numpy array or dictionary please") #Pleaseeee

        self.len = len(self.matrixDict)
        if s != None:
            self.size = s
        elif isinstance(m, np.ndarray):
            self.size = (len(m),len(m[0]))

        # Calculates the matrix size (if none given) by parsing given matrix.
        else:
            self.size = (0,0)
            for pos in m:
                if pos[0] > self.size[0]:
                    self.size[0] = pos[0]
                if pos[1] > self.size[1]:
                    self.size[1] = pos[1]
            self.size[0] += 1
            self.size[1] += 1


    def asMatrix(self):
        """ Calculates fully populated matrix (including 0s) from sparse representation.

        Returns
        -------
        numpy array
            fully populated (width x height) original matrix (including 0s)

        """
        output = np.zeros((self.size[0],self.size[1]))
        for pos in self.matrixDict:
            output[pos[0]][pos[1]] = self.matrixDict[pos]
        return output


    def __str__(self):
        """ Turns efficient sparse matrix representation into readable fully
            populated matrix representation.

        Returns
        -------
        str
            stringified populated matrix.

            E.g. for a 3x3 matrix with a 1 in the lower right corner only:
            "[0. 0. 0.]
             [0. 0. 0.]
             [0. 0. 1.]"

        """
        return str(self.asMatrix())
