import tkinter as tk
from tkinter import *
import time

master = Tk()
#class popUp(Frame):
   
#    def __init__(self):
 #       super().__init__()   
  #       
   #     self.initUI()
        
        
    #def initUI(self):
   #     window.geometry("600x400")
     #   window.title("Settings for Jeopardy")
      #  btn = Button(window, text="Games", command = Jeopardy.initUI)
       # btn.grid(column =1, row = 0)

        
class Jeopardy(Frame):
        
    def initUI():
        def screen2():
            print("Derp")
            btn.grid_remove()
        
        master.geometry("1400x800")
        master.title("Jeopardy")
        user = int(input())
        for buttons in range(0,user):
            btn = Button(master, text = "Guess", command = screen2)
            btn.grid(column = buttons, row = 6)
            print(buttons)




def main():
   # popUpGame = popUp()
    game = Jeopardy.initUI()
    master.mainloop()  

if __name__ == '__main__':
    main()


