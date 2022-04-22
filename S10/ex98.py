
def steffensen(x, tol, nmax, f):
    n = 0
    delta = tol + 1
    while abs(delta) >= tol and n < nmax:
        n += 1
        fx = f(x)
        dfdx = (f(x+fx) - fx) / fx
        delta = -fx/dfdx
        x = x + delta
    if n >= nmax:
        return None
    return x


print(steffensen(50, 1e-4, 200, lambda x: x**2 - 1))
