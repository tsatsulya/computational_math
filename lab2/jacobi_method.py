import numpy as np
import matplotlib.pyplot as plt

from matrix_init import _initMatrix_, _initValue_
from matrix_init import m_getErrorMatrixNorm, builPlot

ITERATION_LIMIT = 1000

all_errors_list = []

# initialize the matrix
A = np.array(_initMatrix_())
# initialize the RHS vector
b = np.array(_initValue_(), float)

# prints the system
print("System:")
for i in range(A.shape[0]):
    row = [f"{A[i, j]}*x{j + 1}" for j in range(A.shape[1])]
    print(f'{" + ".join(row)} = {b[i]}')
print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        print(f"Iteration {it_count}: {x}")

    all_errors_list.append(m_getErrorMatrixNorm(A, x, b))

    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=1e-8, rtol=0.):
        break

    x = x_new

    # all_errors_list.append(m_getErrorMatrixNorm(A, x, b))
"""
plt.plot(all_errors_list)
plt.title('Jacobi method discrepancy')
plt.show()
"""

builPlot(all_errors_list, 'jacobi')

print(f"Solution: {x}")
error = np.dot(A, x) - b
print(f'error value:{error}')


