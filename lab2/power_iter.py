import numpy as np
import matplotlib.pyplot as plt
import math
from matrix_init import _initMatrix_, _initValue_, m_getErrorMatrixNorm,\
                        builPlot

def isPosDef(x):
    return np.all(np.linalg.eigvals(x) > 0)


SIGMA = 1e-8

ITERATION_LIMIT = 100


# initialize the matrix
A = np.array(_initMatrix_())

# initialize the RHS vector
b = np.array(_initValue_())

x = np.array([2]*len(b)) #np.zeros_like(b, np.float_)

lambda_list = []

for it_count in range(1, ITERATION_LIMIT):
    
    #x_new = np.zeros_like(x, dtype=np.float_)

    x_new = np.dot(A, x) / math.sqrt(np.dot(np.dot(A, x), np.dot(A, x)))

    lambd = np.dot(np.dot(A, x), x) / np.dot(x, x)

    #print(lambd)
    
    lambda_list.append(lambd)

    x = x_new

"""
print(np.dot(A, x))
print(np.dot(lambda_list[-1], x))
"""

max_l = lambda_list[-1]

# print(isPosDef(A))

E = np.eye(len(A))

min_lambda_list = []

B = np.dot(max_l, E) - A

for it_count in range(1, ITERATION_LIMIT):
    
    #x_new = np.zeros_like(x, dtype=np.float_)
    
    x_new = np.dot(B, x) / math.sqrt(np.dot(np.dot(B, x), np.dot(B, x)))

    lambd = np.dot(np.dot(B, x), x) / np.dot(x, x)

    #print(lambd)
    
    min_lambda_list.append(lambd)

    x = x_new

"""
print(np.dot(A, x))
print(np.dot(min_lambda_list[-1], x))
"""

plt.figure(figsize=(16/2,9/2))
plt.plot(lambda_list)
plt.plot(min_lambda_list)
plt.title('find min and max lambda value via power iteration method')

plt.grid(linestyle = '--', linewidth = 0.5)

plt.xlabel('iteration number \n the last value on the chart is lambda - {:.4e}, iteration - {}'.format(lambda_list[-1], len(lambda_list)))

#plt.xlabel('iteration number')
plt.ylabel('lambda value')

plt.tight_layout()


plt.savefig('img/lambda.jpg', dpi=500)
