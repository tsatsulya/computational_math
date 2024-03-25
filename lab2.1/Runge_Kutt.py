import numpy as np
import random as rnd
import matplotlib.pyplot as plt


plt.figure(figsize=(16/2,9/2))


def X(x, y):
    return y
def Y(x, y):
    return x**2 - 1

K = {4: [[1/2, 0, 0], [0, 1/2, 0], [0, 0, 1]],
     1: [[1/2]]}
c = {4: np.array([1/6, 1/3, 1/3, 1/6]),
     1: np.array([1])}

def point_in_circle(r, a, b):
    r_ = r * np.sqrt(rnd.randrange(0, 10000)/10000)
    theta = rnd.randrange(0, 10000)/10000 * 2 * np.pi
    x = a + r_ * np.cos(theta)
    y = b + r_ * np.sin(theta)
    return [x, y]

def new_k(X, Y, x, y, s, h, K):
    km = {'k': np.array([Y(x, y)]), 'm': np.array([X(x, y)])}
    if s <= 1:
        return km

    for i in range(1, s + 1):
        new_x, new_y = x, y
        for j in range(i):
            new_x += h * K[i - 1][j] * km['m'][j]
            new_y += h * K[i - 1][j] * km['k'][j]
        km['k'] = np.append(km['k'], Y(new_x, new_y))
        km['m'] = np.append(km['m'], X(new_x, new_y))
    return km


def new_c(x, y, c, k_,h):
    new_x, new_y = x, y
    for i in range(len(c)):
       new_x += c[i] * k_['m'][i] * h
       new_y += c[i] * k_['k'][i] * h

    return [new_x, new_y]

def Runge_kutt(a, b, X, Y, h, s):
    xx, yy = np.array([a]), np.array([b])
    for t in range(0, 10):
        km = new_k(X, Y, xx[-1], yy[-1], s - 1, h, K[s])
        new_ = new_c(xx[-1], yy[-1], c[s], km, h)
        # if (new_[0] * new_[0] + new_[1] * new_[1]) > 10:
        #     break
        xx = np.append(xx, new_[0])
        yy = np.append(yy, new_[1])
    plt.plot(xx, yy)
    # plt.show()


l = 5
x0 = [1, -1]
y0 = [0, 0]
for i in range(200):
    for j in range(len(x0)):
        point = point_in_circle(1, x0[j], y0[j])
        Runge_kutt(point[0], point[1], X, Y, 0.05, 4)

for i in range(len(x0)):
    plt.plot(x0[i], y0[i], marker = '*', markersize = 8, color = 'r')



plt.xlabel("x")
plt.ylabel("y")
plt.savefig('imgs/RungeKutt1_1_0', dpi = 200)