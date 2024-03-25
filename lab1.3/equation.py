import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr

root_range = [-3, 3]
point_num = 10
equation = '2*x**2 - 5*x + 3 = 0'
fi_equation = '(2*x**2 + 3) / 5'
sigma = 1e-4

x_list = []
error_list = [[], []]

x_newton = []
error_newton = [[], []]

x_iter = []
error_iter = [[], []]


def graph_insert(x, err, x_list=x_list, error_list=error_list):
    x_list.append(x)
    error_list[0].append(err)
    error_list[1].append(err)
    return


def graph_insert_diff(x, err_u, err_d, x_list=x_list, error_list=error_list):
    x_list.append(x)
    error_list[0].append(err_d)
    error_list[1].append(err_u)
    return


def graph_clear():
    global x_list, error_list
    x_list = []
    error_list = [[], []]
    return


def calc_equation(eq, x):
    eq = eq.replace('x', '(' + str(x) + ')')
    return eval(eq)


def find_root_range():
    global root_range, equation, point_num
    global expression

    expression = equation[0:equation.find('=')]
    out_key = False
    root_ind = 0

    while True:
        step = (root_range[1] - root_range[0]) / point_num
        for ind in range(point_num):
            if (calc_equation(expression, root_range[0] + (ind) * step)
                    * calc_equation(expression, root_range[0] + (ind + 1) * step) < 0):
                root_ind = ind
                out_key = True

                graph_insert(root_range[0] + (ind + 1/2) * step, 1/2 * step)
                break
            else:
                graph_insert_diff(root_range[0] + (ind + 1/2) * step, root_range[1] - (
                    root_range[0] + (ind + 1/2) * step), (ind + 1/2) * step)
        if out_key:
            break
        else:
            point_num += 2
            print('extending point number')
            graph_clear

    root_range[1] = root_range[0] + (root_ind + 1) * step
    root_range[0] = root_range[0] + (root_ind) * step

    print(root_range[0], root_range[1])
    return


def half_div_range():
    global expression

    while abs(eval(expression.replace('x', str((root_range[1] + root_range[0]) / 2)))) > sigma:

        if (calc_equation(expression, (root_range[1] + root_range[0]) / 2)
                * calc_equation(expression, root_range[1]) < 0):
            root_range[0] = (root_range[1] + root_range[0]) / 2
        else:
            root_range[1] = (root_range[1] + root_range[0]) / 2

    print((root_range[1] + root_range[0]) / 2)
    return


def iteration_method():
    global root_range, fi_equation, equation

    approx = (root_range[1] + root_range[0]) / 2

    while abs(calc_equation(expression, approx)) > sigma:
        approx = calc_equation(fi_equation, approx)
        graph_insert(approx, math.sqrt(
            abs(calc_equation(expression, approx))), x_iter, error_iter)

    print(approx)
    return


def newton_method():
    global root_range, fi_equation, equation, x_newton, error_newton

    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(expression, my_symbols)

    x_0 = root_range[0]
    approx = x_0

    while abs(calc_equation(expression, approx)) > sigma:
        approx = approx - calc_equation(expression, approx) / \
            calc_equation(str(diff(my_func, my_symbols['x'])), x_0)
        graph_insert(approx, math.sqrt(
            abs(calc_equation(expression, approx))), x_newton, error_newton)

    print(approx)
    return


find_root_range()
iteration_method()
newton_method()

plt.figure(figsize=(16/2, 9/2))

plt.plot([ind + 1 for ind in range(len(x_list))], x_list)
plt.errorbar([ind + 1 for ind in range(len(x_list))], x_list,
             yerr=error_list, fmt='o', ecolor='g', linewidth=1)

plt.plot([ind + len(x_list) for ind in range(len(x_newton))], x_newton)
plt.errorbar([ind + len(x_list) for ind in range(len(x_newton))],
             x_newton, yerr=error_newton, fmt='o', ecolor='g', linewidth=1)

plt.plot([ind + len(x_list) for ind in range(len(x_iter))], x_iter)
plt.errorbar([ind + len(x_list) for ind in range(len(x_iter))],
             x_iter, yerr=error_iter, fmt='o', ecolor='g', linewidth=1)

plt.legend(['Dividing a segment in half', 'Newton method',
           'Iteration method'], loc='upper left', fontsize='7')

plt.title('finding the root of the equation')

plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel('iteration number')
plt.ylabel('root value')

plt.tight_layout()

# plt.show()
plt.savefig('img/root.jpg', dpi=500)

plt.clf()

plt.figure(figsize=(16/2, 9/2))

plt.plot([ind + len(x_list) for ind in range(len(x_newton))], x_newton)
plt.errorbar([ind + len(x_list) for ind in range(len(x_newton))],
             x_newton, yerr=error_newton, fmt='o', ecolor='g', linewidth=1)

plt.plot([ind + len(x_list) for ind in range(len(x_iter))], x_iter)
plt.errorbar([ind + len(x_list) for ind in range(len(x_iter))],
             x_iter, yerr=error_iter, fmt='o', ecolor='g', linewidth=1)

plt.legend(['Dividing a segment in half', 'Newton method'],
           loc='upper left', fontsize='7')

plt.title('finding the root of the equation')

plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel('iteration number')
plt.ylabel('root value')

plt.tight_layout()

# plt.show()
plt.savefig('img/root_in.jpg', dpi=500)
