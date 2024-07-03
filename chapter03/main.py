#creating buttons

from tkinter import *

root = Tk() 

def displayGreeting():
  myLabel = Label(root,text='Hello')
  myLabel.pack()
# myButton = Button(root,text='Home',state=DISABLED )
myButton = Button(root,text='Home', padx=50,pady=50,command=displayGreeting,fg="firebrick",bg='black')
myButton.pack()

root.mainloop()