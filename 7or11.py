#definingvariables
import random
import time
#function
def roll_dice():
    dice_roll = random.randint(1, 6)
    dice_roll2=random.randint(1,6)
    result=(dice_roll + dice_roll2)
    return result

print("welcome to the game of Lucky sevens and 11s")
money=1000
while money>0:
    # get a valid bet amount
    Bet=input("how much of your " +str(money) + " dollars do you want to bet?")
    BetAmount=int(Bet)
    while BetAmount<=0:
        Bet=input("how much of your " +str(money) + " dollars do you want to bet?")
        BetAmount=int(Bet)
    # calculate the updated money for two scenarios
    NewMoney=money-BetAmount
    if NewMoney<0:
        print("Using a loan shark?")
        time.sleep(4)
    print("After placing your bet you now have", NewMoney)
    winnermoney=BetAmount+money
    losermoney=(money-BetAmount)
    #winnerlooser sequence
    Winner=roll_dice()

    if Winner==7 or Winner==11:
        money=winnermoney
        print("winner winner! " + str(Winner))
        print(winnermoney)
    else:
        print("Sorry you lost " + str(Winner))
        print(losermoney)
        money=losermoney
if money<0:
    print("Casino put a lien on your home!")      
