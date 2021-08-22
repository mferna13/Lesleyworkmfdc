import random
def roll_10_dice():
    result = []
    for i in range(10):
        dice_roll = random.radint (1, 6)
        result.append(dice_roll)
    return result