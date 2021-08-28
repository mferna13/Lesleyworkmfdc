import time
import random
from tkinter.constants import NO, S
# REMOVE """ HERE
#"""
print("Welcome to the Body Positivity Questionaire. Please Answer each question with yes or no.")
#List will help make the questions easier to input each time
Questions = [
    "I don't like certain parts of my body.",
    "I deny my bodies needs regularly.",
    "I don't think anyone could ever love me becuse of my body.",
    "Most of my inner comments to my body are negative or judgmental.",
    "My body image changes based on what others say about my apprence."]
Affirmation=[
    "Find one part of your body you love.",
    "Your body is worthy Of nurishment",
    "You are profoundly loved by those that see their own worth." ,
    "When we fear rejection or being unloved it can be easier to be our harshest critics. We feel better putting ourselves down because we assume everyone else wants to critize our bodies.",
    "Others put us down because they don't  feel good about themselves."]
        
Num_Questions = len(Questions)
# using functions and boolean operator
def AskForYesOrNo(question):
    Answer = input(question)

    while not (Answer=="Yes" or Answer=="yes" or Answer=="no" or Answer=="No"):
        print("Remember yes and no.")
        time.sleep=(3)
        Answer=input(question)

    return Answer

YesCount = 0
NoCount = 0

for i in range(Num_Questions):
    current_question = Questions[i]
    print("Here is a question #", i+1, "for you:")

    Response = AskForYesOrNo(current_question)
    # at this point Response is guaranteed to be one of "Yes", "yes", "No", "no"
    
    if Response == "Yes" or Response == "yes":
        YesCount = YesCount + 1
        current_affirmtion= Affirmation[i]
        print(current_affirmtion)
    else:
        NoCount = NoCount + 1

print("number of yes=", YesCount)
print("number of no=", NoCount)

if YesCount>NoCount:
    print("I'm Here to share a resource I find helpful. Lets remember every-body has somebody to care for. Please visit https://positivepsychology.com/positive-body-image/")
else:
    print(" Check in on your friends they might be struggling with body positivity!")
#"""
# REMOVE """ HERE

def TurtlePoem():
    import turtle
    poem=turtle.Turtle()
    poem.pendown()
    poem.goto(-300,0)
    poem.write("""What lies Beyond the surface of glass and Almagamate?
Is it found by looking in a mirror or grasping the parts you hate.
Your body is special a work of great art!
Please never from these words should you part.
Look or feel your body and mention one part
Find the one you love in your heart.""", font=("Arial", 16, "normal"))
    poem.penup()
    turtle.exitonclick()
def curve():
    import turtle
    heart=turtle.Turtle()
    heart.speed("fastest")
    for i in range(200):
        heart.right(1)
        heart.forward(1)
        heart.color("black", "red")  
        heart.begin_fill()
        heart.left(140)
        heart.forward(111.65)
        heart.left(120)
        heart.forward(111.65)
        heart.end_fill()
    turtle.exitonclick()
print("Here is a poem for you")
TurtlePoem()
curve()