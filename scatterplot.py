import pylab
import random

ax, ay = [], []

for i in range(100):
    ax.append(random.random())
    ay.append(random.random())

pylab.scatter(ax,ay)

pylab.savefig('scatterplot.png')
