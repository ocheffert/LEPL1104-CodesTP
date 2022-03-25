from matplotlib import pyplot as plt
import numpy as np


x, y = np.meshgrid(np.linspace(-3, 3, 1000), np.linspace(-3, 3, 1000))
z = x + 1j*y
b = 0.5 + z/2 + 3*z*z/8
c = z*z/4.0
f1 = abs(b - np.sqrt(b*b - c))
f2 = abs(b + np.sqrt(b*b - c))
gain = np.maximum(f1, f2)
plt.contourf(x, y, gain, np.arange(0, 1.1, 0.1), cmap=plt.cm.jet_r)
plt.contour(x, y, gain, np.arange(0, 1.1, 0.1), colors='black')
ax = plt.gca()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
plt.xticks(np.arange(-3, 4, 1))
plt.yticks(np.arange(-3, 4, 1))
plt.show()
