import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import time

matplotlib.rcParams['toolbar'] = 'None'
myColorMap = matplotlib.cm.jet


def edpEuler(m, n, beta):

    side = np.linspace(0, 1, m)
    X, Y = np.meshgrid(side, side)

    U = X**2 + Y**2     # cdt initiale

    Unew = U.copy()
    c = 0
    c_instable = 0
    c_limit = 0

    for _ in range(n):
        for i in range(1, m-1):
            for j in range(1, m-1):
                c += 1
                Unew[i, j] = U[i, j] + beta * \
                    (U[i+1, j+1]-U[i-1, j+1]-U[i+1, j-1]+U[i-1, j-1])
                facteur = Unew[i, j] / U[i, j]
                if facteur > 1:
                    c_instable += 1
                    print('Aie aie aie')
                elif facteur == 1:
                    c_limit += 1
        U = Unew.copy()
    print('Limit: ', c_limit/c)
    print('Instable: ', c_instable/c)
    return U


# ou:

def edpEuler_vectorized(m, n, beta):
    side = np.linspace(0, 1, m)
    X, Y = np.meshgrid(side, side)
    U = X**2 + Y**2
    for _ in range(n):
        U[1:-1, 1:-1] += beta*(U[2:, 2:] - U[:-2, 2:] -
                               U[2:, :-2] + U[:-2, :-2])
    return U


m = 40
n = 4
beta = 0.5     # pas encore boum

# m = 40
# n = 40
# beta = 0.5    # Boum boum

# m = 40
# n = 400
# beta = 0.3   # Boum boum boum

tic = time.time()
U = edpEuler(m, n, beta)
toc = time.time() - tic
print(f' === Loops version :      elapsed time is {toc} seconds.')
tic = time.time()
U = edpEuler_vectorized(m, n, beta)
toc = time.time() - tic
print(f' === Vectorized version : elapsed time is {toc} seconds.')


alpha = np.linspace(0, 1, m)
[X, Y] = np.meshgrid(alpha, alpha)
plt.contourf(X, Y, U, 10, cmap=myColorMap)
plt.contour(X, Y, U, 10, colors='k', linewidths=1)
plt.axis("equal")
plt.axis("off")
plt.show()
