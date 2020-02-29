import numpy as np
import operations as op
import sympy

matA = np.array([[3,4],[7,2],[9,1]])
matB = np.array([[1,2,3,4],[5,6,7,8]])

print(op.kroneckerProduct(matA,matB))