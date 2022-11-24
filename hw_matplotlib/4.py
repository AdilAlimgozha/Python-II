import matplotlib.pyplot as plt

countries = ['Germany','India', 'UK', 'US', 'South Korea', 'Australia']
share = [16.5, 27.8, 24.6, 18.5, 9.3, 3.3]
Explode = [0, 0, 0, 0.2, 0, 0]
colorss = ['cyan', 'red', 'green', 'blue', 'yellow', 'purple']
plt.pie(share, explode = Explode, autopct='%1.2f%%', labels = countries, shadow = True, startangle = 45, colors = colorss)
plt.title('Population Density Index')
plt.axis('equal')
plt.show()