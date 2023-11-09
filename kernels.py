
import numpy as np

h = 1

def Gauss(x):
    c = (h**3)*np.pi**(3/2)
    return np.exp(-x**2)

def cubic(x):
    c = np.pi*h**3
    if 0 <= x <= 1:
        return (1 - 3/2*x**2 + 3/4*x**3)
    if 1 <= x <= 2:
        return (1/4 * (2 - x)**3)
    if x > 2:
        return 0

def Gadget(x):
    c = np.pi*h**3
    return (1 - 6*x**2 + 6*x**3) if 0 <= x <= 0.5 else 2*(1-x)**3 if 0.5 <= x <= 1 else  0
