import matplotlib.pyplot as plt

def append_el(x, s, num):
    for i in range(num):
        x.append(s)

mon = []
tue = []
wed = []
thu = []
fri = []
sat = []
sun = []

append_el(mon, "Mon", 25)
append_el(tue, "Tue", 48)
append_el(wed, "Wed", 75)
append_el(thu, "Thu", 7)
append_el(fri, "Fri", 18)
append_el(sat, "Sat", 68)
append_el(sun, "Sun", 29)

num_bins = 7
plt.hist(mon, num_bins, color = '#20B2AA', width = 0.8)
plt.hist(tue, num_bins, color = '#40E0D0', width = 0.8)
plt.hist(wed, num_bins, color = '#6B8E23', width = 0.8)
plt.hist(thu, num_bins, color = '#DAA520', width = 0.8)
plt.hist(fri, num_bins, color = 'purple', width = 0.8)
plt.hist(sat, num_bins, color = 'plum', width = 0.8)
plt.hist(sun, num_bins, color = '#7FFFD4', width = 0.8)
plt.show()