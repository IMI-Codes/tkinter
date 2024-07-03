#Positioning with grid System
""" import tkinter """ #This is valid
from tkinter import *

root = Tk()

myLabel = Label(root, text="You I'm Creating a GUI")
myLabel2 = Label(root, text="Hey You")

myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)

root.mainloop()