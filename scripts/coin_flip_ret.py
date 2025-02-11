# coin flip function that returns a list object containing flip history

from random import randint

def coinflip(num): 
  flip_results = []

  for x in range(num):
    flip = randint(0,1)
    if flip == 1:
      print("Heads")
    else:
      print("Tails")

    flip_results.append(flip)
    
  return flip_results