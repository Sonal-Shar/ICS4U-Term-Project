import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
master = Tk()
points1 = 0
points2 = 0
points3 = 0
points4 = 0
btnQ = 0
qLs = open('questions.txt').read().splitlines()
pLs = open('answers.txt').read().splitlines()
class question(Frame):
    def question1():
        
        window = Tk()
        window.geometry("1400x800")
        window.resizable(False, False)
        window.title("Question")
        qShow = Label(window,text = qLs[0], font = ("Helvetica",32))
        qShow.place(x = 600, y = 10)
        
        
class Jeopardy(Frame):
        
    def initUI():
        def screen2():
            print("Derp")
        
        master.geometry("1400x800")
        master.resizable(False, False)
        master.title("Jeopardy")

        
        image = Image.open("jeopardywallpaper3.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x = 0, y = 0)

        group1pts = Label(text = "$" + str(points1), font = ("Helvetica", 24), bg = 'white')
        group1pts.place(x = 1060, y= 65)
        image1 = Image.open("200btn.png")
        image2 = Image.open("400btn.png")
        image3 = Image.open("600btn.png")
        image4 = Image.open("800btn.png")
        image5 = Image.open("1000btn.png")
        
        BtnImg1 = ImageTk.PhotoImage(image1)
        BtnImg2 = ImageTk.PhotoImage(image2)
        BtnImg3 = ImageTk.PhotoImage(image3)
        BtnImg4 = ImageTk.PhotoImage(image4)
        BtnImg5 = ImageTk.PhotoImage(image5)
        
        c1r1 = Button(master, image = BtnImg1, command = question.question1, height = 86, width = 185).place(x = 94, y = 285)
        c1r2 = Button(master, image = BtnImg2, command = screen2, height = 86, width = 185).place(x = 94, y = 375)
        c1r3 = Button(master, image = BtnImg3, command = screen2, height = 86, width = 185).place(x = 94, y = 465)
        c1r4 = Button(master, image = BtnImg4, command = screen2, height = 86, width = 185).place(x = 94, y = 555)
        c1r5 = Button(master, image = BtnImg5, command = screen2, height = 86, width = 185).place(x = 94, y = 645)

        c2r1 = Button(master, image = BtnImg1, command = screen2, height = 86, width = 185).place(x = 299, y = 285)
        c2r2 = Button(master, image = BtnImg2, command = screen2, height = 86, width = 185).place(x = 299, y = 375)
        c2r3 = Button(master, image = BtnImg3, command = screen2, height = 86, width = 185).place(x = 299, y = 465)
        c2r4 = Button(master, image = BtnImg4, command = screen2, height = 86, width = 185).place(x = 299, y = 555)
        c2r5 = Button(master, image = BtnImg5, command = screen2, height = 86, width = 185).place(x = 299, y = 645)

        c3r1 = Button(master, image = BtnImg1, command = screen2, height = 86, width = 185).place(x = 504, y = 285)
        c3r2 = Button(master, image = BtnImg2, command = screen2, height = 86, width = 185).place(x = 504, y = 375)
        c3r3 = Button(master, image = BtnImg3, command = screen2, height = 86, width = 185).place(x = 504, y = 465)
        c3r4 = Button(master, image = BtnImg4, command = screen2, height = 86, width = 185).place(x = 504, y = 555)
        c3r5 = Button(master, image = BtnImg5, command = screen2, height = 86, width = 185).place(x = 504, y = 645)

        c4r1 = Button(master, image = BtnImg1, command = screen2, height = 86, width = 185).place(x = 709, y = 285)
        c4r2 = Button(master, image = BtnImg2, command = screen2, height = 86, width = 185).place(x = 709, y = 375)
        c4r3 = Button(master, image = BtnImg3, command = screen2, height = 86, width = 185).place(x = 709, y = 465)
        c4r4 = Button(master, image = BtnImg4, command = screen2, height = 86, width = 185).place(x = 709, y = 555)
        c4r5 = Button(master, image = BtnImg5, command = screen2, height = 86, width = 185).place(x = 709, y = 645)

        c5r1 = Button(master, image = BtnImg1, command = screen2, height = 86, width = 185).place(x = 914, y = 285)
        c5r2 = Button(master, image = BtnImg2, command = screen2, height = 86, width = 185).place(x = 914, y = 375)
        c5r3 = Button(master, image = BtnImg3, command = screen2, height = 86, width = 185).place(x = 914, y = 465)
        c5r4 = Button(master, image = BtnImg4, command = screen2, height = 86, width = 185).place(x = 914, y = 555)
        c5r5 = Button(master, image = BtnImg5, command = screen2, height = 86, width = 185).place(x = 914, y = 645)


        c6r1 = Button(master, image = BtnImg1, command = screen2, height = 86, width = 185).place(x = 1119, y = 285)
        c6r2 = Button(master, image = BtnImg2, command = screen2, height = 86, width = 185).place(x = 1119, y = 375)
        c6r3 = Button(master, image = BtnImg3, command = screen2, height = 86, width = 185).place(x = 1119, y = 465)
        c6r4 = Button(master, image = BtnImg4, command = screen2, height = 86, width = 185).place(x = 1119, y = 555)
        c6r5 = Button(master, image = BtnImg5, command = screen2, height = 86, width = 185).place(x = 1119, y = 645)
        c1r1.image = BtnImg1

    
   
def main():
   # popUpGame = popUp()
    game = Jeopardy.initUI()
    #game = question.initUI()
    master.mainloop()  

if __name__ == '__main__':
    main()
