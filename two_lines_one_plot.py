import pylab
import math

n = 1000

xmin, xmax = -2. * math.pi, 2. * math.pi

x = pylab.linspace(xmin, xmax, n)

y1 = pylab.sin(x)**2
y2 = pylab.cos(x)**2

pylab.plot(x,y1, label='sin^2(x)')
pylab.legend()
pylab.plot(x,y2, label='cos(x)')
pylab.legend()

#pylab.show()

pylab.savefig('two_curves.png')
