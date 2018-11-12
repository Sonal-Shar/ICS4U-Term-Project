
import tkinter as tk
from PIL import Image, ImageTk
button_flag = True

def click():
    """
    respond to the button click
    """
    global button_flag
    # toggle button colors as a test
    if button_flag:
        button1.config(bg="white")
        button_flag = False
    else:
        button1.config(bg="green")
        button_flag = True

root = tk.Tk()

# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)

# pick a (small) image file you have in the working directory ...
photo1 = tk.PhotoImage(file="200btn.png")

# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, compound=tk.TOP, width=155, height=55, image=photo1,
    text="optional text", bg='green', command=click)
button1.pack(side=tk.LEFT, padx=2, pady=2)

# save the button's image from garbage collection (needed?)
button1.image = photo1

# start the event loop
root.mainloop()