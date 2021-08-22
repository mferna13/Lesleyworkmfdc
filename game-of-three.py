import random

def roll_three_dice():
    result = []
    for i in range(3):
        dice_roll = random.randint(1, 6)
        result.append(dice_roll)
    return result

lst = roll_three_dice()
print("computer_rolls:", lst)
print("computer best:", max(lst))
computer_best=max(lst)
lst = roll_three_dice()
print("user rolls", lst)
print("user best", max(lst))
user_best= max(lst)
if user_best>computer_best:
    print("user wins!!")
elif computer_best>user_best:
    print("computer wins")
else:
    print("It's a tie!")