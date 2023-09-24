from math import *

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