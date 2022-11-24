import matplotlib.pyplot as plt

countries = ['Germany', 'Greece', 'Iceland', 'Ireland', 'Italy', 'Austria', 'Belgium', 'Denmark', 'Finland', 'France']
share = [10.2, 10.2, 10.7, 17.7, 30.3, 3.6, 3.8, 4.1, 4.2, 5.3]
Explode = []
for i in range(len(countries)):
    Explode.append(0)
plt.pie(share, explode = Explode, autopct='%1.2f%%', labels = countries, startangle = 45)
plt.title('Population Density Index')
plt.axis('equal')
plt.legend(title = "countries", loc = 'best')
plt.show()