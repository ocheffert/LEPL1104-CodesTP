def secante(x0, x1, tol, nmax, f):
    n = 0
    delta = tol + 1
    f0 = f(x0)
    while abs(delta) >= tol and n < nmax:
        n += 1
        f1 = f(x1)
        delta = -f1*(x1-x0)/(f1-f0)
        x0 = x1
        f0 = f1
        x1 = x1 + delta
    return x1


print(secante(-10, -9, 1e-4, 200, lambda x: x**2 - 1))
