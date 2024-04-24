

import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

data = pd.read_excel("recommend/files/Specialist.xlsx")

x = data.drop(['Disease', 'Unnamed: 0'], axis = 1)
x_columns = x.columns
y = data.Disease



from sklearn.model_selection import train_test_split

x_train, x_test, y_train , y_test = train_test_split(x ,y, random_state = 50)

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = RandomForestClassifier(n_estimators=200)
model.fit(x_train, y_train)
predictions = model.predict(x_test)
accuracy_score(y_test, predictions)

model = LogisticRegression(max_iter = 1000)
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(predictions)
accuracy_score(y_test, predictions)

import pickle
pickle.dump(model, open('Specalist.pkl', 'wb'))

loaded_model = pickle.load(open('Specalist.pkl', 'rb'))
# Rename columns in new_data to match the feature names used during training
# new_data_dict = {
#     'Symptom_1': [1],   # Replace with actual values for symptoms
#     'Symptom_2': [0],   # Replace with actual values for symptoms
#     'Symptom_3': [1],
#     'Symptom_4': [1],   # Replace with actual values for symptoms
#     'Symptom_5': [0],   # Replace with actual values for symptoms
#     'Symptom_6': [1],
#     'Symptom_7': [1],   # Replace with actual values for symptoms
#     'Symptom_8': [0],   # Replace with actual values for symptoms
#     'Symptom_9': [1],# Replace with actual values for symptoms
#     # Add more symptoms as needed
# }

# # Convert the dictionary to a DataFrame
# new_data = pd.DataFrame(new_data_dict)
# print(new_data)
# new_data.columns = ['a','b','c','d','e','f','g','h','i']  # Replace with the actual feature names used during training

# new_predictions = loaded_model.predict(new_data)