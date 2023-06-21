import random

global playerHealth 
global enemyHealth 
global winner
playerHealth = 5
enemyHealth  = 5
winner = ""

def d6():
  rng = random.SystemRandom()
  return rng.randint(1, 6)

def checkHealth():
  if playerHealth <= 0:
    winner = "Computer"
    return False
  else: 
    return True

def checkRoll(roll):
  match roll:
    case 1:
      playerHealth -= 1
      print("That looks like it's going to leave a mark!")
    case 2:
      print("testing 2")
    case 3:
      print("Wild card time baby!\n Let's gooooo!")
      checkRoll(d6())
      checkRoll(d6())
      checkRoll(d6())
    case 4:
      print("Sorry bud looks like nothing happened..")
    case 5:
      playerHealth += 1
      print("You gained a life! How's that fair?!")
    case 6:
      enemyHealth -= 1
      print("Agh I've been wounded!")

def playerTurn():
  word = input("Type roll when you're ready to go: ")
  roll = d6()
  if word == "roll":
    print("You rolled " + str(roll) + "!")
    checkRoll(roll)
    result = checkHealth()
    return result
  else:
    print("That wasn't quite right...try again..\n")
    word = playerTurn()

def intro():
  name = input("Ready to play? Tell me your name: ")
  print("Hi " + name + "! Let's get started.")
  print("We both start with " + str(playerHealth) + " lives, roll the dice to lose, gain, or inflict damage on me.")
  print("Last one standing wins...")
  print("Good Luck!\n")
  return name

#plays the game
def init():
  flag   = True
  name   = intro()
  while flag == True:
    flag = playerTurn()
  print(winner + " won!")
  print("Game Over")
  

init()
# something is wrong here...need to fix it so it checks both player and enemy health,
# determines the winner if there is one,
# then ends the game if there is
