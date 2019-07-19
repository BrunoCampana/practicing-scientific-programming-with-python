import pylab

#pylab.rc('text', usetex=True)

t = pylab.linspace(0., 0.1, 1000)

Vp_uk, Vp_us = 230, 110

f_uk, f_us = 50, 60

V_uk = Vp_uk * pylab.sin(2 * pylab.pi * f_uk * t)
V_us = Vp_us * pylab.sin(2 * pylab.pi * f_us * t)

pylab.plot(t*1000, V_uk, label='UK')

pylab.plot(t*1000, V_us, label='US')

pylab.title('A comparison of AC voltages in the UK and US')

pylab.xlabel('Time /ms', fontsize=16.)

pylab.ylabel('Voltage /V', fontsize=16.)

pylab.legend()

#pylab.show()

pylab.savefig('voltage.png')
