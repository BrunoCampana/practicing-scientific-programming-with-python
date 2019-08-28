import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(-2, 2, 1000)
#the syntax line_cosh, = ... to assign the returned line object to the variable line_cosh rather than the list containing that object
line_cosh, = ax.plot(x, np.cosh(x))
line_quad, = ax.plot(x, x**2 / 2)
plt.show()
