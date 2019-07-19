import pylab

theta = pylab.linspace(0, 2.*pylab.pi, 1000)
a = 1.
r = 2 * a * (1. + pylab.cos(theta))
pylab.polar(theta, r)

pylab.savefig('cardioid.png')
