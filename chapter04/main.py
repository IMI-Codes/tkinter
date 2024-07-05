#creating input fields
from tkinter import *
root = Tk()

def myClick():
  hello = "Hello", e.get()
  myLabel = Label(root,text=hello)
  myLabel.pack()
  
e = Entry(root, width=100)
e.pack()
e.insert(0, 'Enter your default Name')

myButton = Button(root,text='click me',command=myClick)
myButton.pack()


root.mainloop()