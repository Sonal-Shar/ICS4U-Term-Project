import tkinter as tk
from tkinter import *
import time

window = Tk()
class popUp(Frame):
    
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
        window.geometry("600x400")
        window.title("Settings for Jeopardy")
        btn = Button(window, text="Games", command = Jeopardy.initUI)
        btn.grid(column =1, row = 0)

        
class Jeopardy(Frame):
    
    def initUI():
        master = Tk()
        master.geometry("1400x800")
        master.title("Jeopardy") 

def main():
    popUpGame = popUp()
    window.mainloop()  

if __name__ == '__main__':
    main()  

