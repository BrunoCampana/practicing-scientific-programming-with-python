import pylab
import random

# For example, take 5,000 random values from the normal distribution with mean 0 and
#standard deviation 2

data = []
for i in range(5000):
    data.append(random.normalvariate(0,2))
pylab.hist(data, bins=20, density=True)

pylab.savefig('histogram_normed.png')
