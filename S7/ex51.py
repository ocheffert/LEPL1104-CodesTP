import numpy as np

Xstart = 0
Xend = 1
Ustart = 0
Uend = 0.5*(np.exp(Xend) - np.sin(Xend) - np.cos(Xend))
# number of experiments
nE = 8
# store the error at Xend
Eexpl = np.zeros(nE)
Eimpl = np.zeros(nE)

for j in range(nE):
    # n is the number of subintervals equispaced by h
    n = pow(2, j+1)
    h = (Xend-Xstart)/n
    X = np.linspace(Xstart, Xend, n+1)
    # Uexpl is the solution of the explicit method
    Uexpl = np.zeros(n+1)
    Uexpl[0] = Ustart
    # Uimpl is the solution of the implicit method
    Uimpl = np.zeros(n+1)
    Uimpl[0] = Ustart
    # iterates over the subintervals from Xstart to Xend
    for i in range(n):
        # apply the explicit method
        Uexpl[i+1] = Uexpl[i] + h*(np.sin(X[i]) + Uexpl[i])
        # apply the implicit method
        Uimpl[i+1] = (Uimpl[i] + h*np.sin(X[i+1]))/(1 - h)
    # store the error at Xend
    Eexpl[j] = abs(Uexpl[-1] - Uend)
    Eimpl[j] = abs(Uimpl[-1] - Uend)

# compute the order of convergence
Oexpl = np.log(abs(Eexpl[:-1]/Eexpl[1:]))/np.log(2)
Oimpl = np.log(abs(Eimpl[:-1]/Eimpl[1:]))/np.log(2)
print("orderExpl ", *['%.4f ' % val for val in Oexpl])
print("orderImpl ", *['%.4f ' % val for val in Oimpl])

# compute the mean of the order of convergence
print("meanExpl ", np.mean(Oexpl))
print("meanImpl ", np.mean(Oimpl))
