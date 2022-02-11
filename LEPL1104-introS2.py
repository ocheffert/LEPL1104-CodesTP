# -*- coding: utf-8 -*-
import numpy as np
from scipy.interpolate import CubicSpline as spline
from matplotlib import pyplot as plt


def plot_my_spline():
    """
    Plot the spline interpolation of sinus
    """
    n = 21
    L = 1
    # interpolation points
    X = np.linspace(-L, L, n)
    U = np.sin(2*np.pi*X)

    # evaluation points
    x = np.linspace(-L, L, 10*n)

    # CubicSpline returns a function !
    spl1: callable = spline(X[0:10], U[:10])
    spl2: callable = spline(X[0:21:2], U[:21:2])

    # evaluate the spline at x
    uSpline1 = spl1(x)
    uSpline2 = spl2(x)

    plt.plot(x, uSpline1, '-b', label='spline sur les 10 premiers points')
    plt.plot(x, uSpline2, '-r', label='spline sur un point sur deux')
    plt.plot(X[:10], U[:10], '.r', markersize=20, label='10 premiers points')
    plt.plot(X[:21:2], U[:21:2], '.b', markersize=10, label='1 point sur 2')
    plt.legend(loc='upper right')
    plt.show()


def practice_with_arrays():
    """
    Practice with arrays and its basic operations
    """
    # Create an array
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Create a 2D array
    b = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])

    # iterate over elements of the the array
    for element in a:
        print(element, end=' ')

    print()
    # iterate over indices of the array
    for index in range(len(a)):
        print(a[index], end=' ')
    print()

    # learn slices  (start:stop:step)
    print(f'a = {a}')
    print(f'a[1:5] = {a[1:5]}')
    print(f'a[1:5:2] = {a[1:5:2]}')
    print(f'a[::2] = {a[::2]}')
    # fast way to reverse an array in pure python :-)
    print(f'a[::-1] = {a[::-1]}')

    # a view vs a copy !!
    a_view = a[1:5]
    a_copy = a[1:5].copy()
    a_view[0] = 100
    print(f'a = {a}')
    print(f'a_view = {a_view}')
    print(f'a_copy = {a_copy}')

    # allocate via zeros
    A = np.zeros((3, 3))
    # fill with random stuff
    for i in range(3):
        for j in range(3):
            A[i, j] = np.random.rand()
    b = np.array([1, 2, 3])
    # solve the linear system
    print(np.linalg.solve(A, b))


def quick_dotProduct(a, b):
    """
    Dot product of two arrays
    """
    return np.dot(a, b)  # same as a @ b


def slow_dotProduct(a, b):
    """
    Dot product of two arrays
    """
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


if __name__ == '__main__':
    from time import time

    practice_with_arrays()

    plot_my_spline()

    print("\n--------Perf of dot product----------")
    v1 = np.ones(100_000)
    v2 = np.ones(100_000)
    before = time()
    quick_dotProduct(v1, v2)
    after = time()
    print(f"elapsed time of quick_dotProduct: {after - before}[s]")
    slow_dotProduct(v1, v2)
    print(f"elapsed time of slow_dotProduct: {time() - after}[s]")
