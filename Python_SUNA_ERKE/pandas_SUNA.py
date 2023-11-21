import pandas as pd

df = pd.read_csv('job.csv')

print(df)   #print all dataset

print(df.head(20)) #first 20 rows

conpany_name = df['company_name']
print(conpany_name)     #print all comany names

df.sort_values('experience', axis = 0, ascending = True,
                 inplace = True, na_position ='first')    #sort values by experience
print(df)               

cols = pd.DataFrame(df, columns = ['job_title', 'company_name', 'location']) #select obly this columns
print(cols)

count = df.job_title.value_counts()
print(count)    #count of jobs