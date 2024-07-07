from tkinter import *

gui = Tk()
gui.title('Simple Calculator')
gui.geometry('800x650')



#function definitions

def addition():
  global convNum1
  global math
  math = "addition"
  num1 = userInput.get()
  convNum1 = int(num1)
  userInput.delete(0,END)

def subtraction():
  global math
  global convNum1
  math = 'subtraction'
  num1 = userInput.get()
  convNum1 = int(num1)
  userInput.delete(0,END)
  
  

def multiplication():
  global math 
  global convNum1
  math = 'multiplication'
  num1 = userInput.get()
  convNum1 = int(num1)
  userInput.delete(0,END)
  

def divide():
  global math 
  global convNum1
  math = 'division'
  num1 = userInput.get()
  convNum1 = int(num1)
  userInput.delete(0,END)
  

def finalAnswer():
  num2 = userInput.get()
  userInput.delete(0,END)
  if math == "addition":
    userInput.insert(0, convNum1 + int(num2))
  elif math == "subtraction":
    userInput.insert(0, convNum1 - int(num2))
  elif math == 'division':
    userInput.insert(0,convNum1 / int(num2))
  elif math == 'multiplication':
    userInput.insert(0,convNum1  * int(num2)) 
    
    

def button_click(number):
  current = userInput.get()
  userInput.delete(0,END)
  userInput.insert(0,str(current)+str(number))
  
def clearScreen():
  userInput.delete(0,END)

#input box
userInput = Entry(gui,width=50,borderwidth=5)
userInput.grid(row=0,column=0, columnspan=4, padx=5,pady=2)


#creating buttons 

add = Button(gui,text="+",padx=40,pady=40,command=addition)
equal = Button(gui,text="=",padx=40,pady=40,command=finalAnswer)
clear = Button(gui,text="CE",padx=40,pady=40,command=clearScreen)
subtract = Button(gui,text="-",padx=40,pady=40,command=subtraction)
multiply = Button(gui,text="X",padx=40,pady=40,command=multiplication)
division = Button(gui,text='/',padx=40,pady=40,command=divide)

button_1 = Button(gui,text=1, padx=40,pady=40,command=lambda: button_click(1))
button_2 = Button(gui,text=2, padx=40,pady=40,command=lambda: button_click(2))
button_3 = Button(gui,text=3, padx=40,pady=40,command=lambda: button_click(3))
button_4 = Button(gui,text=4, padx=40,pady=40,command=lambda: button_click(4))
button_5 = Button(gui,text=5, padx=40,pady=40,command=lambda: button_click(5))
button_6 = Button(gui,text=6, padx=40,pady=40,command=lambda: button_click(6))
button_7 = Button(gui,text=7, padx=40,pady=40,command=lambda: button_click(7))
button_8 = Button(gui,text=8, padx=40,pady=40,command=lambda: button_click(8))
button_9 = Button(gui,text=9, padx=40,pady=40,command=lambda: button_click(9))
button_0 = Button(gui,text=0, padx=40,pady=40,command=lambda: button_click(0))



#puts the buttons on the screen
#row 1
clear.grid(row=1,column=1,padx=10,pady=10)
add.grid(row=1,column=2,padx=10,pady=10)
subtract.grid(row=1,column=0,padx=10,pady=10)
multiply.grid(row=1,column=3,padx=10,pady=10)
#row 2
button_7.grid(row=2,column=0, padx=10,pady=10)
button_8.grid(row=2,column=1, padx=10,pady=10)
button_9.grid(row=2,column=2, padx=10,pady=10)

#row 3 
button_4.grid(row=3,column=0, padx=10,pady=10)
button_5.grid(row=3,column=1, padx=10,pady=10)
button_6.grid(row=3,column=2, padx=10,pady=10)

#row 4
button_1.grid(row=4,column=0, padx=10,pady=10)
button_2.grid(row=4,column=1, padx=10,pady=10)
button_3.grid(row=4,column=2, padx=10,pady=10)

#row 5
button_0.grid(row=5,column=1, padx=10,pady=10)
equal.grid(row=5,column=2,padx=10,pady=10)
division.grid(row=5,column=3,padx=10,pady=10)

gui.mainloop()