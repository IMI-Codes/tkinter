from customtkinter import *
from tools.play import player

GUI = CTk()
GUI.title('Leveling Up')
newPlayer = player()

def setuserName():
  userName = userInput.get()
  if len(userName) == 0:
    return
  else:
    newPlayer.setPlayerName(userName)
#Components
welcomeMsg = CTkLabel(master=GUI,text=f"Hello {newPlayer.playerName}",font=("Roboto",75))

#Getting userName
nameRequest = CTkLabel(master=GUI,text="Please Enter your Name")
userInput = CTkEntry(master=GUI,width=100)
setName = CTkButton(master=GUI,command=setuserName,text="Set New Name")
#Placing components on the screen
welcomeMsg.grid(row=0,column=1)
nameRequest.grid(row=1,column=0)
userInput.grid(row=2,column=0)
setName.grid(row=3,column=0)
#myLabel.pack()
GUI.mainloop()


