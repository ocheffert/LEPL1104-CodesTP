
import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import norm, solve


def solveEuler(h):
    Xstart = 0
    Xend = 4
    # Ustart = 1
    tol = 10e-15
    nmax = 20

    X = np.arange(Xstart, Xend+h, h)
    U = np.zeros((len(X), 2))
    U[0, :] = [1, 1]
    for i in range(len(X)-1):
        U[i+1, :] = U[i, :]
        n = 0
        dx = tol + 1
        while norm(dx) >= tol and n < nmax:
            n += 1
            # g is in fact -g
            g = [-U[i+1, 0] + U[i, 0] + h * (-U[i+1, 0]*U[i+1, 0]+U[i+1, 1]),
                 -U[i+1, 1] + U[i, 1] + h * (-50*U[i+1, 1]*U[i+1, 1]+X[i+1])]
            dgdx = np.array([[1+2*h*U[i+1, 0], -h],
                             [0, 1+100*h*U[i+1, 1]]])
            dx = solve(dgdx, g)
            U[i+1, :] += dx
        if (n == nmax):
            print(
                f'Iteration {i} - {n} : too much Newton-Raphson iterations !')
    return X, U


for h in [0.5, 0.1, 0.01]:
    X, U = solveEuler(h)
    plt.plot(X, U[:, 0], '.-b', markersize=6, linewidth=1)
    plt.plot(X, U[:, 1], '.-r', markersize=6, linewidth=1)
plt.legend(['u(x)', 'v(x)'])
plt.show()
