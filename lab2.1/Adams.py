import numpy as np
import random as rnd
import matplotlib.pyplot as plt


plt.figure(figsize=(16/2,9/2))


def X(x, y):
    return y
def Y(x, y):
    return x**2 - 1

def point_in_circle(r, a, b):
    r_ = r * np.sqrt(rnd.randrange(0, 10000)/10000)
    theta = rnd.randrange(0, 10000)/10000 * 2 * np.pi
    x = a + r_ * np.cos(theta)
    y = b + r_ * np.sin(theta)
    return [x, y]

def new_u1(x, y, h, f):
    f.append([X(x, y), Y(x, y)])
    return [x + h * f[-1][0], y+ h * f[-1][1]]

def new_u2(x, y, h, f):
    f.append([X(x, y), Y(x, y)])
    return [ x + h * (3/2 * f[-1][0] - 1/2 * f[-2][0]),
             y + h * (3/2 * f[-1][1] - 1/2 * f[-2][1])]

def new_u3(x, y, h, f):
    f.append([X(x, y), Y(x, y)])
    return [x + h * (23/12 * f[-1][0] - 16/12 * f[-2][0] + 5/12 * f[-3][0]),
            y + h * (23/12 * f[-1][1] - 16/12 * f[-2][1] + 5/12 * f[-3][1])]




def Adams(x0, y0, h):
    ff = []
    xx = np.array([x0])
    yy = np.array([y0])

    new_u = new_u1(xx[-1], yy[-1], h, ff)
    xx = np.append(xx, new_u[0])
    yy = np.append(yy, new_u[1])


    new_u = new_u2(xx[-1], yy[-1], h, ff)
    xx = np.append(xx, new_u[0])
    yy = np.append(yy, new_u[1])

    for __ in range(10):
        new_u = new_u3(xx[-1], yy[-1], h, ff)
        if (new_u[1]**2 + new_u[0]**2) > 2:
            break
        xx = np.append(xx, new_u[0])
        yy = np.append(yy, new_u[1])

    plt.plot(xx, yy, '-', ms=1)



h = 0.05
r = 1
x0 = [1.0, -1.0]
y0 = [0, 0]

for _ in range(200):
    for i in range(len(x0)):
        point = point_in_circle(r, x0[i], y0[i])
        Adams(point[0], point[1], h)

for i in range(len(x0)):
    plt.plot(x0[i], y0[i], marker = '*', markersize = 8, color = 'b')

plt.ylabel("y")
plt.xlabel("x")
plt.savefig('imgs/Adams.png', dpi = 200)
# plt.show()