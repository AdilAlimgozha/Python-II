from tkinter import *

class Logon:

    def __init__(self, bd):
        self.window = Tk()
        self.bd = bd
        self.window.geometry('600x600+300+100')
        self.L1 = Label(self.window, text = 'Login')
        self.L2 = Label(self.window, text = 'Password')
        self.L1.place(x = 200, y = 200)
        self.L2.place(x = 200, y = 250)
        self.E1 = Entry(self.window)
        self.E2 = Entry(self.window)
        self.E1.place(x = 270, y = 200)
        self.E2.place(x = 270, y = 250)
        self.B = Button(self.window, text = 'Enter')
        self.B.place(x = 300, y = 300)

    def success_enter(self):
        self.window.destroy()
        new_window = Tk()
        new_window.geometry('600x600+300+100')
        L3 = Label(new_window, text = 'success enter')
        L3.pack(side = LEFT)
    
    def not_success_enter(self):
        self.L3 = Label(self.window, text = 'wrong login or password')
        self.L3.pack(side = LEFT)

    def check_log_pass(self, event):
        self.flag = False
        for key in self.bd.keys():
            if key == self.E1.get() and self.bd[key] == self.E2.get():
                self.success_enter()
            else:
                self.not_success_enter()
    
    def button(self):
        self.B.bind('<Button-1>', self.check_log_pass)
    
    def mainloop(self):
        self.window.mainloop()

d = {'Adil': '12345',
    'Timur': '54321',
    'Aruzhan': 'qwerty'}

logon = Logon(d)
logon.button()
logon.mainloop()
