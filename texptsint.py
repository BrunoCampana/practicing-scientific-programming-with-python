import pylab

t = pylab.linspace(0, 2, 1000)
f = t * pylab.exp(t + pylab.sin(20*t))
pylab.plot(t, f)
pylab.xlim(1.5,1.8)
pylab.ylim(0,30)
pylab.savefig('texptsint.png')
