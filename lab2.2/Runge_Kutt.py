import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


plt.figure(figsize=(16/2,9/2))
t_start, t_end, y0 = 0, 1000, np.array([1, 0, 0])

def f(t, y):
    u, v, w = y
    return np.array([
        -0.04*u + (10**4)*v*w,
        0.04*u - (10**4)*v*w - 3*(10**7)*(v**2),
        3*(10**7)*(v**2)
    ])

h = 0.1

y_, t_ = [y0], [t_start]
n = int((t_end - t_start)/h)

for i in range(n):
    yn, tn = y_[i], t_[i]

    k1_ = lambda k: k - f(tn + (1/4)*h, yn + (1/4)*h*k)
    k2_ = lambda k: k - f(tn + (3/4)*h, yn + (1/2)*h*k1 + (1/4)*h*k)

    k1 = fsolve(k1_, yn)
    k2 = fsolve(k2_, yn)

    y_.append(yn + h*((1/2)*k1 + (1/2)*k2))
    t_.append(tn + h)


y_ = np.array(y_)
t_ = np.array(t_)


u, v, w = y_.transpose()

plt.plot(t_, u, label='u', marker = '*', markersize = 4)
plt.plot(t_, v, label='v', marker = '*', markersize = 4)
plt.plot(t_, w, label='w', marker = '*', markersize = 4)

plt.ylabel("y")
plt.xlabel("x")
plt.savefig('imgs/Runge_Kutt.png', dpi = 200)