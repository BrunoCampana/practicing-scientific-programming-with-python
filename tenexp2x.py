import pylab

ax = pylab.linspace(0.1, 1., 100)
ayi = 1./ax
aye = 10. * pylab.exp(-2.*ax)
pylab.plot(ax, ayi, color='r', linestyle=':', linewidth=4.)
pylab.plot(ax, aye, color='m', linestyle='--', linewidth=2.)
#pylab.show()
pylab.savefig('tenexp2x.png')
