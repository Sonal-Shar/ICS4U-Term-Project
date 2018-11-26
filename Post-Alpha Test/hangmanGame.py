import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from random import *
import linecache

guess_word=[]

class hangMan(Frame):

    def backEnd():
        def getTheWord():
            wordChooser = random.randint(1, 75)
            guessFile = linecache.getline('words.txt', wordChooser)
            print(guessFile)
            
        def wordLength():
            lenWord = len(guessFile)
            for char in range (lenWord-1):
              word.append("_")
            print (word)
            
        def find(str, ch):
            "This function determines where all the letters of a word are in the word"
            for i, ltr in enumerate(str):
                if ltr == ch:
                    yield i
        def
        while (a < 20):

            user = str(input()).lower()

            order = list(find(guessFile, user))

            #This is used to see if letter has already been guessed
            if (user in guesses):
              print("You have already guessed this letter. Try again.")


            else:
              #This appends all your guesses to a list
              guesses.append(user)



            #Determine if you have the letter or not
              if (len(order)==0 and a <=20):
                guessesLeft = guessesLeft - 1
                print("There is no letter " + user + " in this word. You have " + str(guessesLeft) + " guesses left.")
                wrongChoices += 1
                if (guessesLeft > 0):
                  print("Try Again.")
                if (wrongChoices >= 9):
                  break      




              else:
              #Replaces the letter in the word
                for i in range(len(order)):
                  stop = order[i]

                  word[stop] = user
                print(word)

                if (len(list(find(word, "_")))==0):
                  break


        #End words
        print("GAME OVER")
        if (wrongChoices >= 9 and wrongChoices != 0):
          print("You lose! Your word was " + guessFile)
        else:
          print("You win! You correctly guessed the word " + guessFile)
