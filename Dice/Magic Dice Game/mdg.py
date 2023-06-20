import random

def d6():
  rng = random.SystemRandom()
  return rng.randint(1, 6)
"""
def scoreKeeper(player, score):
  rows = []
  with open('score.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      rows.append(row)
  
  with open('score.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
      writer.write(row)
"""
def prompt(flag):
  print("flag is set from " + str(flag) + " to false!")
  return False

#plays the game
def init():
  flag = True
  name = input("Ready to play? Tell me your name: ")
  print("Hi " + name + "! Let's get started.")
  while flag == True:
    flag = prompt(flag)
  print(d6())

init()
