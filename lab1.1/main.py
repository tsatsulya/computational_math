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
ADList      = [Deriv1, Deriv2, Deriv3, Deriv4, Deriv5]
FuncList    = [Sin, CosSin, ExpSinCos, LogArg, SqrtArg]
RDList      = [SinDeriv, CosSinDeriv, ExpSinCosDeriv, LogArgDeriv, SqrtArgDeriv]

point     = 2

# build for all needed functions

#for everyFkey in range(5):

# 20 point for every derivative approx functions

FuncNameList = ['$sin(x^2)$', '$cos(sin(x))$', '$e^{sin(cos(x))}$', '$ln(x+3)$', '$(x+3)^{1/2}$']

def createFucnStat(funcNum=0, funcName='_Enter_', fileName='stat.jpg'):
    
    ErrorList = [[], [], [], [], []]
    
    x = [2**(-ind) for ind in range(20)]
    #x.append(0)

    print(RDList[funcNum](point))

    for ind in range(len(x)):
        step = x[ind]
        # set of approx functions
        for key in range(5):
            ErrorList[key].append(fabs( ADList[key](FuncList[funcNum], point, step)\
                               - RDList[funcNum](point)))
            
            #ErrorList[key].append(ADList[key](FuncList[funcNum], point, step))#\
            #                        - RDList[funcNum](point))
            """
            ErrorList[1].append(Deriv2(Sin, point, step) - SinDeriv(point))
            ErrorList[2].append(Deriv3(Sin, point, step) - SinDeriv(point))
            ErrorList[3].append(Deriv4(Sin, point, step) - SinDeriv(point))
            ErrorList[4].append(Deriv5(Sin, point, step) - SinDeriv(point))
            """

    #for ind in range(5):
    #    print(ErrorList[ind]) 
    plt.figure(figsize=(16/2,9/2))
    plt.xscale("log")
    plt.yscale("log")

    for ind in range(5):
        plt.plot(x, ErrorList[ind], marker='*', markersize=4)
        #print(ErrorList[ind])

    LegendList = ['$\\frac{f(x+h) - f(x)}{h}$',\
                
                '$\\frac{f(x) - f(x-h)}{h}$',\
                
                '$\\frac{f(x+h) - f(x-h))}{2h}$',\
                
                '$\\frac{4}{3}\\cdot\\frac{f(x+h) - f(x-h))}{2h}\
                    - \\frac{1}{3}\\cdot\\frac{f(x+2h) - f(x-2h))}{4h}$',\
                
                '$\\frac{3}{2}\\cdot\\frac{f(x+h) - f(x-h))}{2h} - \\frac{3}{5}\\cdot\\frac{f(x+2h)\
                    - f(x-2h))}{4h} + \\frac{1}{10}\\cdot\\frac{f(x+3h) - f(x-3h))}{6h}$'\
                ]

    plt.legend(LegendList, loc="upper left", fontsize="7")
    plt.xlabel("h value")
    plt.ylabel("Error value")

    #plt.xlim([0,1])
    plt.title("Derivative approx error value in (x={:.2f}) for: ".format(point) + funcName)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    #plt.show()
    
    plt.savefig(fileName, dpi=500)
    plt.clf()

#Folder = 'img/'
Folder = ''

for ind in range(5):
    createFucnStat(ind, FuncNameList[ind], Folder +'stat'+str(ind)+'p'+str(int(point))+'.jpg')