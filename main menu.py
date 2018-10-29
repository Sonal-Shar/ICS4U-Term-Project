import tkinter as tk
from tkinter import *


window = Tk()



def login():
    btn.grid_remove()
    Label(window, text="First Name").grid(row=0)
    Label(window, text="Last Name").grid(row=1)

    e1 = Entry(window)
    e2 = Entry(window)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    btn2 = Button(window, text="next").grid(column=10, row=3)
    

window.title("Main menu")
 
window.geometry('350x200')
   
btn = Button(window, text="Login",command=login).grid(column=1, row=3)

window.mainloop()




