import pandas as pd

data = pd.read_csv('data.csv')
data2 = data.copy()

print(data)     #print all dataset

print(data.tail(10)) #print last 10 rows

print(data.describe()) #descpitpion of dataset

data.sort_values('Dangerous', axis = 0, ascending = False,
                 inplace = True, na_position ='first')  #sort data by Dangerness
print(data)

filter = data['symptoms1'] == 'Fever'
data.where(filter, inplace=True)
data.sort_values('symptoms1', axis = 0, ascending = False,
                 inplace = True, na_position ='last')       #filter data with symptoms1 is 'Fever'
print(data)

symp2 = data.symptoms3.value_counts()
print(symp2)    #count of symptoms3
