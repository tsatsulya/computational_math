import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *


from numpy import cos, sin, pi, exp
def F(x):
    return np.array([sin(x[0] + 1) - x[1] - 1.2, 2*x[0] + cos(x[1]) - 2])
def J(x):
    return np.array([[cos(x[0] + 1), -1], [2, -sin(x[1])]])

vector_list = [[], []]
norm_list = []

def build_plot(method_name, file_name):
    global vector_list, norm_list

    plt.figure(figsize=(16/2, 9/2))
    plt.plot([ind for ind in range(len(vector_list[0]))],
             vector_list[0], marker='o')
    plt.plot([ind for ind in range(len(vector_list[0]))],
             vector_list[1], marker='o')
    plt.plot([ind for ind in range(len(norm_list))], norm_list, marker='o')

    plt.legend(['x', 'y', '$F$'], loc='upper left', fontsize='10')

    plt.title('finding the roots of the system - ' + method_name + ' method')

    plt.grid(linestyle='--', linewidth=0.5)

    plt.xlabel('iteration number')
    plt.ylabel('roots value')

    plt.tight_layout()

    plt.savefig('img/' + file_name + '.jpg', dpi=500)

    plt.clf()

    vector_list = [[], []]
    norm_list = []
    return


def test_newton_system():
    tol = 1e-4
    x, n = newton_system(F, J, x=np.array([1, 1], dtype=float), eps=1e-10)
    print(n, x)
    print(F(x))
    build_plot('Newton\'s', 'system_newton')
    return


def newton_system(F, J, x, eps):
    global vector_list, norm_list

    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector

    iteration_counter = 0

    vector_list[0].append(x[0])
    vector_list[1].append(x[1])
    norm_list.append(F_norm)

    while abs(F_norm) > eps and iteration_counter < 1000:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1
        vector_list[0].append(x[0])
        vector_list[1].append(x[1])
        norm_list.append(F_norm)

    if abs(F_norm) > eps:
        iteration_counter = -1

    return x, iteration_counter


def test_iterative_method():
    from numpy import cos, sin, pi, exp

    def F(x):
        return np.array([sin(x[0] + 1) - x[1] - 1.2, 2*x[0] + cos(x[1]) - 2])

    def D(x):
        return np.array([1 - cos(x[1]) / 2, sin(x[0] + 1) - 1.2])

    n, x = iterative_method(F, D, x=np.array([1, 1], dtype=float), eps=1e-10)
    print(n, x)
    print(F(x))

    build_plot('Iterative', 'system_iter')
    return


def iterative_method(F, D, x, eps):
    iteration_counter = 0

    vector_list[0].append(x[0])
    vector_list[1].append(x[1])
    norm_list.append(abs(np.linalg.norm(F(x), ord=2)))

    while abs(np.linalg.norm(F(x), ord=2)) > eps and iteration_counter < 1000:
        x = D(x)

        vector_list[0].append(x[0])
        vector_list[1].append(x[1])
        norm_list.append(abs(np.linalg.norm(F(x), ord=2)))

        iteration_counter += 1

    return iteration_counter, x


test_newton_system()
test_iterative_method()
