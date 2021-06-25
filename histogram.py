import numpy
import matplotlib.pyplot as plt

# Generating a random sequence of 100000 random numbers from 0.0 to 5.0
x = numpy.random.uniform(0.0, 5.0, 100000)
bars = 100

# Ploting the histogram
print(x)
plt.hist(x, bars)
plt.show()