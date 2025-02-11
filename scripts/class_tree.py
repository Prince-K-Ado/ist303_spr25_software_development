class Tree():
  def __init__(self, name:str="Fir", height=3):
    self.name = name
    self.height = height

  def water(self, gallons=10):
    self.height = self.height + gallons * .15
    print(f"I grew! I am now {self.height} feet.")
    self.talk()

  def talk(self):
    print(f"I'm a {self.name} tree. Nice talking to you.")

class DeciduousTree(Tree):
  def __init__(self, *args):  #args are optional
    super().__init__(*args)  #call Tree __init__ with *args
    self.canopy = 100

  def winter(self):
    self.canopy *= .25
    print(f"It is winter and my canopy is at \
    {self.canopy} percent of its former grandeur.")

  def talk(self):
    print(f"I'm a deciduous {self.name} tree. \
    Do you have any leaves for me?")