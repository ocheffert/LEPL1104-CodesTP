import matplotlib.pyplot as plt
import numpy as np


def ex62():
    def f(x):
        return x*np.exp(x)
    x = np.linspace(0, 3, 100)
    plt.figure()
    plt.plot(x, f(x))
    plt.grid()
    plt.show()


def ex63():
    def g(x):
        return 2*np.sqrt(x-1)
    x = np.linspace(0, 3, 100)
    plt.figure()
    plt.plot(x, x, label='y = x')
    plt.plot(x, g(x), label='g(x)')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    ex63()
