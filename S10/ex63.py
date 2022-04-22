from cmath import sqrt  # complex sqrt


def PF(x, tol, nmax):
    def iter(xi):
        return 2*sqrt(x-1)

    i = 0
    delta = tol + 1

    while abs(delta) > tol and i < nmax:
        xold = x
        x = iter(xold)
        delta = x - xold
        i += 1

    print(f'Estimated error after {i} iterations: {abs(delta)}')

    return x


print(PF(1.5, 1e-4, 200))
print(PF(2.5, 1e-4, 200))    # plus rapide... voir feuille
