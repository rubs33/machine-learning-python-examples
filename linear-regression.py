from scipy import stats
import matplotlib.pyplot as plt

# X is the age of a car
# Y is the speed the car passed by a tollbooth
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# Calculating the linear regression
# A linear function has the format: f(x) = a*x + b
# The method lineregress returns: slope (a) and intercept (b)
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Creating a function to predict the value of Y based on the value of X
def myfunc(x):
  return slope * x + intercept



# Predicting the speed of a car of 10 years old
speed = myfunc(10)

print('Speed (car with 10 years old): ', speed)

# Correlation (R): values near 1 or -1 indicate high correlation (of x and y), but values near 0 indicate low correlation
print('R: ', r)



# Plotting
plt.scatter(x, y)
plt.plot(x, list(map(myfunc, x)))
plt.show()

