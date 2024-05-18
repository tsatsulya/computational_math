import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

t_start, t_end, y0 = 0, 1000, np.array([1, 0, 0])
h = 0.0002
y_step = 10**(-4)

def f(t, y):
    u, v, w = y
    return np.array([
        -0.04*u + (10**4)*v*w,
        0.04*u - (10**4)*v*w - 3*(10**7)*(v**2),
        3*(10**7)*(v**2)
    ])

y_, t_ = [y0], [t_start]
n = int((t_end - t_start)/h)

order = 4
P = sp.linalg.pascal(order + 1, kind = 'upper')

e = np.array([0, 1, 0, 0, 0])
L = np.array([251/720, 1, 11/12, 1/3, 1/24])

zn_ = np.zeros((order + 1, y0.size))
zn_[0] = y0
zn_[1] = h*f(t_start, y0)

for i in range(n):
    yn = y_[i]
    tn = t_[i]
    zn = zn_

    inter = P @ zn
    zn1 = inter + np.outer(L, (h*f(tn, yn) - np.dot(e, inter)))

    yn1 = zn_[0]
    tn1 = tn + h

    y_.append(yn1)
    t_.append(tn1)

y_ = np.array(y_)
t_ = np.array(t_)


u, v, w = y_.transpose()

plt.plot(t_, u, label='u', marker = '*', markersize = 4)
plt.plot(t_, v, label='v', marker = '*', markersize = 4)
plt.plot(t_, w, label='w', marker = '*', markersize = 4)

plt.ylabel("y")
plt.xlabel("x")
plt.savefig('imgs/Nordsik.png', dpi = 200)