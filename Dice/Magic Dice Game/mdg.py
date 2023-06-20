import random

health = 10

def d6():
  rng = random.SystemRandom()
  return rng.randint(1, 6)

def prompt(flag):
  print("flag is set from " + str(flag) + " to false!")
  return False

def intro():
  name = input("Ready to play? Tell me your name: ")
  print("Hi " + name + "! Let's get started.")
  print("We both start with 5 lives, roll the dice to lose, gain, or inflict damage on me."
  print("Good Luck!\n")
  return name

#plays the game
def init():
  flag = True
  name = intro()
  while flag == True:
    flag = prompt()
  print("Game Over")

init()
