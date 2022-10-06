from tkinter import *

def success_enter(event):
    new_window = Tk()
    L3 = Label(new_window, text = 'success enter')
    L3.pack(side = LEFT)

def check_log_pass(login, password, bd):
    for key in bd.keys():
        print(login)
        if key == login:
            print(key)
            for val in bd.values():
                print(password)
                if val == password:
                    print(val)
                    success_enter()

d = {'Adil': '12345',
    'Timur': '54321',
    'Aruzhan': 'qwerty'}

window = Tk()
L1 = Label(window, text = 'Login')
L2 = Label(window, text = 'Password')
L1.pack(side = LEFT)
L2.pack(side = TOP)
E1 = Entry(window)
E2 = Entry(window)
E1.pack(side = RIGHT)
E2.pack(side = TOP)

B = Button(window, text = 'Enter')
B.bind('<Button-1>', check_log_pass(E1.get(), E2.get(), d))
B.pack(side = BOTTOM)
window.mainloop()