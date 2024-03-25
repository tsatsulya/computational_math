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



def fdn_new_u(alphas, beta, h, xx, yy):
    # u_new = tau * beta * func(u_new) + sum(alpha[i] * u_old[i])
    # u_new = gamma * func(u_new) + delta
    last_x, last_y = xx[-1], yy[-1]

    delta_x = (alphas[2] * xx[-1] + alphas[1] * xx[-2] + alphas[0] * xx[-3])
    delta_y = (alphas[2] * yy[-1] + alphas[1] * yy[-2] + alphas[0] * yy[-3])

    gamma = h * beta
    new_x = gamma * X(xx[-1], yy[-1]) + delta_x
    new_y = gamma * Y(xx[-1], yy[-1]) + delta_y

    while (np.linalg.norm(np.array([last_x - new_x, last_y - new_y])) > 0.1**4):
        last_x, last_y = new_x, new_y
        new_x, new_y = gamma * X(last_x, last_y) + delta_x, \
            gamma * Y(last_x, last_y) + delta_y

    return [new_x, new_y]

def FDN(x0, y0, h):
    ff = []
    xx = np.array([x0])
    yy = np.array([y0])

    new_u = new_u1(xx[-1], yy[-1], h, ff)
    xx = np.append(xx, new_u[0])
    yy = np.append(yy, new_u[1])


    new_u = new_u2(xx[-1], yy[-1], h, ff)
    xx = np.append(xx, new_u[0])
    yy = np.append(yy, new_u[1])

    new_u = new_u3(xx[-1], yy[-1], h, ff)
    xx = np.append(xx, new_u[0])
    yy = np.append(yy, new_u[1])

    for __ in range(10):
        new_u = fdn_new_u(alphas, beta, h, xx, yy)
        if (new_u[1]**2 + new_u[0]**2) > 4:
            break
        xx = np.append(xx, new_u[0])
        yy = np.append(yy, new_u[1])

    plt.plot(xx, yy, '-', ms=1)

alphas = [2/11, -9/11, 18/11]
beta = 6/11

h = 0.05
r = 1
x0 = [-1, 1]
y0 = [0, 0]

for _ in range(200):
    for i in range(len(x0)):
        point = point_in_circle(r, x0[i], y0[i])
        FDN(point[0], point[1], h)

for i in range(len(x0)):
    plt.plot(x0[i], y0[i], marker = '*', markersize = 8, color = 'b')

plt.ylabel("y")
plt.xlabel("x")
plt.savefig('imgs/fdn.png', dpi = 200)
# plt.show()