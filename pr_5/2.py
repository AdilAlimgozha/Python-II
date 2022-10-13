from tkinter import *

root = Tk()
E1 = Entry(root)
E1.pack()
entry = E1.get()
root.mainloop()
print ("Entered text:", entry)