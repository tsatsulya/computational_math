import numpy as np
import matplotlib.pyplot as plt

from matrix_init import _initMatrix_, _initValue_, m_getErrorMatrixNorm,\
                        builPlot

ITERATION_LIMIT = 1000

all_errors_list = []

# initialize the matrix
A = np.array(_initMatrix_())

# initialize the RHS vector
b = np.array(_initValue_())

print("System of equations:")
for i in range(A.shape[0]):
    row = [f"{A[i,j]:3g}*x{j+1}" for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b, np.float_)

for it_count in range(1, ITERATION_LIMIT):
    
    x_new = np.zeros_like(x, dtype=np.float_)
    print(f"Iteration {it_count}: {x}")
    
    all_errors_list.append(m_getErrorMatrixNorm(A, x, b))

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    
    if np.allclose(x, x_new, rtol=1e-8):
        break
    
    x = x_new

    # all_errors_list.append(m_getErrorMatrixNorm(A, x, b))
"""
plt.plot(all_errors_list)
plt.title('Seidel method discrepancy')
plt.show()
"""

builPlot(all_errors_list, 'seidel')

print(f"Solution: {x}")
error = np.dot(A, x) - b
print(f'error value:{error}')
