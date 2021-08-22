import random
#def DiceRoll():
 #   number=random.randint(1,6)
  #  print(number)
#for i in range(10):
 #   DiceRoll()

#def ReturnOneRoll():
 #   number=random.randint(1,6)
  #  return number
#for i in range(10): 
 #   value=ReturnOneRoll()
  #  print(value)

def roll_dice(n):
    dice = [] # start with empty list of dice
    # add random numbers between 1 to 6 to the list
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice


value=roll_dice(4)
print(value)
import random

lst = []
for i in range(3):
    lst.append(random.randint(1, 6))
print(max(lst))
print(min(lst))
print(lst)
print("computer_rolls")
lst=[]
for i in range(3):
    lst.append(random.randint(1,6))
print(max(lst))
print(min(lst))
print(lst)
print("user_rolls")
