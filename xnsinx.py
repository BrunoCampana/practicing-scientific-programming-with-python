import pylab
#pylab.rc('text', usetex=True)

x = pylab.linspace(-10,10,1001)
for n in range(1,5):
    y = x**n * pylab.sin(x)
    y /= max(y)
pylab.plot(x,y, label=r'$x^{}\sin x$'.format(n))
pylab.legend(loc='lower center')
#pylab.show()
pylab.savefig('xnsinx.png')
