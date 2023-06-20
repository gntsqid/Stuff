import random

playerHealth = 5
enemyHealth  = 5

def d6():
  rng = random.SystemRandom()
  return rng.randint(1, 6)

def promptPlayer():
  word = input("Type roll when you're ready to go: ")
  if word == "roll":
    return d6()
  else:
    print("That wasn't quite right...try again..\n")
    word = prompt()

def checkRoll(num):
  print("\nnum was rolled")
  flag = False
  print("flag is set from True to " + str(flag) + '!')
  return flag

def checkHealth():
  if playerHealth <= 0:
    return False
  if  enemyHealth <= 0:
    winner = intro().name
    return False
    
  
def intro():
  name = input("Ready to play? Tell me your name: ")
  print("Hi " + name + "! Let's get started.")
  print("We both start with " + str(health) + " lives, roll the dice to lose, gain, or inflict damage on me.")
  print("Last one standing wins...")
  print("Good Luck!\n")
  return name

#plays the game
def init():
  flag   = True
  winner = ""
  name   = intro()
  while flag == True:
    winner  = promptPlayer()
    checkRoll(num)
    flag = checkHealthP()
    num  = promptEnemy()
    checkRoll(num)
    flag = checkHealth()
  print("Game Over")
  

init()
# something is wrong here...need to fix it so it checks both player and enemy health,
# determines the winner if there is one,
# then ends the game if there is
