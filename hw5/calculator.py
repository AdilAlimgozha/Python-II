from tkinter import *
import re
from math import *

xx = 10
yy = 10
s = ""

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

def calculation_degree(si, nu):
    i = 0
    while '^' in si:
        if si[i] == '^':
            nu[i] = pow(nu[i], nu[i+1])
            del nu[i+1]
            del si[i]
        else:
            i += 1

def show_digit(i):
    global xx, yy
    global s, L
    L.destroy()
    s += "{index}".format(index = i)
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_plus():
    global xx, yy
    global s, L
    L.destroy()
    s += "+"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_mult():
    global xx, yy
    global s, L
    L.destroy()
    s += "*"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_minus():
    global xx, yy
    global s, L
    L.destroy()
    s += "-"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_div():
    global xx, yy
    global s, L
    L.destroy()
    s += "/"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_degree():
    global xx, yy
    global s, L
    L.destroy()
    s += "^"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_dot():
    global xx, yy
    global s, L
    L.destroy()
    s += "."
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_sine():
    global xx, yy
    global s, L
    L.destroy()
    s += "sin"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_cosine():
    global xx, yy
    global s, L
    L.destroy()
    s += "cos"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_tg():
    global xx, yy
    global s, L
    L.destroy()
    s += "tg"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_ctg():
    global xx, yy
    global s, L
    L.destroy()
    s += "ctg"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)
def show_ln():
    global xx, yy
    global s, L
    L.destroy()
    s += "ln"
    L = Label(window, text = s, font = ('Arial', 30))
    L.place(x = xx, y = yy)

def show_result():
    global xx, yy
    global s, L 
    L.destroy()
    if s[0] == '-':
        s = '0' + s
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
    sign = []
    for x in s:
        if x.isdigit() == False and x != '.' and x != "s" and x != "i" and x != "n" and x != "c" and x != "o" and x != "t" and x != "g" and x != "l":
            sign.append(x)
    calculation_degree(sign, num)
    calculation_mult_div(sign, num)
    calculation_plus_minus(sign, num)
    s = str(num[0])
    L = Label(window, text = str(num[0]), font = ('Arial', 30))
    L.place(x = xx, y = yy)

window = Tk()
window.geometry('600x600')
L = Label(window, text = '', font = ('Arial', 30))
L.place(x = xx, y = yy)

buttons = [Button(window, text = '0', height = 5, width = 10),
Button(window, text = '1', height = 5, width = 10),
Button(window, text = '2', height = 5, width = 10),
Button(window, text = '3', height = 5, width = 10),
Button(window, text = '4', height = 5, width = 10),
Button(window, text = '5', height = 5, width = 10),
Button(window, text = '6', height = 5, width = 10),
Button(window, text = '7', height = 5, width = 10),
Button(window, text = '8', height = 5, width = 10),
Button(window, text = '9', height = 5, width = 10)]
plus = Button(window, text = '+', font = ('Arial', 31), height = 1, width = 2)
mult = Button(window, text = '*', font = ('Arial', 31), height = 1, width = 2)
minus = Button(window, text = '-', font = ('Arial', 31), height = 1, width = 2)
div = Button(window, text = '/', font = ('Arial', 31), height = 1, width = 2)
degree = Button(window, text = '^', font = ('Arial', 31), height = 1, width = 2)
dot = Button(window, text = '.', font = ('Arial', 30), height = 1, width = 3)
sine = Button(window, text = 'sin', font = ('Arial', 9), height = 5, width = 7)
cosine = Button(window, text = 'cos', font = ('Arial', 9), height = 5, width = 7)
tg = Button(window, text = 'tg', font = ('Arial', 9), height = 5, width = 7)
ctg = Button(window, text = 'ctg', font = ('Arial', 9), height = 5, width = 7)
ln = Button(window, text = 'ln', font = ('Arial', 9), height = 5, width = 7)
equal = Button(window, text = '=', font = ('Arial', 30), height = 1, width = 3)

r = 240
c = 0
for i in range(len(buttons)):
    if i == 0:
        buttons[i].place(x = c+80, y = r + 240)
    if 1 <= i <= 3:
        buttons[i].place(x = c, y = r)
        c += 80
    if 4 <= i <= 6:
        buttons[i].place(x = c - 240, y = r + 80)
        c += 80
    if 7 <= i <= 9:
        buttons[i].place(x = c - 480, y = r + 160)
        c += 80
plus.place(x = 240, y = 320)
mult.place(x = 240, y = 240)
minus.place(x = 240, y = 403)
div.place(x = 240, y = 484)
degree.place(x = 357, y = 320)
dot.place(x = 0, y = 486)
sine.place(x = 298, y = 240)
cosine.place(x = 298, y = 320)
tg.place(x = 298, y = 403)
ctg.place(x = 298, y = 484)
ln.place(x = 357, y = 240)
equal.place(x = 160, y = 486)

buttons[0].bind('<Button-1>', lambda event: show_digit(0))
buttons[1].bind('<Button-1>', lambda event: show_digit(1))
buttons[2].bind('<Button-1>', lambda event: show_digit(2))
buttons[3].bind('<Button-1>', lambda event: show_digit(3))
buttons[4].bind('<Button-1>', lambda event: show_digit(4))
buttons[5].bind('<Button-1>', lambda event: show_digit(5))
buttons[6].bind('<Button-1>', lambda event: show_digit(6))
buttons[7].bind('<Button-1>', lambda event: show_digit(7))
buttons[8].bind('<Button-1>', lambda event: show_digit(8))
buttons[9].bind('<Button-1>', lambda event: show_digit(9))
plus.bind('<Button-1>', lambda event: show_plus())
mult.bind('<Button-1>', lambda event: show_mult())
minus.bind('<Button-1>', lambda event: show_minus())
div.bind('<Button-1>', lambda event: show_div())
degree.bind('<Button-1>', lambda event: show_degree())
dot.bind('<Button-1>', lambda event: show_dot())
sine.bind('<Button-1>', lambda event: show_sine())
cosine.bind('<Button-1>', lambda event: show_cosine())
tg.bind('<Button-1>', lambda event: show_tg())
ctg.bind('<Button-1>', lambda event: show_ctg())
ln.bind('<Button-1>', lambda event: show_ln())
equal.bind('<Button-1>', lambda event: show_result())

window.mainloop()