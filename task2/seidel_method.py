import numpy as np
import matplotlib.pyplot as plt

from matrix_init import init_matrix, m_get_error_matrix_norm,\
    builPlot

SIGMA = 1e-8
ITERATION_LIMIT = 1000
all_errors_list = []


def init_value(n=99):
    return [i + 1 for i in range(n + 1)]


A = np.array(init_matrix())
b = np.array(init_value())

print("System of equations:")
for i in range(A.shape[0]):
    row = [f"{A[i,j]:3g}*x{j+1}" for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b, np.float_)

for it_count in range(1, ITERATION_LIMIT):

    x_new = np.zeros_like(x, dtype=np.float_)
    print(f"Iteration {it_count}: {x}")
    all_errors_list.append(m_get_error_matrix_norm(A, x, b))

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if m_get_error_matrix_norm(A, x, b) <= SIGMA:
        break
    x = x_new

builPlot(all_errors_list, 'seidel')

print(f"Solution: {x}")
print(f'error value:{m_get_error_matrix_norm(A, x, b)}')
