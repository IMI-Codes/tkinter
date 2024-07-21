from customtkinter import *



GUI = CTk()
GUI.title('Leveling Up')

def setuserName():
  userName = userInput.get()
  if len(userName) == 0 or userName == "":
    return
  else:
    newPlayer.setPlayerName(userName)
    welcomeMsg.configure(text=f"Hello {newPlayer.playerName}")
    GUI.update_idletasks()
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


