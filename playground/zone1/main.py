from customtkinter import *
from tools.play import player

GUI = CTk()
GUI.title('Leveling Up')
newPlayer = player()

#Components

welcomMsg = CTkLabel(text=f"Hello {newPlayer.playerName}",master=GUI,font=('Roboto',75))

userName = CTkLabel(text="Please Enter Your Name Below",master=GUI,font=('Roboto',50))

userInput = CTkTextbox(master=GUI)
submit = CTkButton(master=GUI,text="Home")
#Placing components on the screen
welcomMsg.grid(row=0,column=0)
userName.grid(row=1,column=1)
#myLabel.pack()
GUI.mainloop()


