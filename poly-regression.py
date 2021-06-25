import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score
from scipy import stats

# X is the hour of the day
# Y is the speed that a car has passed by a tollbooth
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]



# Calculating the linear regression (bad R)
slope, intercept, r, p, std_err = stats.linregress(x, y)
print("R (linear):", r)




# Calculating the polinomial regression (good R)
mymodel = numpy.poly1d(numpy.polyfit(x, y, 5))
print("R (polinomial): ", r2_score(y, mymodel(x)))



# Predict the speed of a car that passes in the tollbooth at 17hrs
speed = mymodel(17)
print("Speed (at 17hrs): ", speed)



# Plotting the grath from 0hrs to 24hrs
myline = numpy.linspace(0, 24, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()