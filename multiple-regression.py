import pandas
from sklearn import linear_model

# CSV with cars (name, model, volume, weight and CO2 emission)
df = pandas.read_csv("cars.csv")


# Specifying X as the elements to analise and Y as the conclusion element
# That means: we want to see if there is a correlation between weight and volume with the emission of CO2
X = df[['Weight', 'Volume']]
y = df['CO2']

# Create a linear regression based on X, Y
regr = linear_model.LinearRegression()
regr.fit(X, y)


# Predict the emission of CO2 of a car with 2300Kg and volume 1300cm3
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)

# The coef indicates the proportion of Weight (1Kg) that affects CO2 (1g),
# and the proportion of Volume (1cm3) that affects CO2 (1g)
print(regr.coef_)