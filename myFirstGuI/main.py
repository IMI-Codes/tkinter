from tkinter import *

gui = Tk()
gui.config(bg='whitesmoke')
gui.geometry('500x500')


def greetings():
  username = name.get()
  greet = f"Hello {username}"
  greeting = Label(gui,text=greet)
  greeting.pack()

name = Entry(gui,width=50)
name.pack()
name.insert(0, 'Please Enter a Name')
submit = Button(gui,text='Submit',command=greetings, padx=25, fg='firebrick',bg='black',font='monospace')
submit.pack()



gui.mainloop()