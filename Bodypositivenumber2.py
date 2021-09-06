import time
import webbrowser
# Show the welcome message
print("Welcome to the Body Positivity Questionaire. Please Answer each Statement with yes or no.")
# Store questions and affirmations in lists (concurrently - question 1 corresponds to affirmation 1). This makes our code more flexible as one can add/modify questions without changing the rest of the code.
Statements = [
    "I don't like certain parts of my body. ",
    "I deny my body's needs regularly. ",
    "I don't think anyone could ever love me becuse of my body. ",
    "Most of my inner comments to my body are negative or judgmental. ",
    "My body image changes based on what others say about my appearance. "]
Affirmation=[
    "Find one part of your body you love. ",
    "Your body is worthy Of nourishment. ",
    "You are profoundly loved by those that see their own worth. " ,
    "When we fear rejection or being unloved it can be easier to be our harshest critics. We feel better putting ourselves down because we assume everyone else wants to critize our bodies.",
    "Others put us down because they don't  feel good about themselves. "]
        
NumStatements = len(Statements)
# I'm using functions, while loops, and Boolean operators here.
# This function will give a statement and prompt them again if they have mistyped their answer (e.g. said maybe instead of yes or no)
def AskForYesOrNo(Statements):
    Answer = input(Statements)

    while not (Answer=="Yes" or Answer=="yes" or Answer=="no" or Answer=="No"):
        print("Remember yes and no.")
        time.sleep(3)
        Answer=input(Statements)

    return Answer
# Maintain two counters for the number of yes or no answers encountered during the quiz.
YesCount = 0
NoCount = 0
# Here I'm using for loops to ask Statements one by one
for i in range(NumStatements):
    CurrentStatements = Statements[i]
    print("Here is the next statement", i+1, "for you:")

    Response = AskForYesOrNo(CurrentStatements)
    # at this point Response is guaranteed to be one of "Yes", "yes", "No", "no"
    
    if Response == "Yes" or Response == "yes":
# if the answer is yes, increment yes counter and print and affirmation
        YesCount = YesCount + 1
        CurrentAffirmation= Affirmation[i]
        print(CurrentAffirmation)
    else:
# otherwise the answer is "no" and increment "no" answer
        NoCount = NoCount + 1
# Display final statistics
print("number of yes= ", YesCount)
print("number of no= ", NoCount)

if YesCount>NoCount:
    # If yes is the majority statistic and shares a helpful resource
    print("I'm Here to share a resource I find helpful. Lets remember every-body has somebody to care for. Here is a link just for you!")
    #Thank you David for this line of Code
    Response = AskForYesOrNo("Would you like me to open this helpful resource?")
    if Response=="yes" or Response=="Yes":
        webbrowser.open_new_tab(" https://positivepsychology.com/positive-body-image/")
else:
    #The user gets a postive message and encouraged to check in with friends.
    print(" It's great you feel good about your body.Check in on your friends they might be struggling with body positivity!")

#using turtle  to give code more User Centered design by making poem easier to see

def TurtlePoem():
    import turtle
    HeartPoem=turtle.Turtle()
    HeartPoem.goto(-300,0)
    HeartPoem.pendown()
    HeartPoem.write("""What lies beyond the surface of glass and almagamate?
Is it found by looking in a mirror and grasping the parts you hate?
Your body is special a work of great art!
Please never from these words should you part.
So when you Look or feel your body please mention one part
Find the one you love in your heart.""", font=("Arial", 16, "normal"))
    HeartPoem.penup()
    HeartPoem.speed("fastest")
    HeartPoem.goto(0,-150)
    HeartPoem.pendown()
    for i in range(200):
        HeartPoem.right(1)
        HeartPoem.forward(1)
        HeartPoem.color("black", "red")  
        HeartPoem.begin_fill()
        HeartPoem.left(140)
        HeartPoem.forward(113)
        HeartPoem.left(120)
        HeartPoem.forward(112)
        HeartPoem.end_fill()
    turtle.exitonclick()
print("Here is a poem for you")
TurtlePoem()