
# Gauss method
# n = 99, ai = ci = 1, bi = 10, pi = 1, fi = i.

import numpy as np
from matrix_init import initMatrix, DEBUG, _initValue_, printErrorNorm, _initMatrix_
import copy

matrix = initMatrix()


def pop_up_string(matrix, trace_):
    max = matrix[trace_][trace_]

    for ind in range(len(matrix) - trace_):
        if matrix[ind+trace_][trace_] > max:

            max = matrix[ind + trace_][trace_]
            mainLine = ind + trace_

    ch_item = matrix[mainLine]
    matrix.remove(ch_item)
    matrix.insert(trace_, ch_item)

    return matrix


for col_ in range(len(matrix[0]) - 1):

    matrix = pop_up_string(matrix, col_)
    DEBUG(matrix)

    for str_ in range(len(matrix) - 1 - col_):

        if matrix[col_][col_] != 0:
            ratio = matrix[str_ + 1 + col_][col_] / \
                matrix[col_][col_]

            for inside in range(len(matrix[0])):
                if inside >= col_:
                    matrix[str_ + 1 + col_][inside] -= ratio * \
                        matrix[col_][inside]
            DEBUG(ratio)

x = []

key = len(matrix) - 1

for i in range(key + 1):
    if matrix[key - i][len(matrix[0]) - 1] != 0:

        prev_koeff_sum = 0

        if i > 0:
            for sum_ in range(i):
                prev_koeff_sum += matrix[key - i]
                [len(matrix[0]) - 2 - sum_] * x[len(x) - sum_ - 1]

        x.insert(0, (matrix[key - i][len(matrix[0]) - 1] - prev_koeff_sum)
                 / matrix[key - i][len(matrix[0]) - 2 - i])
    else:
        print('system can''t be solved')
        break

print('x = ', x)
printErrorNorm(_initMatrix_(), x, _initValue_())
