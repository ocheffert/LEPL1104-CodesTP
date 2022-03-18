import numpy as np
from matplotlib import pyplot as plt


meth = 'RK'

name = {'RK': '4th order Runge Kutta',
        'EE': 'Explicit Euler', 'EI': 'Implicit Euler'}[meth]

Xstart = 0
Xend = 4
Ustart = 1
x = np.linspace(Xstart, Xend, 100)
u = np.exp(-5*x)+x
def f(x, u): return 5*(x-u) + 1


# return U_i+1 follwowing euler explicit or euler implicit or runge-kutta
# X is the abscissa needed to compute the method (Xi for EE and RK and Xi+1 for EI)
def method(Ui, X):
    if meth == 'EE':
        return Ui + h*(5*(X-Ui)+1)
    elif meth == 'EI':
        return (Ui + h*(5*X+1))/(1+5*h)
    elif meth == 'RK':
        K1 = f(X, Ui)
        K2 = f(X+h/2, Ui+K1*h/2)
        K3 = f(X+h/2, Ui+K2*h/2)
        K4 = f(X+h, Ui+K3*h)
        return Ui + h*(K1+2*K2+2*K3+K4)/6
    else:
        print('method not found')


plt.figure()
for j in range(1, 5):
    n = pow(2, j+1)
    X = np.linspace(Xstart, Xend, n+1)
    h = (Xend - Xstart)/n
    U = np.zeros(n+1)
    U[0] = Ustart
    for i in range(n):
        U[i+1] = method(U[i], X[i])
    plt.subplot(2, 2, j)
    plt.xlim((-0.1, 4.1))
    plt.ylim((-2.0, 6.0))
    plt.yticks(np.arange(-2, 7, 2))
    plt.title(f'{name} with n={n}')
    plt.plot(x, u, '-k', X, U, '.-r', markersize='5.0')
    print(f' u(4) = {U[-1]} ({name} with {n} steps) ')
plt.show()
