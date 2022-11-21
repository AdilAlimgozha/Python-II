import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def append_el(x, s, num):
    for i in range(num):
        x.append(s)

x = []
colors = ['red', 'green', 'blue', 'purple', 'black', 'yellow', 'orange']
append_el(x, "Mon", 25)
append_el(x, "Tue", 48)
append_el(x, "Wed", 75)
append_el(x, "Thu", 7)
append_el(x, "Fri", 18)
append_el(x, "Sat", 68)
append_el(x, "Sun", 29)

num_bins = 7
plt.hist(x, num_bins, rwidth = 0.7)
plt.show()