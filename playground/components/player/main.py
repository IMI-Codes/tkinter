class Player :
  def __init__(self):
    self.Name = "Player"
    self.playerStats = {"Strength":0,"Speed":0}
    self.age = None
  def setName(self,value):
    self.Name = value
  def addStat(self,key,value):
    convertedKey = key.lower()
    if convertedKey in self.playerStats:
      print("Already Exist")
    else:  
      self.playerStats[convertedKey] = value
      print("Success")


newPlayer = Player()
newPlayer.addStat("Strength",0)
