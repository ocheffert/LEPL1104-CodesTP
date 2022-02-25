from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline as spline
import numpy as np


# add 2 points before and after the X and Y data
# the X data are sequences of 0,1,0   (X3 is already an appended virtual data)
X = [1, 0, 0, 1, 0, 0, 1, 0]  # = X[-2:] + X + X3 X[1:3] where X = [0,1,0]
# the Y data are sequences of 0,0,1   (Y3 is already an appended virtual data)
Y = [0, 1, 0, 0, 1, 0, 0, 1]  # = Y[-2:] + Y + Y3 + Y[1:3] where Y = [0,0,1]
T = [0, 1, 2, 3, 4, 5, 6, 7]
t = np.linspace(2, 5, 100)

plt.plot(X[:3], Y[:3], 'or')
plt.plot(spline(T, X)(t), spline(T, Y)(t), '-g')
plt.show()
