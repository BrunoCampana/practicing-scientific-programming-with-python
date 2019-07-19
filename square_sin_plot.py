import pylab
import math

n = 1000

xmin, xmax = -2. * math.pi, 2. * math.pi

x = pylab.linspace(xmin, xmax, n)

y = pylab.sin(x)**2

pylab.plot(x,y)

#pylab.show()

pylab.savefig('square_sin_plot.png')

'''
This is called vectorization and is described in more detail in Section 6.1.3. Lists
and tuples can be turned into array objects supporting vectorization with the array
constructor method
'''
