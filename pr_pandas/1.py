import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pr_pandas\diabetes.csv')
print(data)


amount_outcomes = data.Outcome.value_counts() #1
print("ill people:", amount_outcomes[0])
print("recovered people:", amount_outcomes[1])
amount_people = data.Age.value_counts()
print('the most frequent age 22:', amount_people[22], 'people')


sort_by_insulin = data.sort_values(by = "Insulin") #2
print(sort_by_insulin)


memory = data.memory_usage(deep=True) #3
print(memory)


selection = data.loc[0:10, ['Age', 'SkinThickness', 'BMI', 'Glucose']] #4
print(selection)


grouping = data.groupby(by = 'BloodPressure').DiabetesPedigreeFunction.mean() #5
print(grouping)


sort_by_age = data.sort_values(by = "Age")
x = sort_by_age["Age"]
y = amount_people[x]
plt.plot(x, y)
plt.title("amount of people with diabet in cetrain age")
plt.xlabel("age")
plt.ylabel("amount of people")
plt.grid()
plt.show()