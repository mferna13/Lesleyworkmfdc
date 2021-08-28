from tkinter import *
import random
import time
# make window
window = Tk()
window.title('I Am?')

canvas = Canvas(window, width=400, height=400, bg="white")
canvas.pack()

background_image = PhotoImage(file="mirror.gif")
background = canvas.create_image(200, 200, image=background_image)

title = canvas.create_text(200, 200, text="I Am...", fill="blue", font=("Helvetica", 30))
directions = canvas.create_text(200, 300, text= "How are you feeling?", fill="green", font=("Helvetica", 15))

def clear_intro():
    canvas.delete(title)
    canvas.delete(directions)

def show_question1():
    global QuestionOne
    QuestionOne=canvas.create_text(200, 200, text="I Am Beautiful? Yes/No", fill="blue", font=("Helvetica", 15))

def clear_question1():
    global QuestionOne
    canvas.delete(QuestionOne)
window.after(2000, clear_intro)
window.after(2000, show_question1)
window.after(4000, clear_question1)
move_direction = 0 # track which direction player is moving
# Function handles when user first presses arrow keys
def check_input(event):
    global Answer
    key = event.keysym
    if key == "Right":
       Answer = "yes"
    elif key == "Left":
        Answer = "Left"
 
        def end_input(event):
        global Answer
    move_direction = "None"

# Function handles when user stop pressing arrow keys
def end_input(event):
    global move_direction
    move_direction = "None"

def show_QuestionTwo():
    global QuestionTwo
    QuestionTwo=canvas.create_text(200, 200, text="I Love my Body? Yes/No", fill="blue", font=("Helvetica", 15))
def clear_QuestionTwo():
    global QuestionTwo
    canvas.delete(QuestionTwo)

window.after(4000, show_QuestionTwo)
window.after(6000, clear_QuestionTwo)
window.mainloop() # last line is the GUI main event loop