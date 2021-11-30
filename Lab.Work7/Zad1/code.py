from numpy import *
import matplotlib.pyplot as plt
x = linspace(-3, 3, 1000)
y = 15*sin(10*x)*cos(3*x)
plt.plot(x, y)
plt.show()