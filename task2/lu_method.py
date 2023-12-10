import numpy as np
from scipy.linalg import lu
from matrix_init import _initMatrix_, _initValue_,\
    DEBUG, printErrorNorm

A = np.array(_initMatrix_())
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

printErrorNorm(A_list, x, value_list)
