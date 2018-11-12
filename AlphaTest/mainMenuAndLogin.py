import tkinter as tk
from tkinter import *
usernameList = open('usernames.txt').read().splitlines() #Collects data from the text file and stores it in an array
passwordList = open('passwords.txt').read().splitlines() #Collects data from the text file and stores it in an array

window = Tk()
TextArea = Text(width = 26, height=1, font=("Helvetica", 26))
TextArea2 = Text(width = 26, height=1, font=("Helvetica", 26))

class mainMenuAndLogin():
    def mainMenuGUI():
        global btn
        window.title("Main Menu")
        btn= Button(window, text="Login",font=("Helvetica",15),command=mainMenuAndLogin.loginGUI, height = 6, width =18)
        btn.place(x=570, y=350)

        
    def loginGUI():
        global TextArea
        global TextArea2
        
        window.title("Login")
        btn.place_forget()
        lab1= Label(window, text="Username",font=("Helvetica", 32))
        lab1.place(x=350, y=300)
        Label2=Label(window, text="Password", font=("Helvetica", 32))
        Label2.place(x=350, y=350)

        TextArea.place(x=570, y=300)

        TextArea2.place(x=570, y=350)

        btn2 = Button(window, text="Next",font=("Helvetica",15),command=mainMenuAndLogin.loginUI, height = 6, width = 18)
        btn2.place(x=1030,y=510)
        

    def loginUI():
        
        def searchThroughFile(aList, anInteger): #Declare the function
            tempVar = 0 #Variable that will hold index value
            for i in range(len(aList)): #For the range in the length of the list
                if int(aList[i]) == anInteger: #If the input = the index value
                    tempVar = i + 1 #Tempvar is now the index place +1 since most people start counting with one
                    return tempVar #returns the variable
            return -1
    
        userNameSpot = 0
        passwordNameSpot = 0
        usernameInput = TextArea.get("1.0","end-1c")
        passwordInput = TextArea2.get("1.0","end-1c")
        tempUserVar = 37
        tempPassVar = 37
        
        for i in range (len(usernameList)):
            if usernameList[i] == usernameInput:
                usernameSpot = 1
                for j in range (len(passwordList)):
                    if passwordList[i] == passwordInput:
                        passwordSpot = 1
                        if usernameSpot == passwordSpot:
                            window.destroy()
                            break
                        else:
                            print("Incorrect username or password. Please try again.")
                            break
                    else:
                        tempPassVar -= 1
                        if tempPassVar == 0:
                            print("Incorrect username or password. Please try again.")
                        
            else:
                tempUserVar -= 1
                if tempUserVar == 0:
                    print("Incorrect username or password. Please try again.")
                
                
            
        #print (userNameSpot)
        #print(passwordNameSpot)
        #if userNameSpot == passwordNameSpot:
            #window.destroy()
def main():
    window.geometry('1400x800')
    window.resizable(False, False)
    mainMenuAndLogin.mainMenuGUI()
    #mainMenuAndLogin.loginUI()


if __name__ == "__main__":
    main()
    window.mainloop()
