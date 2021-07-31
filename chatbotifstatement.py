name=input("Hello I am Emotibot, What is your name? ")
Mood=input("How are you feeling? ")
if Mood=="happy":
    input("why are you happy?")
else:
    if Mood=="sad":
        print("May I tell you a joke? "+(name))
        print("Why did the computer catch a virus?... Because it had an open window. ")
    else:
        print ("Wow Humans have diverse ways of feeling, " +name+"!")
        print ("Maybe you could show me how to feel " +Mood+"?")
print("Goodbye")