from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def DEBUG(param, description='NULL'):
    #print(description, param)
    return

def setAllZero(matrix, n, ind):
    matrix[ind].extend([0]*(n-ind-1))

def _initMatrix_(n=3, a=1, b=5, c=1, p=1):
    matrix = []
    
    for ind in range( n ):
        matrix.append([])
        
        if ind != 0:
            matrix[ind].extend([0]*(ind-1))
            matrix[ind].extend([a, b, c])
            setAllZero(matrix, n, ind)
        else:
            matrix[ind].extend([b,c])
            setAllZero(matrix, n, ind)

    matrix.append([p]*(n+1))
    
    return matrix

def _initValue_(n=3):
    return [ ind+1 for ind in range( n+1 )]

def initMatrix(n=3, a=1, b=5, c=1, p=1):
    
    matrix = _initMatrix_(n, a, b, c, p)
    
    for ind in range( n+1 ):
        matrix[ind].append(ind+1)

    return matrix

def getErrorMatrixNorm(list):
    return sqrt(sum(list[ind]**2 for ind in range(len(list))) )

def printErrorNorm(matrix_list, x, value_list):
    
    error_list = []

    for ind in range(len(matrix_list)):
        error_list.append(value_list[ind] - sum(matrix_list[ind][i]*x[i] for i in range(len(x))))

    print('Error vector:', error_list)

    print('Error norm value:{:.2e}'.format(getErrorMatrixNorm(error_list)))

def m_getErrorMatrixNorm(A, x, b):
    error = np.dot(A, x) - b
    #print(f'error value:{error}')
    return getErrorMatrixNorm(error.tolist())

def builPlot(all_errors_list, name='plot', folder='img/', dpi=500, show=False):
    
    fileName = name + '.jpg'

    plt.figure(figsize=(16/2,9/2))
    plt.plot(all_errors_list)
    
    plt.xlim([0, len(all_errors_list)])
    plt.ylim([0, max(all_errors_list)])

    plt.grid(linestyle = '--', linewidth = 0.5)

    plt.xlabel("iterations number")
    plt.title(name + ' method discrepancy')
    
    if show != False:
        plt.show()
    
    plt.savefig(folder + fileName, dpi=500)
    plt.clf()