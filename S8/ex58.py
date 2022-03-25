import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-3, 3, 1000), np.linspace(-3, 3, 1000))

z = x + 1j*y   # z is h \lambda
# the 4th arg means draw for values in [0,1] with step 0.1
plt.contourf(x, y, np.abs(1+z+z*z/2),
             np.arange(0, 1.1, 0.1), cmap=plt.cm.jet_r)
plt.grid()
plt.show()
