import random

health = 5

def d6():
  rng = random.SystemRandom()
  return rng.randint(1, 6)

def prompt():
  word = input("Type roll when you're ready to go: ")
  if word == "roll":
    return d6()
  else:
    word = input("That wasn't right...try again: ")
def check(num):
  flag = False
  print("flag is set from True to " + str(flag) + '!')
  return flag
  
def intro():
  name = input("Ready to play? Tell me your name: ")
  print("Hi " + name + "! Let's get started.")
  print("We both start with " + str(health) + " lives, roll the dice to lose, gain, or inflict damage on me.")
  print("Last one standing wins...")
  print("Good Luck!\n")
  return name

#plays the game
def init():
  flag = True
  name = intro()
  while flag == True:
    num = prompt()
    flag = check(num)
  print("Game Over")

init()
