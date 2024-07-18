from customtkinter import *
from PIL import ImageTk ,Image


GUI = CTk()
GUI.title('Images')

img = ImageTk.PhotoImage(Image.open("chapter06\wingsofFreedom.jpg"))
myLabel = CTkLabel(image=img,master=GUI)
myLabel.pack()
GUI.mainloop()