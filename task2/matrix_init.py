from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def DEBUG(param, description='NULL'):
    return


def set_all_zero(matrix, n, ind):
    matrix[ind].extend([0]*(n-ind-1))


def init_matrix_(n=99, a=1, b=10, c=1, p=1):
    matrix = [[]]
    matrix[0].extend([b, c])
    set_all_zero(matrix, n, 0)

    for i in range(1, n):
        matrix.append([])
        matrix[i].extend([0]*(i - 1))
        matrix[i].extend([a, b, c])
        set_all_zero(matrix, n, i)
    matrix.append([p]*(n+1))

    return matrix


def init_matrix(n=99, a=1, b=10, c=1, p=1):

    matrix = init_matrix_(n, a, b, c, p)
    for i in range(n + 1):
        matrix[i].append(i + 1)

    return matrix


def get_error_matrix_norm(list):
    return sqrt(sum(list[ind]**2 for ind in range(len(list))))


def print_erroe_norm(matrix_list, x, value_list):

    error_list = []
    for ind in range(len(matrix_list)):
        error_list.append(
            value_list[ind] - sum(matrix_list[ind][i]*x[i] for i in range(len(x))))

    print('Error vector:', error_list)
    print('Error norm value:{:.2e}'.format(get_error_matrix_norm(error_list)))


def m_get_error_matrix_norm(A, x, b):
    error = np.dot(A, x) - b
    return get_error_matrix_norm(error.tolist())


def builPlot(all_errors_list, name='plot', folder='img/', dpi=500, show=False):

    fileName = name + '.jpg'

    plt.figure(figsize=(16/2, 9/2))
    plt.plot(all_errors_list)

    plt.xlim([0, len(all_errors_list)])
    plt.ylim([0, max(all_errors_list)])

    plt.grid(linestyle='--', linewidth=0.5)

    plt.xlabel("iterations number")
    plt.title(name + ' method discrepancy')

    if show:
        plt.show()

    plt.savefig(folder + fileName, dpi=500)
    plt.clf()
