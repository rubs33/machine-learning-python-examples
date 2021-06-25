import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# Reading CSV of shows
# The CSV contains a list of comedians (age, experience, comedy rank, nationality) and whether a customer went to the show
df = pandas.read_csv("shows.csv")

print("Raw data")
print(df)
print()


# Normalizing the data to use only numbers
nationalities = {'UK': 0, 'USA': 1, 'N': 2}
answers = {'YES': 1, 'NO': 0}
reversed_answers = {value : key for (key, value) in answers.items()}

df['Nationality'] = df['Nationality'].map(nationalities)
df['Go'] = df['Go'].map(answers)

print("Normalized data")
print(df)
print()



# Specifying the fields to analise and the conclusion field
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']




# Creating the decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)



# Specifying a new comedian
#print('Age:')
#age = input()
#print('Experience:')
#experience = input()
#print('Rank:')
#rank = input()
#print('Nationality (UK, USA, N):')
#nationality = input();

age = 40
experience = 10
rank = 7
nationality = 'USA'

comedians = [[age, experience, rank, nationalities[nationality] ]]

print(comedians[0])


# Predict whether the customer would go to the show of the new comedian
results = dtree.predict(comedians)

print("Prediction: ", reversed_answers[results[0]])



# Ploting the decision tree
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
