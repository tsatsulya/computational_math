import numpy as np
import matplotlib.pyplot as plt

t_start, t_end, y0 = 0, 1000, np.array([1, 0, 0])
h = 0.0002

def f(t, y):
    u, v, w = y
    return np.array([
        -0.04*u + (10**4)*v*w,
        0.04*u - (10**4)*v*w - 3*(10**7)*(v**2),
        3*(10**7)*(v**2)
    ])

y_step = 10**(-5)

y_, t_ = [y0], [t_start]
n = int((t_end - t_start)/h)

for i in range(n):
    yn, tn = y_[i], t_[i]

    E = np.eye(y0.size)
    A = E - ((1+1j)/2)*h
    b = f(tn + h/2, yn)
    w = np.linalg.solve(A, b)
    yn1, tn1 = yn + h * w.real, tn + h

    y_.append(yn1)
    t_.append(tn1)

y_ = np.array(y_)
t_ = np.array(t_)

u, v, w = y_.transpose()

plt.plot(t_, u, label='u', marker = '*', markersize = 3)
plt.plot(t_, v, label='v', marker = '*', markersize = 3)
plt.plot(t_, w, label='w', marker = '*', markersize = 3)

plt.ylabel("y")
plt.xlabel("x")
plt.savefig('imgs/Rosenbrock.png', dpi = 200)