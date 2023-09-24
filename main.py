import matplotlib.pyplot as plt
from funcs import *

def func_set(func, point, delta, mplex):
    value = (func(point + mplex*delta) - func(point - mplex*delta)) \
                / (2*mplex*delta) 
    return value

def derivative_1(func, point, delta):
    value = (func(point + delta) - func(point)) / delta
    return value

def derivative_2(func, point, delta):
    value = (func(point) - func(point - delta)) / delta
    return value

def derivative_3(func, point, delta):
    value = (func(point + delta) - func(point - delta)) / (2*delta) 
    return value

def derivative_4(func, point, delta):   
    val1 = func_set(func, point, delta, 1)
    val2 = func_set(func, point, delta, 2)
    return (4/3)*val1 - (1/3)*val2

def derivative_5(func, point, delta):   
    val1  = func_set(func, point, delta, 1)
    val2 = func_set(func, point, delta, 2)
    val3 = func_set(func, point, delta, 3)
    return (3/2)*val1 - (3/5)*val2 + (1/10)*val3


def sin_2(arg):
    return sin(arg**2)
def d_sin_2(arg):
    return cos(arg**2)*2*arg

def cos_sin(arg):
    return cos(sin(arg))
def d_cos_sin(arg):
    return -sin(sin(arg))*cos(arg)

def exp_sin_cos(arg):
    return exp(sin(cos(arg)))
def d_exp_sin_cos(arg):
    return exp_sin_cos(arg)*cos(cos(arg))*(-sin(arg))

def log_3(arg):
    if arg + 3 <= 0:
        print("exception log({})".format(0))
        return 0
    return log(arg + 3)
def d_log_3(arg):
    return 1/(arg + 3)

def sqrt_3(arg):
    return sqrt(arg + 3)
def d_sqrt_3(arg):
    return 1/(2*sqrt_3(arg))


d_list = [derivative_1, derivative_2, derivative_3, derivative_4, derivative_5]
funcs = [sin_2, cos_sin, exp_sin_cos, log_3, sqrt_3]
d_funcs = [d_sin_2, d_cos_sin, d_exp_sin_cos, d_log_3, d_sqrt_3]

point = 0

func_names = ['$sin(x^2)$', '$cos(sin(x))$', '$e^{sin(cos(x))}$', '$ln(x+3)$', '$(x+3)^{1/2}$']

def create_stat(func_num=0, func_name='_enter_', file_name='funcs_stat.jpg'):
    errors = [[] for i in range(5)]
    x = [2**(-ind) for ind in range(20)]

    for ind in range(len(x)):
        step = x[ind]
        for key in range(5):
            errors[key].append(fabs(d_list[key](funcs[func_num], point, step) \
                               - d_funcs[func_num](point)))

    plt.figure(figsize=(8,5))
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("h")
    plt.ylabel("Error")
    plt.title("error for " + func_name + " and x=" + str(point))

    for i in range(5):
        plt.plot(x, errors[i], marker='.', markersize=3)

    legends = ['$\\frac{f(x+h) - f(x)}{h}$', '$\\frac{f(x) - f(x-h)}{h}$', \
                  '$\\frac{f(x+h) - f(x-h))}{2h}$', \
                  '$\\frac{4}{3}\\cdot\\frac{f(x+h) - f(x-h))}{2h} \
                    - \\frac{1}{3}\\cdot\\frac{f(x+2h) - f(x-2h))}{4h}$', \
                  '$\\frac{3}{2}\\cdot\\frac{f(x+h) - f(x-h))}{2h} - \\frac{3}{5}\\cdot\\frac{f(x+2h) \
                    - f(x-2h))}{4h} + \\frac{1}{10}\\cdot\\frac{f(x+3h) - f(x-3h))}{6h}$' \
                 ]
    plt.legend(legends, loc="upper left", fontsize="5")

    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.savefig(file_name, dpi=500)
    plt.clf()

folder_name = 'img/'

for i in range(5):
    create_stat(i, func_names[i], folder_name + 'stat_' + str(i+1) + '_p_' + str(int(point)) + '.jpg')