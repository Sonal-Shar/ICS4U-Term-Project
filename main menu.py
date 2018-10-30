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
    btn2 = Button(window, text="next",command=window.quit and window.destroy).grid(column=8, row=3)


window.title("Main menu")
 
window.geometry('350x200')
   
btn = Button(window, text="Login",command=login, height = 4, width = 6)
btn.grid(column=1, row= 3)

window.mainloop()


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self,text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
    

class Page2(Page):
   def __init__(self, *args, **kwargs):# syntax *args in function definitions in python is used to pass a variable number of arguments to a function. 
       Page.__init__(self, *args, **kwargs)#**kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

