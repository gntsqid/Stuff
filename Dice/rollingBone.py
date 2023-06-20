import random

def d20():
  rng = random.SystemRandom()
  return rng.randint(1, 20)

def d6():
  rng = random.SystemRandom()
  return rng.randint(1, 6)

def prompt():
  count = int(input("How many dice are we rolling? "))
  type  = input("Which kind? ")
  match type:
    case 'd20':
      for i in range(count):
        print("you rolled: " + str(d20()))
    case 'd6':
      for i in range(count):
        print("You rolled: " + str(d6()))

prompt()
