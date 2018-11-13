import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time

qLs = open('questions.txt').read().splitlines()
pLs = open('answers.txt').read().splitlines()
class question(Frame):
    window = tk()
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)




   
def main():
    app = question.question1()
    window.mainloop()
if __name__ == '__main__':
    main()
