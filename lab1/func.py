
from math import *  

#============= 1st Set
def Sin(arg):
    return sin(arg**2)

def SinDeriv(arg):
    return cos(arg**2)*2*arg
#=========== End 1st Set

#============= 2nd Set
def CosSin(arg):
    return cos(sin(arg))

def CosSinDeriv(arg):
    return -sin(sin(arg))*cos(arg)
#============= End 2nd Set

#============= 3 Set
def ExpSinCos(arg):
    return exp(sin(cos(arg)))

def ExpSinCosDeriv(arg):
    return ExpSinCos(arg)*cos(cos(arg))*(-sin(arg))
#============= End 3 Set

#============= 4 Set
def LogArg(arg):
    if arg + 3 == 0:
        print("exception log({})".format(0))
        return 0
    return log(arg + 3)

def LogArgDeriv(arg):
    return 1/(arg + 3)
#============= End 4 Set

#============= 5 Set
def SqrtArg(arg):
    return sqrt(arg + 3)

def SqrtArgDeriv(arg):
    return 1/(2*SqrtArg(arg))
#============= End 5 Set