from tkinter import *
 
window = Tk()
games = False
interactiveLessons = False

def clicked(event):
    event.widget.grid_remove()

def directoryForGames():
    btn5 = Button(window, text="jeopardy", bg="yellow", fg="blue", command = presetOrNo)
    btn5.grid(column=1, row=0)
    btn6 = Button(window, text="Matching", bg="yellow", fg="blue", command = presetOrNo)
    btn6.grid(column=1, row=2)

def presetOrNo():
    btn5.bind('<Button-3>', clicked)
    btn6.bind('<Button-4>', clicked)
    print("I ran out of time")
def interactiveLessons():
    btn.bind('<Button-1>', clicked)
    btn2.bind('<Button-2>', clicked)
    btn3.bind('<Button-3>', clicked)
    btn4.bind('<Button-4>', clicked)
    print("This is where we'd go to the interactive lessons if we had that")

def directoryForLogs():
    btn.bind('<Button-1>', clicked)
    btn2.bind('<Button-2>', clicked)
    btn3.bind('<Button-3>', clicked)
    btn4.bind('<Button-4>', clicked)
    print("I ran out of time")

def Settings():
    print("This is where the settings would go")
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
btn = Button(window, text="Games", command =directoryForGames)
btn.grid(column=1, row=0)
btn2 = Button(window, text="Interactive Lessons", command =interactiveLessons)
btn2.grid(column=1, row=1)
btn3 = Button(window, text="Logs", command =directoryForLogs)
btn3.grid(column=1, row=2)
btn4 = Button(window, text="Settings", command =Settings)
btn4.grid(column=1, row=3)

window.mainloop()
