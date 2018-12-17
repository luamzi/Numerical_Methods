import Lagrange
import numpy as np

#para grau 1
x1 = np.array([0.1, 0.6])
y1 = np.array([1.221, 3.32])
Lagrange(x1, y1, 0.2)

#para grau 2
x = np.array([0.1, 0.6, 0.8])
y = np.array([1.221, 3.32, 4.953])
Lagrange(x, y, 0.2)