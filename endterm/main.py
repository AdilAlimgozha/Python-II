from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
from mathematical_part import *

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

class Make_matrix:
    def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('600x700+400+40')

        self.L = Label(self.window, text = 'Construct your matrix in Z5 (only 0, 1, 2, 3, 4 numbers allowed)')
        self.L.place(x = 120, y = 20)

        self.B = Button(self.window, text = 'Calculate SVD')
        self.B.place(x = 280, y = 500)

        self.rows = int(choose_size.size[0])
        self.cols = int(choose_size.size[1])

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
            self.npA = np.array(self.A)
            self.window.destroy()
            solution.create_w()

    def button(self):
        self.B.bind('<Button-1>', self.get_entries)

class Solution:
     def create_w(self):
        self.window = Tk()
        self.window.resizable(False,False)
        self.window.geometry('600x700+400+40')
        self.L = Label(self.window, text = ' Singular value decomposition: A = B*D*C')
        self.L.place(x = 200, y = 20)

        svd = SVD(make_matrix.npA)
        svd.adj()
        svd.find_eigenvalues()
        svd.str_charac_pol()
        svd.D()
        svd.C()
        svd.B()
        svd.mult()

        
        self.L1 = Label(self.window, text = svd.matrixD)
        self.L1.place(x = 200, y = 50)
        self.L11 = Label(self.window, text = "D =")
        self.L11.place(x = 175, y = 60)

        self.L2 = Label(self.window, text = svd.matrixC_t)
        self.L2.place(x = 300, y = 50)
        self.L22 = Label(self.window, text = "C =")
        self.L22.place(x = 275, y = 60)

        self.L3 = Label(self.window, text = svd.matrixB)
        self.L3.place(x = 400, y = 50)
        self.L33 = Label(self.window, text = "B =")
        self.L33.place(x = 375, y = 60)

        self.L4 = Label(self.window, text = "Steps", font = ('Cambria', 20, 'bold'))
        self.L4.place(x = 280, y = 100)

        self.L5 = Label(self.window, text = svd.matrixadjAA)
        self.L5.place(x = 60, y = 150)
        self.L55 = Label(self.window, text = "1) AdjointA(transposed) * A:")
        self.L55.place(x = 60, y = 130)

        self.L6 = Label(self.window, text = svd.char_pol_str + " = 0")
        self.L6.place(x = 30, y = 230)
        self.L66 = Label(self.window, text = "2) Find characterictic polinomyal (A - xI):")
        self.L66.place(x = 60, y = 210)

        self.L7 = Label(self.window, text = svd.matrixEVAL)
        self.L7.place(x = 60, y = 290)
        self.L77 = Label(self.window, text = "3) Find eigenvalues:")
        self.L77.place(x = 60, y = 260)

        self.L8 = Label(self.window, text = svd.matrixD)
        self.L8.place(x = 60, y = 350)
        self.L88 = Label(self.window, text = "4) Find matrix D, where are square roots (r) of eigenvalues on main diagonal:")
        self.L88.place(x = 60, y = 320)

        self.L9 = Label(self.window, text = svd.matrixC_t)
        self.L9.place(x = 60, y = 430)
        self.L99 = Label(self.window, text = "5) Find orthogona matrix C, which is transpose matrix of eigenvectors:")
        self.L99.place(x = 60, y = 400)

        self.L10 = Label(self.window, text = svd.matrixB)
        self.L10.place(x = 60, y = 510)
        self.L1010 = Label(self.window, text = "6) Find matrix B, where b = A*eigenvector/r:")
        self.L1010.place(x = 60, y = 480)

        self.L11 = Label(self.window, text = svd.matrixmult)
        self.L11.place(x = 60, y = 600)
        self.L1111 = Label(self.window, text = "7) Verify that decompisition is correct:")
        self.L1111.place(x = 60, y = 570)

        self.L12 = Label(self.window, text = svd.matrixB)
        self.L12.place(x = 130, y = 600)
        self.L1212 = Label(self.window, text = "=")
        self.L1212.place(x = 110, y = 615)

        self.L13 = Label(self.window, text = svd.matrixD)
        self.L13.place(x = 200, y = 600)
        self.L1313 = Label(self.window, text = "*")
        self.L1313.place(x = 185, y = 620)

        self.L13 = Label(self.window, text = svd.matrixC_t)
        self.L13.place(x = 270, y = 600)
        self.L1313 = Label(self.window, text = "*")
        self.L1313.place(x = 255, y = 620)


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