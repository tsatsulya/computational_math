import numpy as np
from scipy.linalg import lu
from matrix_init import _initMatrix_, _initValue_,\
                         DEBUG, getErrorMatrixNorm

# Define a square matrix A
A = np.array(_initMatrix_())

# Perform the LU Decomposition
L, U = lu(A, True)

DEBUG('L', L)
DEBUG('U', U)

LU = np.matmul(L, U)

if np.allclose(A, LU):
    print('LU decomposition is valid.')
    print('Continue...')

    y = np.matmul(np.linalg.inv(L), _initValue_())
    DEBUG(y)

    x = np.matmul(np.linalg.inv(U), y)
    print('x=', x.tolist())
else:
    print('LU decomposition is not valid.')

A_list = A.tolist()
value_list = _initValue_()
error_list = []

for ind in range(len(A_list)):
    error_list.append(value_list[ind] - sum(A_list[ind][i]*x[i] for i in range(len(x))))

print('Error vector:', error_list)

print('Error norm value:{:.2e}'.format(getErrorMatrixNorm(error_list)))