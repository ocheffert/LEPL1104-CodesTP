import numpy as np


def f(x):
    return x*np.exp(x)


def df(x):
    return np.exp(x)*(1+x)


def NR(x, tol, nmax):
    i = 0
    deltaX = tol + 1

    while i < nmax and abs(deltaX) > tol:
        deltaX = -f(x)/df(x)
        x += deltaX
        i += 1

    print(f'Estimated error after {i} iterations: {abs(deltaX)}')

    return x


print(NR(0.2, 1e-4, 100))
print(NR(20, 1e-4, 100))
