# coin flip code as a function, only prints to console

from random import randint

def coinflip():
  flip = randint(0,1)

  if flip == 1:
    print("Heads")
  else:
    print("Tails")