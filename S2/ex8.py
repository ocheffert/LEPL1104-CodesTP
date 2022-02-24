import numpy as np
from scipy.interpolate import CubicSpline as spline
from matplotlib import pyplot as plt


def compareSplines():
    """ Plot cubic spline and parametric cubic spline (ex8.1-2)
    """
    # Data: interpolation points
    X = np.array([0, 0.5, np.sqrt(3)/2, 1])
    Y = np.array([1, np.sqrt(3)/2, 0.5, 0])

    # interpolate by cubic spline
    yhSpl = spline(X, Y)

    # interpolate by parametric cubic spline with T as parameter
    T = np.array([k*np.pi/6 for k in range(4)])
    xparamSpl = spline(T, X)
    yparamSpl = spline(T, Y)

    # evaluation points
    x = np.linspace(X[0], X[-1], 30)
    t = np.linspace(T[0], T[-1], 30)

    # plot circle and splines
    _, ax = plt.subplots()

    ax.plot(x, yhSpl(x), '-r', label='Cubic spline')
    ax.plot(xparamSpl(t), yparamSpl(t), '-b', label='Parametric cubic spline')
    plt.scatter(X, Y, label='Interpolation points')

    # plot circle
    circle = plt.Circle((0, 0), 1, color='g', fill=False)
    ax.add_patch(circle)

    # make axis equal in size (looks nicer :)
    ax.set_aspect("equal")

    plt.legend()
    plt.show()


def fullCircle():
    """ Plot full circle using parametric cubic spline (ex 8.3)
    """
    # T must go from 0 to 2*pi
    T = np.array([k*np.pi/6 for k in range(13)])
    X, Y = np.cos(T), np.sin(T)

    xparamSpl = spline(T, X)
    yparamSpl = spline(T, Y)

    # evaluation points
    t = np.linspace(T[0], T[-1], 100)

    # plot circle and splines
    _, ax = plt.subplots()

    ax.plot(xparamSpl(t), yparamSpl(t), '-b', label='Parametric cubic spline')
    plt.scatter(X, Y, label='Interpolation points')

    # plot circle
    circle = plt.Circle((0, 0), 1, color='g', fill=False)
    ax.add_patch(circle)

    # make axis equal in size (looks nicer :)
    ax.set_aspect("equal")

    plt.legend()
    plt.show()


compareSplines()
fullCircle()
