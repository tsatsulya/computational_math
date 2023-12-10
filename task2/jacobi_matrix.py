import numpy as np
import matplotlib.pyplot as plt

from matrix_init import _initMatrix_, _initValue_
from matrix_init import m_getErrorMatrixNorm, builPlot

SIGMA = 1e-8
ITERATION_LIMIT = 1000

all_errors_list = []

a = np.array(_initMatrix_())
b = np.array(_initValue_(), float)

# prints the system
print("System:")
for i in range(a.shape[0]):
    row = [f"{a[i, j]} * x{j + 1}" for j in range(a.shape[1])]
    print(f'{" + ".join(row)} = {b[i]}')
print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        print(f"Iteration {it_count}: {x}")

    all_errors_list.append(m_getErrorMatrixNorm(a, x, b))

    x_new = np.zeros_like(x)

    for i in range(a.shape[0]):
        s1 = np.dot(a[i, :i], x[:i])
        s2 = np.dot(a[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / a[i, i]
        if x_new[i] == x_new[i-1]:
            break

    if m_getErrorMatrixNorm(a, x, b) <= SIGMA:
        break

    x = x_new


"""
plt.plot(all_errors_list)
plt.title('Jacobi method discrepancy')
plt.show()
"""

builPlot(all_errors_list, 'jacobi')

print(f"Solution: {x}")
print(f'error value:{m_getErrorMatrixNorm(a, x, b)}')
