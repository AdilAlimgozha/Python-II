import re
from math import *

s = 'sin1^2+ln1-cos1+tg12+ctg12'
if s[0] == '-':
    s = '0' + s
def calculation_mult_div(si, nu):
    i = 0
    while '*' in si or "/" in si:
        if si[i] == "*":
            nu[i] = nu[i] * nu[i+1]
            del nu[i+1]
            del si[i]
        elif si[i] == "/":
            nu[i] = nu[i] / nu[i+1]
            del nu[i+1]
            del si[i]
        else:
            i += 1
            
def calculation_plus_minus(si,nu):
    i = 0
    while '+' in si or '-' in si:
        if si[i] == "+":
            nu[i] = nu[i] + nu[i+1]
            del nu[i+1]
            del si[i]
        elif si[i] == "-":
            nu[i] = nu[i] - nu[i+1]
            del nu[i+1]
            del si[i]
        else:
            i += 1

def degree(si, nu):
    i = 0
    while '^' in si:
        if si[i] == '^':
            nu[i] = pow(nu[i], nu[i+1])
            del nu[i+1]
            del si[i]
        else:
            i += 1
            
num = re.split('\+|\-|\*|\/|\^', s)
for i in range(len(num)):
    if 'sin' not in num[i] and 'cos' not in num[i] and 'tg' not in num[i] and 'ctg' not in num[i] and 'ln' not in num[i]:
        num[i] = float(num[i])
    else:
        if 'sin' in num[i]:
            dig = ''
            for x in num[i]:
                if x.isdigit() or x == '.':
                    dig += x
                    num[i] = sin(float(dig))
        elif 'cos' in num[i]:
            dig = ''
            for x in num[i]:
                if x.isdigit() or x == '.':
                    dig += x
                    num[i] = cos(float(dig))
        elif 'tg' in num[i] and 'c' not in num[i]:
            dig = ''
            for x in num[i]:
                if x.isdigit() or x == '.':
                    dig += x
                    num[i] = sin(float(dig))/cos(float(dig))
        elif 'ctg' in num[i]:
            dig = ''
            for x in num[i]:
                if x.isdigit() or x == '.':
                    dig += x
                    num[i] = cos(float(dig))/sin(float(dig))
        elif 'ln' in num[i]:
            dig = ''
            for x in num[i]:
                if x.isdigit() or x == '.':
                    dig += x
                    num[i] = log(float(dig))
print(num)

sign = []
for x in s:
    if x.isdigit() == False and x != "." and x != "s" and x != "i" and x != "n" and x != "c" and x != "o" and x != "t" and x != "g" and x != "l":
        sign.append(x)
print(sign)

degree(sign, num)
calculation_mult_div(sign, num)
calculation_plus_minus(sign, num)

print(str(num[0]))