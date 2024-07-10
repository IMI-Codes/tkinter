#using icons, images,exit buttons
from tkinter import *
from PIL import ImageTk,Image

# the main display AKA root
GUI = Tk()
GUI.title('My App')
GUI.geometry('900x700')
# use this to change to default icon pass in the location of the icon to be displayed GUI.iconbitmap()








myImage = ImageTk.PhotoImage(Image.open('pictures\7deb81b3c1be503144df67f61c1c4be9.jpg'))
myLabel = Label(image=myImage)
myLabel.pack()





quitButton = Button(GUI,text="Exit",command=GUI.quit)
quitButton.pack()
GUI.mainloop()