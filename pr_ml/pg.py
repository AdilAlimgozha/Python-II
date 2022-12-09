import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
data = pd.read_csv('pr_ml\ex1data1 (1).txt', header=None)

# data.rename(columns={'0':'score', '1':'jk'}, inplace=True)
# print(data)
# cols=data.columns
# for column in cols:
#     print(cols)
data.columns=['score', 'jk']
df=pd.DataFrame(data)
# fig, ax = plt.subplots(figsize=(15,7))
# plt.plot(df['score'], color='green')
# plt.plot(df['jk'], color='blue')
# plt.plot('-')
# plt.legend()
# data.groupby(['0']).count()['1'].plot(ax=ax)
# plt.show()

slope = np.polyfit (df.score , df.jk ,1)[ 0 ] 
intercept = np.polyfit (df.score , df.jk ,1)[ 1 ]

#create scatterplot 
plt.scatter(df.score, df.jk)
# plt.plot(df.score, df.jk, linewidth=3, linestyle='-')
#add regression line 
plt.show()