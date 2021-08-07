#introduction to main character and place
import time
name=input("What is thy name oh valliant adventurer? I'm Eulalia")
print("welcome to Traconis, "+name+".")
print("A creature of the darkness has kidnapped the princess! only you can save her! ")
#introduction to task using elseif
flower= input("Did you bring  Lumen flowers?")
time.sleep(3)
if flower =="yes" or flower == "I do"  or flower=="Yes":
    time.sleep(3)
    LumenHandoff="Let me add it to a potion I was cooking up!"
    amount= input("How many did you bring?")
elif flower=="no" or flower=="No" or flower=="I don't" or flower==" I do not":
    LumenHandoff="Check your sachel Lumen flowers come to those in dire need"+name+"!"
    amount="0"
amount=int(amount)
print(LumenHandoff)
print("Time to make a potion.")
time.sleep(3)
if amount % 2 == 0:
    # even number of flowers
    print("Excellent, Lumen flowers are the most poetent in even amounts")
    time.sleep(3)
else:
    # odd number of flowers
    print("Too much Lumen is dangerous! Do you want to kill us?! Lumen is not stable in odd amounts! Bury one quick!")
    time.sleep(3)
    answer=input("Did you bury it?")

    while not (answer== "yes" or answer=="Yes" or answer=="I did"):
        print("don't mess around!")
        answer=input("Did you bury it yet?")
        if answer== "yes" or answer=="Yes" or answer=="I did":
            print("Wow that was close! I don't think anyone has lived to tell about odd Lumens "+name+"!")
            time.sleep(6)
print("few hours later...")
print(" Egad, it is finished!")
print("Time to leave! Hurry, hurry!!")
print(" I may have an acient book with directions.")
time.sleep(3)
print("Walk to main doors then 3000 steps to Gate. Go left at the kingdom gates walk 50KM, and at the fork in the road go left. When you get to red trees please go right, but do not eat fruit from tree. Then you will get to a large ash tree with a door. Answer the riddle to enter")
ready=input("Are you ready? Yes or no!")
if ready== "yes" or ready=="Yes":
    print("Goodbye"+name+" and good luck!")
else:
    if ready== "no" or ready=="No":
        #first leg of journey
        print("No one feels ready for adventures, but adventures choose us. Off you go! No is not an option.Bye!")

# PERFECT STARTS
stepcount=input(" I'm at the main doors how many steps should I walk?")
stepcount = int(stepcount)
if stepcount == 3000:
    print("I knew I remembered")
while not (stepcount==3000):
    if stepcount>3000:
        print("I think that's too high")
    else:
        if stepcount<3000:
           print("That seems too low.")
    stepcount= input("I need to make another choice! What should I choose?")  
    stepcount=int(stepcount)
# PERFECT ENDS
#fork in the road
KM=50
User_KM=input("How many Kilometers should I go?")
User_KM=int(User_KM)
if User_KM==50:
    print("My mind is an elephant")
while not (User_KM == 50):
#greater than 50
    if User_KM>50:
        print("Too high, I think.")
    else:
        print("Hmm, that seems too low!")
    #ask user for new input
    User_KM=input("Let me try another! How many kilometers should I go?")
    User_KM=int(User_KM)
FirstLeft=input("There is a fork,go left or right?")
while not(FirstLeft=="left"):
    print("Definitely on the right track, but not the one I want!")
    print("umm I'm lost! Better go back!")
    FirstLeft=input("Right or Left?")
print("By jove we made it to trees!")
    #tree sequence life can be lost
lives=3
Fruit="no"
Eating=input("Should I eat fruit? What did Eulalia say? Yes or no?")
while Eating=="yes" or Eating=="Yes":
    lives=lives-1
    if lives < 1:
        print("Whoops, no more lives left. We will reviwe you after one minute.")
        time.sleep(60)
        lives = 3
    print("I'd better save up strength for the final test! I lost a life"+ str(lives))
    print("I'm feeling terrible I'm not eating anymore")
    Eating= input("should I eat? Yes or no?")
if Eating=="no" or Eating=="No":
    print("The red trees look suspect, good thinking.")
    print("Glad I'm making a smart choice!")
#walking to tree
Walk=input("should we keep going to the tree?")
if Walk=="yes" or Walk=="Yes":
    print("on my way!")

elif Walk=="no" or Walk=="No":
    print("I'm taking a quick nap!")
    time.sleep(5)
    print("I'm rested enough lets go!")
#riddle time
print("This journey is long and lonely it is taking a long time to see the door.....")
time.sleep(6)
print("I see large ash tree and there is a door!")
print("Who goes by the door of darkness? speak thy name!")
input("what is thy name?")
time.sleep(3)
print(" It is riddle time!!!No one has ever solved")
print("I never was, am always to be. No one ever saw me nor ever will. Yet I am the confidence of all to live and breathe on this terrestrial ball.")
riddleAnswer=input("Speak truth and enter!! What am I?")
while not (riddleAnswer== "tomorrow" or riddleAnswer == 'Tomorrow'):
    riddleAnswer = input('That is incorrect try again!')
    if riddleAnswer=="Tomorrow" or riddleAnswer=="tomorrow":
        print("door opens")
        time.sleep(3)
        print("Door closes!")
        print("help me! Oh help me!")
        print(" I can't see anything I'm trying!")
lumen=input("What should I use to see? I have a mushroom, water, scroll, candle and the potion?")
while not (lumen=="Candle" or lumen=="candle"):
    if lumen=="mushroom" or lumen=="water":
       lumen=input("Hmm I should save food and drink, lets try again.")
    else:
        print("I can't see")
        lumen=input("Try again!")

print("Woah I can see! Where are you princess.")
    
print("I'm not sure I think go left and then right?, but the creature is coming back soon hurry!")
direction=input(" should I go left then right?")
while not (direction=="yes" or direction=="Yes"):
    if direction=="no" or direction=="No":
        print("Go back! I don't hear her anymore")
    else:
        print("I don't understand!")
        direction=input("Try going Left Right? Yes or no?")
print("I found you princess how are doing")
print("Dying of thirst and hunger I've only had foul water to drink!")
Food_princess=input("Should I give her food? Yes or no?")
if Food_princess=="Yes" or Food_princess=="yes":
    print("yum yum yum! slurp, slurp")
else:
    print("I'm being selfish! Have some food!!")
    time.sleep(3)
print("ohh no the creature is coming.")
magic=input("How did you get passed my riddle? Do you think you can stop me? Yes or no?")
while not (magic=="yes" or magic=="Yes"):
    if magic=="no" or magic == "No":
        magic=print("correct only a fool would come here!")
    else:
        magic=print("quit mocking me!")
magic=input("so you have any magic fool?")
light=input("open Lumen? yes or no")
if light=="no" or light == "No":
    print("you have died!")
elif light=="yes" or light=="Yes":
    print("You have defeated the creature! brave " + name)
