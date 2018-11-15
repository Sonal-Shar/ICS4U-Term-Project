import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
global points1
points1 = 0
btnQ = 0
qLs = open('questions.txt').read().splitlines()
pLs = open('answers.txt').read().splitlines()
points1 = 0

class question(Frame):

            
    def question1():
        def answerCheck():
            points1 = 0
            answerInput = TextArea1.get("1.0","end-1c")
            if qc1r1 ==1:
                if pLs[0] == answerInput:
                    print("Hooray, you got it!")
                    points1 = points1 + 200
                    print(points1)
                    window.destroy()
                else: 
                    print("Incorrect, the correct answer is " + str(pLs[0]))
                    points1 = points1 - 200
                    print(points1)
                    window.destroy()
        print(points1)
        global qc1r1
        qc1r1 = 1
        window = Tk()
        window.geometry("1400x800")
        window.resizable(False, False)
        window.title("Question")
        global TextArea1
        window.configure(background='#2C5EB3')
        
        
        qShow = Label(window,text = qLs[0], font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
        qShow.place(x = 600, y = 10)
        TextArea1 = Text(window, width = 26, height=1, font=("Helvetica", 26))
        TextArea1.place(x = 200, y = 600)
        checkIfRight = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck).place(x = 694, y = 375)


def main():
   # popUpGame = popUp()
    #game = Jeopardy.initUI()
    game = question.question1()
    #master.mainloop()

if __name__ == '__main__':
    main()

