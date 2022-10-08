from tkinter import *
import re

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

def show_digit(i):
    global xx, yy
    global s
    L = Label(window, text = "{index}".format(index = i), font = ('Arial', 30))
    L.place(x = xx, y = yy)
    xx += 25
    s += "{index}".format(index = i)
def show_plus():
    global xx, yy
    global s
    L = Label(window, text = '+', font = ('Arial', 30))
    L.place(x = xx, y = yy)
    xx += 25
    s += "+"
def show_mult():
    global xx, yy
    global s
    L = Label(window, text = '*', font = ('Arial', 30))
    L.place(x = xx, y = yy)
    xx += 25
    s += "*"
def show_minus():
    global xx, yy
    global s
    L = Label(window, text = '-', font = ('Arial', 30))
    L.place(x = xx, y = yy)
    xx += 25
    s += "-"
def show_div():
    global xx, yy
    global s
    L = Label(window, text = '/', font = ('Arial', 30))
    L.place(x = xx, y = yy)
    xx += 25
    s += "/"

def show_result():
    global xx, yy
    global s
    
    num = re.split('\+|\-|\*|\/', s)
    for i in range(len(num)):
        num[i] = int(num[i])  

    sign = []
    for x in s:
        if x.isdigit() == False:
            sign.append(x)
    
    calculation_mult_div(sign, num)
    calculation_plus_minus(sign, num)

    L = Label(window, text = '= ' + str(num[0]), font = ('Arial', 30))
    L.place(x = xx, y = yy)
    xx += 25

window = Tk()
window.geometry('600x600')

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
minus.place(x = 240, y = 400)
div.place(x = 240, y = 480)
equal.place(x = 160, y = 484)

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
equal.bind('<Button-1>', lambda event: show_result())

window.mainloop()