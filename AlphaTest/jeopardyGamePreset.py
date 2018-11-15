import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
master = Tk()
btnQ = 0
timesUp = False
qLs = open('questions.txt').read().splitlines()
pLs = open('answers.txt').read().splitlines()
points1 = 0
class question(Frame):
   
    def question1():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c1r1.destroy()
                window.destroy()
                
            answerInput = TextArea1.get("1.0","end-1c")
            if qc1r1 ==1:
                if pLs[0] == answerInput:
                    checkIfRight.place_forget()
                    TextArea1.place_forget()
                    points1 += 200
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight.place_forget()
                    TextArea1.place_forget()
                    points1 -= 200
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[0] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc1r1
            global checkIfRight
            global TextArea1
            qc1r1 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[0] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea1 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea1.place(x = 480, y = 575)
            checkIfRight = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight.place(x = 1117, y = 560)

        initUI()

    def question2():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c1r2.destroy()
                window.destroy()
                
            answerInput = TextArea2.get("1.0","end-1c")
            if qc1r2 ==1:
                if pLs[1] == answerInput:
                    checkIfRight2.place_forget()
                    TextArea2.place_forget()
                    points1 += 400
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight2.place_forget()
                    TextArea2.place_forget()
                    points1 -= 400
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[1] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc1r2
            global checkIfRight2
            global TextArea2
            qc1r2 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[1] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea2 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea2.place(x = 480, y = 575)
            checkIfRight2 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight2.place(x = 1117, y = 560)

        initUI()
    def question3():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c1r3.destroy()
                window.destroy()
                
            answerInput = TextArea3.get("1.0","end-1c")
            if qc1r3 ==1:
                if pLs[2] == answerInput:
                    checkIfRight3.place_forget()
                    TextArea3.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight3.place_forget()
                    TextArea3.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[2] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc1r3
            global checkIfRight3
            global TextArea3
            qc1r3 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[2] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea3 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea3.place(x = 480, y = 575)
            checkIfRight3 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight3.place(x = 1117, y = 560)

        initUI()

    def question4():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c1r4.destroy()
                window.destroy()
                
            answerInput = TextArea4.get("1.0","end-1c")
            if qc1r4 ==1:
                if pLs[3] == answerInput:
                    checkIfRight4.place_forget()
                    TextArea4.place_forget()
                    points1 += 800
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight4.place_forget()
                    TextArea4.place_forget()
                    points1 -= 800
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[3] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc1r4
            global checkIfRight4
            global TextArea4
            qc1r4 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[3] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea4 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea4.place(x = 480, y = 575)
            checkIfRight4 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight4.place(x = 1117, y = 560)

        initUI()
    def question5():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c1r5.destroy()
                window.destroy()
                
            answerInput = TextArea5.get("1.0","end-1c")
            if qc1r5 ==1:
                if pLs[4] == answerInput:
                    checkIfRight5.place_forget()
                    TextArea5.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight5.place_forget()
                    TextArea5.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[4] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc1r5
            global checkIfRight5
            global TextArea5
            qc1r5 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[4] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea5 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea5.place(x = 480, y = 575)
            checkIfRight5 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight5.place(x = 1117, y = 560)

        initUI()
    def question6():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c2r1.destroy()
                window.destroy()
                
            answerInput = TextArea6.get("1.0","end-1c")
            if qc2r1 ==1:
                if pLs[5] == answerInput:
                    checkIfRight6.place_forget()
                    TextArea6.place_forget()
                    points1 += 200
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight6.place_forget()
                    TextArea6.place_forget()
                    points1 -= 200
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[5] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc2r1
            global checkIfRight6
            global TextArea6
            qc2r1 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[5] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea6 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea6.place(x = 480, y = 575)
            checkIfRight6 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight6.place(x = 1117, y = 560)

        initUI()

    def question7():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c2r2.destroy()
                window.destroy()
                
            answerInput = TextArea7.get("1.0","end-1c")
            if qc2r2 ==1:
                if pLs[6] == answerInput:
                    checkIfRight7.place_forget()
                    TextArea7.place_forget()
                    points1 += 400
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight7.place_forget()
                    TextArea7.place_forget()
                    points1 -= 400
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[6] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc2r2
            global checkIfRight7
            global TextArea7
            qc2r2 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[6] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea7 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea7.place(x = 480, y = 575)
            checkIfRight7 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight7.place(x = 1117, y = 560)

        initUI()
    def question8():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c2r3.destroy()
                window.destroy()
                
            answerInput = TextArea8.get("1.0","end-1c")
            if qc2r3 ==1:
                if pLs[7] == answerInput:
                    checkIfRight8.place_forget()
                    TextArea8.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight8.place_forget()
                    TextArea8.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[7] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc2r3
            global checkIfRight8
            global TextArea8
            qc2r3 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[7] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea8 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea8.place(x = 480, y = 575)
            checkIfRight8 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight8.place(x = 1117, y = 560)

        initUI()

    def question9():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c2r4.destroy()
                window.destroy()
                
            answerInput = TextArea9.get("1.0","end-1c")
            if qc2r4 ==1:
                if pLs[8] == answerInput:
                    checkIfRight9.place_forget()
                    TextArea9.place_forget()
                    points1 += 800
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight9.place_forget()
                    TextArea9.place_forget()
                    points1 -= 800
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[8] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc2r4
            global checkIfRight9
            global TextArea9
            qc2r4 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[8] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea9 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea9.place(x = 480, y = 575)
            checkIfRight9 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight9.place(x = 1117, y = 560)

        initUI()
    def question10():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c2r5.destroy()
                window.destroy()
                
            answerInput = TextArea10.get("1.0","end-1c")
            if qc2r5 ==1:
                if pLs[9] == answerInput:
                    checkIfRight10.place_forget()
                    TextArea10.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight10.place_forget()
                    TextArea10.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[9] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc2r5
            global checkIfRight10
            global TextArea10
            qc2r5 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[9] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea10 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea10.place(x = 480, y = 575)
            checkIfRight10 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight10.place(x = 1117, y = 560)

        initUI()
    def question11 ():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c3r1.destroy()
                window.destroy()
                
            answerInput = TextArea1.get("1.0","end-1c")
            if qc3r1 ==1:
                if pLs[10] == answerInput:
                    checkIfRight.place_forget()
                    TextArea1.place_forget()
                    points1 += 200
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight.place_forget()
                    TextArea1.place_forget()
                    points1 -= 200
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[10] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc3r1
            global checkIfRight
            global TextArea1
            qc3r1 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[10] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea1 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea1.place(x = 480, y = 575)
            checkIfRight = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight.place(x = 1117, y = 560)

        initUI()

    def question12():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c3r2.destroy()
                window.destroy()
                
            answerInput = TextArea2.get("1.0","end-1c")
            if qc3r2 ==1:
                if pLs[11] == answerInput:
                    checkIfRight2.place_forget()
                    TextArea2.place_forget()
                    points1 += 400
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight2.place_forget()
                    TextArea2.place_forget()
                    points1 -= 400
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[11] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc3r2
            global checkIfRight2
            global TextArea2
            qc3r2 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[11] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea2 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea2.place(x = 480, y = 575)
            checkIfRight2 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight2.place(x = 1117, y = 560)

        initUI()
    def question13():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c3r3.destroy()
                window.destroy()
                
            answerInput = TextArea3.get("1.0","end-1c")
            if qc3r3 ==1:
                if pLs[12] == answerInput:
                    checkIfRight3.place_forget()
                    TextArea3.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight3.place_forget()
                    TextArea3.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[12] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc3r3
            global checkIfRight3
            global TextArea3
            qc3r3 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[12] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea3 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea3.place(x = 480, y = 575)
            checkIfRight3 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight3.place(x = 1117, y = 560)

        initUI()

    def question14():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c3r4.destroy()
                window.destroy()
                
            answerInput = TextArea4.get("1.0","end-1c")
            if qc3r4 ==1:
                if pLs[13] == answerInput:
                    checkIfRight4.place_forget()
                    TextArea4.place_forget()
                    points1 += 800
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight4.place_forget()
                    TextArea4.place_forget()
                    points1 -= 800
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[13] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc3r4
            global checkIfRight4
            global TextArea4
            qc3r4 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[13] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea4 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea4.place(x = 480, y = 575)
            checkIfRight4 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight4.place(x = 1117, y = 560)

        initUI()
    def question15():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c3r5.destroy()
                window.destroy()
                
            answerInput = TextArea5.get("1.0","end-1c")
            if qc3r5 ==1:
                if pLs[14] == answerInput:
                    checkIfRight5.place_forget()
                    TextArea5.place_forget()
                    points1 += 1000
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight5.place_forget()
                    TextArea5.place_forget()
                    points1 -= 1000
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[14] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc3r5
            global checkIfRight5
            global TextArea5
            qc3r5 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[14] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea5 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea5.place(x = 480, y = 575)
            checkIfRight5 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight5.place(x = 1117, y = 560)

        initUI()
    def question16():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c4r1.destroy()
                window.destroy()
                
            answerInput = TextArea6.get("1.0","end-1c")
            if qc4r1 ==1:
                if pLs[15] == answerInput:
                    checkIfRight6.place_forget()
                    TextArea6.place_forget()
                    points1 += 200
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight6.place_forget()
                    TextArea6.place_forget()
                    points1 -= 200
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[15] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc4r1
            global checkIfRight6
            global TextArea6
            qc4r1 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[15] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea6 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea6.place(x = 480, y = 575)
            checkIfRight6 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight6.place(x = 1117, y = 560)

        initUI()

    def question17():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c4r2.destroy()
                window.destroy()
                
            answerInput = TextArea7.get("1.0","end-1c")
            if qc4r2 ==1:
                if pLs[16] == answerInput:
                    checkIfRight7.place_forget()
                    TextArea7.place_forget()
                    points1 += 400
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight7.place_forget()
                    TextArea7.place_forget()
                    points1 -= 400
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[16] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc4r2
            global checkIfRight7
            global TextArea7
            qc4r2 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[16] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea7 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea7.place(x = 480, y = 575)
            checkIfRight7 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight7.place(x = 1117, y = 560)

        initUI()
    def question18():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c4r3.destroy()
                window.destroy()
                
            answerInput = TextArea8.get("1.0","end-1c")
            if qc4r3 ==1:
                if pLs[17] == answerInput:
                    checkIfRight8.place_forget()
                    TextArea8.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight8.place_forget()
                    TextArea8.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[17] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc4r3
            global checkIfRight8
            global TextArea8
            qc4r3 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[17] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea8 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea8.place(x = 480, y = 575)
            checkIfRight8 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight8.place(x = 1117, y = 560)

        initUI()

    def question19():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c4r4.destroy()
                window.destroy()
                
            answerInput = TextArea9.get("1.0","end-1c")
            if qc4r4 ==1:
                if pLs[18] == answerInput:
                    checkIfRight9.place_forget()
                    TextArea9.place_forget()
                    points1 += 800
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight9.place_forget()
                    TextArea9.place_forget()
                    points1 -= 800
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[18] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc4r4
            global checkIfRight9
            global TextArea9
            qc4r4 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[18] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea9 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea9.place(x = 480, y = 575)
            checkIfRight9 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight9.place(x = 1117, y = 560)

        initUI()
    def question20():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c4r5.destroy()
                window.destroy()
                
            answerInput = TextArea10.get("1.0","end-1c")
            if qc4r5 ==1:
                if pLs[19] == answerInput:
                    checkIfRight10.place_forget()
                    TextArea10.place_forget()
                    points1 += 1000
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight10.place_forget()
                    TextArea10.place_forget()
                    points1 -= 1000
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[19] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc4r5
            global checkIfRight10
            global TextArea10
            qc4r5 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[19] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea10 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea10.place(x = 480, y = 575)
            checkIfRight10 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight10.place(x = 1117, y = 560)

        initUI()

    def question21():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c5r1.destroy()
                window.destroy()
                
            answerInput = TextArea1.get("1.0","end-1c")
            if qc5r1 ==1:
                if pLs[20] == answerInput:
                    checkIfRight.place_forget()
                    TextArea1.place_forget()
                    points1 += 200
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight.place_forget()
                    TextArea1.place_forget()
                    points1 -= 200
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[20] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc5r1
            global checkIfRight
            global TextArea1
            qc5r1 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[20] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea1 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea1.place(x = 480, y = 575)
            checkIfRight = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight.place(x = 1117, y = 560)

        initUI()

    def question22():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c5r2.destroy()
                window.destroy()
                
            answerInput = TextArea2.get("1.0","end-1c")
            if qc5r2 ==1:
                if pLs[21] == answerInput:
                    checkIfRight2.place_forget()
                    TextArea2.place_forget()
                    points1 += 400
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight2.place_forget()
                    TextArea2.place_forget()
                    points1 -= 400
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[21] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc5r2
            global checkIfRight2
            global TextArea2
            qc5r2 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[21] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea2 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea2.place(x = 480, y = 575)
            checkIfRight2 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight2.place(x = 1117, y = 560)

        initUI()
    def question23():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c5r3.destroy()
                window.destroy()
                
            answerInput = TextArea3.get("1.0","end-1c")
            if qc5r3 ==1:
                if pLs[22] == answerInput:
                    checkIfRight3.place_forget()
                    TextArea3.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight3.place_forget()
                    TextArea3.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[22] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc5r3
            global checkIfRight3
            global TextArea3
            qc5r3 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[22] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea3 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea3.place(x = 480, y = 575)
            checkIfRight3 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight3.place(x = 1117, y = 560)

        initUI()

    def question24():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c5r4.destroy()
                window.destroy()
                
            answerInput = TextArea4.get("1.0","end-1c")
            if qc5r4 ==1:
                if pLs[23] == answerInput:
                    checkIfRight4.place_forget()
                    TextArea4.place_forget()
                    points1 += 800
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight4.place_forget()
                    TextArea4.place_forget()
                    points1 -= 800
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[23] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc5r4
            global checkIfRight4
            global TextArea4
            qc5r4 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[23] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea4 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea4.place(x = 480, y = 575)
            checkIfRight4 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight4.place(x = 1117, y = 560)

        initUI()
    def question25():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c5r5.destroy()
                window.destroy()
                
            answerInput = TextArea5.get("1.0","end-1c")
            if qc5r5 ==1:
                if pLs[24] == answerInput:
                    checkIfRight5.place_forget()
                    TextArea5.place_forget()
                    points1 += 1000
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight5.place_forget()
                    TextArea5.place_forget()
                    points1 -= 1000
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[24] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc5r5
            global checkIfRight5
            global TextArea5
            qc5r5 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[24] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea5 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea5.place(x = 480, y = 575)
            checkIfRight5 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight5.place(x = 1117, y = 560)

        initUI()
    def question26():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c6r1.destroy()
                window.destroy()
                
            answerInput = TextArea6.get("1.0","end-1c")
            if qc6r1 ==1:
                if pLs[25] == answerInput:
                    checkIfRight6.place_forget()
                    TextArea6.place_forget()
                    points1 += 200
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight6.place_forget()
                    TextArea6.place_forget()
                    points1 -= 200
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[25] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc6r1
            global checkIfRight6
            global TextArea6
            qc6r1 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[25] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea6 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea6.place(x = 480, y = 575)
            checkIfRight6 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight6.place(x = 1117, y = 560)

        initUI()

    def question27():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c6r2.destroy()
                window.destroy()
                
            answerInput = TextArea7.get("1.0","end-1c")
            if qc6r2 ==1:
                if pLs[26] == answerInput:
                    checkIfRight7.place_forget()
                    TextArea7.place_forget()
                    points1 += 400
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight7.place_forget()
                    TextArea7.place_forget()
                    points1 -= 400
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[26] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc6r2
            global checkIfRight7
            global TextArea7
            qc6r2 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[26] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea7 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea7.place(x = 480, y = 575)
            checkIfRight7 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight7.place(x = 1117, y = 560)

        initUI()
    def question28():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c6r3.destroy()
                window.destroy()
                
            answerInput = TextArea8.get("1.0","end-1c")
            if qc6r3 ==1:
                if pLs[27] == answerInput:
                    checkIfRight8.place_forget()
                    TextArea8.place_forget()
                    points1 += 600
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight8.place_forget()
                    TextArea8.place_forget()
                    points1 -= 600
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[27] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc6r3
            global checkIfRight8
            global TextArea8
            qc6r3 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[27] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea8 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea8.place(x = 480, y = 575)
            checkIfRight8 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight8.place(x = 1117, y = 560)

        initUI()

    def question29():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c6r4.destroy()
                window.destroy()
                
            answerInput = TextArea9.get("1.0","end-1c")
            if qc6r4 ==1:
                if pLs[28] == answerInput:
                    checkIfRight9.place_forget()
                    TextArea9.place_forget()
                    points1 += 800
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight9.place_forget()
                    TextArea9.place_forget()
                    points1 -= 800
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[28] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc6r4
            global checkIfRight9
            global TextArea9
            qc6r4 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[28] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea9 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea9.place(x = 480, y = 575)
            checkIfRight9 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight9.place(x = 1117, y = 560)

        initUI()
    def question30():
        
        window = Tk()
        #Checks if the answer is right
        def answerCheck():
            global points1
            def destroy():
                c6r5.destroy()
                window.destroy()
                
            answerInput = TextArea10.get("1.0","end-1c")
            if qc6r5 ==1:
                if pLs[29] == answerInput:
                    checkIfRight10.place_forget()
                    TextArea10.place_forget()
                    points1 += 1000
                    group1pts['text'] = "$" + str(points1)
                    right = Label(window, text = "Correct!", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#1DC90A')
                    right.place(x = 650, y = 300)
                else:
                    checkIfRight10.place_forget()
                    TextArea10.place_forget()
                    points1 -= 1000
                    group1pts['text'] = "$" + str(points1)
                    wrong = Label(window, text = "Incorrect, the correct answer is '" + pLs[29] + "'.", font = ("Helvetica",30),bg = '#2C5EB3', fg = '#FF5353')
                    wrong.place(x = 420, y = 300)

            done = Button(window, text = "Next", height = 6, width = 18, command = destroy)
            done.place(x = 1117, y = 560)

        def initUI():    
            global qc6r5
            global checkIfRight10
            global TextArea10
            qc6r5 = 1
            window.geometry("1400x800")
            window.resizable(False, False)
            window.title("Question")
            window.configure(background='#2C5EB3')
            qShow = Label(window,text = "Conjuguer: ' " + qLs[29] + " '", font = ("Helvetica",32), bg = '#2C5EB3', fg = 'white')
            qShow.place(x = 520, y = 10)
            TextArea10 = Text(window, width = 26, height=1, font=("Helvetica", 26))
            TextArea10.place(x = 480, y = 575)
            checkIfRight10 = Button(window, text = "Answer", height = 6, width = 18, command = answerCheck)
            checkIfRight10.place(x = 1117, y = 560)

        initUI()

class Jeopardy(Frame):
        
    def initUI():
        global group1pts
        global c1r1
        global c1r2
        global c1r3
        global c1r4
        global c1r5
        global c2r1
        global c2r2
        global c2r3
        global c2r4
        global c2r5
        global c3r1
        global c3r2
        global c3r3
        global c3r4
        global c3r5
        global c4r1
        global c4r2
        global c4r3
        global c4r4
        global c4r5
        global c5r1
        global c5r2
        global c5r3
        global c5r4
        global c5r5
        global c6r1
        global c6r2
        global c6r3
        global c6r4
        global c6r5
        
        #Sets variables
        image1 = Image.open("200btn.png")
        image2 = Image.open("400btn.png")
        image3 = Image.open("600btn.png")
        image4 = Image.open("800btn.png")
        image5 = Image.open("1000btn.png")
        image1.load()
        image2.load()
        image3.load()
        image4.load()
        image5.load()
        BtnImg1 = ImageTk.PhotoImage(image1)
        BtnImg2 = ImageTk.PhotoImage(image2)
        BtnImg3 = ImageTk.PhotoImage(image3)
        BtnImg4 = ImageTk.PhotoImage(image4)
        BtnImg5 = ImageTk.PhotoImage(image5)

        def screen2():
            print("Derp")
        
        #Sets the window
        master.geometry("1400x800")
        master.resizable(False, False)
        master.title("Jeopardy")

        #Sets background image
        image = Image.open("jeopardywallpaper3.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x = 0, y = 0)

        #Points
        points1 = 0
        group1pts = Label(text = "$" + str(points1), font = ("Helvetica", 24), bg = 'white')
        group1pts.place(x = 1060, y= 65)

    
        
        c1r1 = Button(master, image = BtnImg1, command = question.question1, height = 86, width = 185)
        c1r1.place(x = 94, y = 285)
        c1r2 = Button(master, image = BtnImg2, command = question.question2, height = 86, width = 185)
        c1r2.place(x = 94, y = 375)
        c1r3 = Button(master, image = BtnImg3, command = question.question3, height = 86, width = 185)
        c1r3.place(x = 94, y = 465)
        c1r4 = Button(master, image = BtnImg4, command = question.question4, height = 86, width = 185)
        c1r4.place(x = 94, y = 555)
        c1r5 = Button(master, image = BtnImg5, command = question.question5, height = 86, width = 185)
        c1r5.place(x = 94, y = 645)

        c2r1 = Button(master, image = BtnImg1, command = question.question6, height = 86, width = 185)
        c2r1.place(x = 299, y = 285)
        c2r2 = Button(master, image = BtnImg2, command = question.question7, height = 86, width = 185)
        c2r2.place(x = 299, y = 375)
        c2r3 = Button(master, image = BtnImg3, command = question.question8, height = 86, width = 185)
        c2r3.place(x = 299, y = 465)
        c2r4 = Button(master, image = BtnImg4, command = question.question9, height = 86, width = 185)
        c2r4.place(x = 299, y = 555)
        c2r5 = Button(master, image = BtnImg5, command = question.question10, height = 86, width = 185)
        c2r5.place(x = 299, y = 645)

        c3r1 = Button(master, image = BtnImg1, command = question.question11, height = 86, width = 185)
        c3r1.place(x = 504, y = 285)
        c3r2 = Button(master, image = BtnImg2, command = question.question12, height = 86, width = 185)
        c3r2.place(x = 504, y = 375)
        c3r3 = Button(master, image = BtnImg3, command = question.question13, height = 86, width = 185)
        c3r3.place(x = 504, y = 465)
        c3r4 = Button(master, image = BtnImg4, command = question.question14, height = 86, width = 185)
        c3r4.place(x = 504, y = 555)
        c3r5 = Button(master, image = BtnImg5, command = question.question15, height = 86, width = 185)
        c3r5.place(x = 504, y = 645)

        c4r1 = Button(master, image = BtnImg1, command = question.question16, height = 86, width = 185)
        c4r1.place(x = 709, y = 285)
        c4r2 = Button(master, image = BtnImg2, command = question.question17, height = 86, width = 185)
        c4r2.place(x = 709, y = 375)
        c4r3 = Button(master, image = BtnImg3, command = question.question18, height = 86, width = 185)
        c4r3.place(x = 709, y = 465)
        c4r4 = Button(master, image = BtnImg4, command = question.question19, height = 86, width = 185)
        c4r4.place(x = 709, y = 555)
        c4r5 = Button(master, image = BtnImg5, command = question.question20, height = 86, width = 185)
        c4r5.place(x = 709, y = 645)

        c5r1 = Button(master, image = BtnImg1, command = question.question21, height = 86, width = 185)
        c5r1.place(x = 914, y = 285)
        c5r2 = Button(master, image = BtnImg2, command = question.question22, height = 86, width = 185)
        c5r2.place(x = 914, y = 375)
        c5r3 = Button(master, image = BtnImg3, command = question.question23, height = 86, width = 185)
        c5r3.place(x = 914, y = 465)
        c5r4 = Button(master, image = BtnImg4, command = question.question24, height = 86, width = 185)
        c5r4.place(x = 914, y = 555)
        c5r5 = Button(master, image = BtnImg5, command = question.question25, height = 86, width = 185)
        c5r5.place(x = 914, y = 645)


        c6r1 = Button(master, image = BtnImg1, command = question.question26, height = 86, width = 185)
        c6r1.place(x = 1119, y = 285)
        c6r2 = Button(master, image = BtnImg2, command = question.question27, height = 86, width = 185)
        c6r2.place(x = 1119, y = 375)
        c6r3 = Button(master, image = BtnImg3, command = question.question28, height = 86, width = 185)
        c6r3.place(x = 1119, y = 465)
        c6r4 = Button(master, image = BtnImg4, command = question.question29, height = 86, width = 185)
        c6r4.place(x = 1119, y = 555)
        c6r5 = Button(master, image = BtnImg5, command = question.question30, height = 86, width = 185)
        c6r5.place(x = 1119, y = 645)
        c1r1.image = BtnImg1
        c1r2.image = BtnImg2
        c1r3.image = BtnImg3
        c1r4.image = BtnImg4
        c1r5.image = BtnImg5

    
         

def main():
   # popUpGame = popUp()
    game = Jeopardy.initUI()
    #game = question.question1()
    master.mainloop()  

if __name__ == '__main__':
    main()
