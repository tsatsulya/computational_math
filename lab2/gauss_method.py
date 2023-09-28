
# Gauss method to solve matrix
# n = 99, ai = ci = 1, bi = 10, pi = 1, fi = i.
# handmade algorithm 

import numpy as np
from matrix_init import initMatrix, DEBUG, _initValue_, printErrorNorm,\
                            _initMatrix_
#n = 2#99
import copy

matrix=initMatrix()
#print(matrix)

# col - column
# str - string

def popUpString(matrix, trace_ind):
    max = matrix[trace_ind][trace_ind]
    mainLine = trace_ind

    for ind in range( len(matrix)-trace_ind):
        if matrix[ind+trace_ind][trace_ind] > max:
            
            max = matrix[ind+trace_ind][trace_ind]
            mainLine = ind+trace_ind
    
    ch_item = matrix[mainLine]
    matrix.remove(ch_item)
    matrix.insert(trace_ind, ch_item)
    
    return matrix

for col_ind in range( len(matrix[0])-1 ):
    
    matrix = popUpString(matrix, col_ind)
    DEBUG(matrix)

    for str_ind in range( len(matrix)-1-col_ind ):
        
        if matrix[col_ind][col_ind] != 0:
            ratio = matrix[str_ind + 1 + col_ind][col_ind] / matrix[col_ind][col_ind]
            
            for inside in range( len(matrix[0]) ):
                if inside >= col_ind:
                    matrix[str_ind + 1 + col_ind][inside] -= ratio*matrix[col_ind][inside]
            DEBUG(ratio)

    DEBUG(matrix)
    DEBUG('=======')

x = []

key = len(matrix)-1

for ind in range( key+1 ):
    if matrix[key - ind][len(matrix[0])-1] != 0:
        
        prev_koeff_sum = 0
        
        if ind > 0:
            for sum_ind in range(ind):
                prev_koeff_sum += matrix[key - ind][len(matrix[0]) - 2 - sum_ind]*x[len(x)-sum_ind-1]
            DEBUG(prev_koeff_sum)
            
        x.insert(0,(matrix[key - ind][len(matrix[0])-1]-prev_koeff_sum)\
                 /matrix[key - ind][len(matrix[0]) - 2 - ind])
    else:
        print('not solved system')
        break

print('x=', x)
printErrorNorm(_initMatrix_(), x, _initValue_())