import matplotlib.pyplot as plt
from func import *

def SimpleFuncSet(exFunc, point, delta, mplex):
    retVal = ( exFunc(point + mplex*delta) - exFunc(point - mplex*delta) )\
                 / (2*mplex*delta) 
    
    return retVal

def Deriv1(exFunc, point, delta):
    retVal = ( exFunc(point + delta) - exFunc(point) ) / delta
    
    return retVal

def Deriv2(exFunc, point, delta):
    retVal = ( exFunc(point) - exFunc(point - delta) ) / delta

    return retVal

def Deriv3(exFunc, point, delta):
    retVal = ( exFunc(point + delta) - exFunc(point - delta) ) / (2*delta) 
    
    return retVal
    #return SimpleFuncSet(exFunc, point, delta, 1)   

def Deriv4(exFunc, point, delta):   
    term  = SimpleFuncSet(exFunc, point, delta, 1)
    term2 = SimpleFuncSet(exFunc, point, delta, 2)

    return (4/3)*term - (1/3)*term2

def Deriv5(exFunc, point, delta):   
    term  = SimpleFuncSet(exFunc, point, delta, 1)
    term2 = SimpleFuncSet(exFunc, point, delta, 2)
    term3 = SimpleFuncSet(exFunc, point, delta, 3)
    
    return (3/2)*term - (3/5)*term2 + (1/10)*term3

# Approximation derivative List
ADList = [Deriv1, Deriv2, Deriv3, Deriv4, Deriv5]
FuncList =  [Sin, CosSin, ExpSinCos, LogArg, SqrtArg]
RDList = [SinDeriv, CosSinDeriv, ExpSinCosDeriv, LogArgDeriv, SqrtArg]

ErrorList = [[], [], [], [], []]
point     = 0

# build for all needed functions

#for everyFkey in range(5):

# 20 point for every derivative approx functions
for ind in range(20):
    step = 2**(-ind)
    # set of approx functions
    for key in range(5):
        ErrorList[key].append(fabs( ADList[key](FuncList[4], point, step)\
                            - RDList[4](point)))
        #ErrorList[key].append(ADList[key](FuncList[4], point, step)\
        #                        - RDList[4](point))
        """
        ErrorList[1].append(Deriv2(Sin, point, step) - SinDeriv(point))
        ErrorList[2].append(Deriv3(Sin, point, step) - SinDeriv(point))
        ErrorList[3].append(Deriv4(Sin, point, step) - SinDeriv(point))
        ErrorList[4].append(Deriv5(Sin, point, step) - SinDeriv(point))
        """

#for ind in range(5):
#    print(ErrorList[ind]) 

plt.xscale("log")
plt.yscale("log")

x = [2**(-ind) for ind in range(20)]

for ind in range(5):
    plt.plot(x, ErrorList[ind])
    print(ErrorList[ind])

#plt.legend(['$\pm2\textdegree$'])
#plt.plot(ErrorList[1])
#plt.ylabel('some numbers')
plt.show()
