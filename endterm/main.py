from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np

class Choose_size:
    def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('200x200+600+300')

        self.frame = Frame(self.window)
        self.frame.pack()
        self.vlist = ["2","3"]
        self.vlist2 = ["2","3"]
        self.Combo1 = ttk.Combobox(self.frame, values = self.vlist, state='readonly')
        self.Combo1.set("m")
        self.Combo1.pack(padx = 5, pady = 5)
        self.Combo2 = ttk.Combobox(self.frame, values = self.vlist2, state='readonly')
        self.Combo2.set("n")
        self.Combo2.pack(padx = 5, pady = 5)

        self.L = Label(self.window, text = """Singular Value Decomposition
Choose the size of a matrix""")
        self.L.place(x = 15, y = 100)

        self.B = Button(self.window, text = 'Enter')
        self.B.place(x = 90, y = 150)

        self.button()

        self.window.mainloop()
    
    def close_1_w_open_2_w(self, event):
        self.get_n_m()
        if self.size != ['m', 'n']:
            self.window.destroy()
            make_matrix.create_w()
        else:
            error_mn.create_w()
            self.size = []

    def button(self):
        self.B.bind('<Button-1>', self.close_1_w_open_2_w)

    def get_n_m(self):
        self.size = []
        self.size.append(self.Combo1.get())
        self.size.append(self.Combo2.get())

        print(self.size)
    
class Make_matrix:
    def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('600x600+400+100')

        self.L = Label(self.window, text = 'Construct your matrix in Z5 (only 0, 1, 2, 3, 4 numbers allowed)')
        self.L.place(x = 120, y = 20)

        self.B = Button(self.window, text = 'Calculate SVD')
        self.B.place(x = 280, y = 500)

        self.rows = int(choose_size.size[0])
        self.cols = int(choose_size.size[1])
        print(self.rows, self.cols)

        self.entries_list = []
        for i in range(self.rows):
            ent_l = []
            for j in range(self.cols):
                ent_l.append(Entry())
            self.entries_list.append(ent_l)
        
        xx = 250
        yy = 50
        for i in range(self.rows):
            for j in range(self.cols):
                self.entries_list[i][j].place(width = 30, height = 30, x = xx, y = yy)
                xx += 50
            xx = 250
            yy += 50

        self.button()
            
        self.window.mainloop()
    
    def get_entries(self, event):
        self.A = []
        for i in range(len(self.entries_list)):
            rowA = []
            for j in range (len(self.entries_list[i])):
                if self.entries_list[i][j].get() == "":
                    error_empty.create_w()
                    rowA = []
                    break
                elif int(self.entries_list[i][j].get()) >= 5:
                    error_Z5.create_w()
                    rowA = []
                    break
                else:
                    rowA.append(int(self.entries_list[i][j].get()))
            if rowA != []:
                self.A.append(rowA)
        else:
            self.window.destroy()
            solution.create_w()
            self.npA = np.array(self.A)
            print(self.npA) #here is svd calculation

    def button(self):
        self.B.bind('<Button-1>', self.get_entries)

class Solution:
     def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('600x600+400+100')
        self.window.mainloop()

class Error_mn:
    def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('200x100+500+300')

        self.L = Label(self.window, text = """ERROR!
        Choose the size""")
        self.L.place(x = 50, y = 15)

        self.B = Button(self.window, text = 'OK')
        self.B.place(x = 100, y = 50)

        self.button()

        self.window.mainloop()

    def close(self, event):
        self.window.destroy()

    def button(self):
        self.B.bind('<Button-1>', self.close)

class Error_Z5:
    def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('200x100+500+300')

        self.L = Label(self.window, text = """ERROR!
The matrix is not in Z5""")
        self.L.place(x = 35, y = 15)

        self.B = Button(self.window, text = 'OK')
        self.B.place(x = 100, y = 50)

        self.button()

        self.window.mainloop()

    def close(self, event):
        self.window.destroy()

    def button(self):
        self.B.bind('<Button-1>', self.close)

class Error_empty:
    def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('200x100+500+300')

        self.L = Label(self.window, text = """ERROR!
The matrix has empty cells""")
        self.L.place(x = 35, y = 15)

        self.B = Button(self.window, text = 'OK')
        self.B.place(x = 100, y = 50)

        self.button()

        self.window.mainloop()

    def close(self, event):
        self.window.destroy()

    def button(self):
        self.B.bind('<Button-1>', self.close)


    

choose_size = Choose_size()
make_matrix = Make_matrix()
solution = Solution()
error_mn = Error_mn()
error_Z5 = Error_Z5()
error_empty = Error_empty()
choose_size.create_w()