import numpy as np

'''a = np.array([[64392, 31655],
 [32579,     0],
 [49248,   462],
 [    0,     0]], dtype=np.uint16)


print(a)
print("Array shape is: ", a.shape)
print("Array dimentions are", a.ndim)
print("Length of each element of array in bytes is", a.itemsize)'''


"""a = np.zeros((5, 2))

num = 100

for row in a:
    for i in range(len(row)):
        row[i] = num
        num += 10
print(a)"""


sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
array_transpose = sampleArray.transpose()

print(array_transpose[1])
