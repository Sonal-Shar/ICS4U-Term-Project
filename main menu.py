import tkinter as tk
from tkinter import *

window = Tk()
  
f = open("logs.txt","r")
line = f.readlines()

def login():
    btn.place_forget()
    lab1= Label(window, text="Username",font=("Helvetica", 32))
    lab1.place(x=350, y=300)
    Label2=Label(window, text="Password", font=("Helvetica", 32))
    Label2.place(x=350, y=350)

    TextArea = Text(width = 26, height=1, font=("Helvetica", 26))
    TextArea.place(x=570, y=300)
    
    TextArea2 = Text(width = 26, height=1, font=("Helvetica", 26))
    TextArea2.place(x=570, y=350)

  
    #e1 = Entry(window)
    #e2 = Entry(window)

    #e1.grid(row=0, column=1)
    #e2.grid(row=1, column=1)
    
    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    btn2 = Button(window, text="Next",font=("Helvetica",15),command=window.quit and window.destroy,height = 6, width = 18)
    btn2.place(x=1030,y=510)
    if TextArea == line:
        print('fdfd')


window.title("Main menu")
 
window.geometry('1400x800')
   
btn = Button(window, text="Login",font=("Helvetica",15),command=login, height = 6, width =18)
btn.place(x=570, y=350) 



    
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
    root.wm_geometry('1400x800')
    root.mainloop()

