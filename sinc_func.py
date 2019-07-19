import pylab
import math

x = pylab.linspace(-20, 20, 1001)
y = pylab.sin(x)/x

pylab.plot(x,y)

#pylab.show()

pylab.savefig('sincx.png')

print(y[498:503])
