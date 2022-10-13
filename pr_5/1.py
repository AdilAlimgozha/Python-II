from cmath import log
from tkinter import *

def success_enter(event):
    new_window = Tk()
    L3 = Label(new_window, text = 'success enter')
    L3.pack(side = LEFT)

def check_log_pass(log, pas, bd):
    global flag
    flag = False
    for key in bd.keys():
        if key == log:
            print(log)
            if bd[key] == pas:
                print(pas)
                flag = True

d = {'Adil': '12345',
    'Timur': '54321',
    'Aruzhan': 'qwerty'}

window = Tk()
window.geometry('600x600')
L1 = Label(window, text = 'Login')
L2 = Label(window, text = 'Password')
L1.pack(side = LEFT)
L2.pack(side = TOP)
E1 = Entry(window)
E2 = Entry(window)

B = Button(window, text = 'Enter')
login = E1.get()
passwd = E2.get()
check_log_pass(login, passwd, d)
E1.pack(side = RIGHT)
E2.pack(side = TOP)
if flag:
    B.bind('<Button-1>', success_enter)
B.pack(side = BOTTOM)
window.mainloop()

check_log_pass(login, passwd, d)
print(login)
print(passwd)