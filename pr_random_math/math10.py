#not finished
from math import *

def is_ten_substring(num_str):
    num_str = str(num_str)
    lst = []
    for i in range(0, len(num_str)):
        sum_val = 0
        substr = ""
        for j in range(i,len(num_str)):
            substr += num_str[j]
            sum_of_substr = list(map(int,substr))
            sum_val = sum(sum_of_substr)
            if sum_val == 10:
                lst.append(substr)
    return lst

num_str="3523014"
print(is_ten_substring(num_str))