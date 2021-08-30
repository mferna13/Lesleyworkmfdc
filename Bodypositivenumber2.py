import time
# Show the welcome message
print("Welcome to the Body Positivity Questionaire. Please Answer each question with yes or no.")
# Store questions and affirmations in lists (concurrently - question 1 corresponds to affirmation 1). This makes our code more flexible as one can add/modify questions without changing the rest of the code.
Questions = [
    "I don't like certain parts of my body.",
    "I deny my bodies needs regularly.",
    "I don't think anyone could ever love me becuse of my body.",
    "Most of my inner comments to my body are negative or judgmental.",
    "My body image changes based on what others say about my apprence."]
Affirmation=[
    "Find one part of your body you love.",
    "Your body is worthy Of nurishment.",
    "You are profoundly loved by those that see their own worth." ,
    "When we fear rejection or being unloved it can be easier to be our harshest critics. We feel better putting ourselves down because we assume everyone else wants to critize our bodies.",
    "Others put us down because they don't  feel good about themselves."]
        
Num_Questions = len(Questions)
# I'm using functions, while loops, and boolean operators here.
# This function will ask user a question and prompt them again if they have mistyped their answer (e.g. said maybe instead of yes or no)
def AskForYesOrNo(question):
    Answer = input(question)

    while not (Answer=="Yes" or Answer=="yes" or Answer=="no" or Answer=="No"):
        print("Remember yes and no.")
        time.sleep(3)
        Answer=input(question)

    return Answer
# Maintain two counters for the number of yes or no answers encountered during the quiz.
YesCount = 0
NoCount = 0
# Here I'm using for loops to ask questions one by one
for i in range(Num_Questions):
    current_question = Questions[i]
    print("Here is a question #", i+1, "for you:")

    Response = AskForYesOrNo(current_question)
    # at this point Response is guaranteed to be one of "Yes", "yes", "No", "no"
    
    if Response == "Yes" or Response == "yes":
# if the answer is yes, increment yes counter and print and affirmation
        YesCount = YesCount + 1
        current_affirmtion= Affirmation[i]
        print(current_affirmtion)
    else:
# otherwise the answer is "no" and increment "no" answer
        NoCount = NoCount + 1
# Display final statistics
print("number of yes=", YesCount)
print("number of no=", NoCount)

if YesCount>NoCount:
    # If yes is the majority statistic and shares a helpful resource
    print("I'm Here to share a resource I find helpful. Lets remember every-body has somebody to care for. Please visit https://positivepsychology.com/positive-body-image/")
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
Is it found by looking in a mirror and grasping the parts you hate.
Your body is special a work of great art!
Please never from these words should you part.
so when you Look or feel your body please mention one part
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