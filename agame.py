from tkinter import *
import random

window = Tk()
window.title('GET RICH FAST!')

# create a canvas to put objects on the screen
canvas = Canvas(window, width=1000, height=600, bg = 'white')
canvas.pack()
# set up welcome screen with title and directions
title = canvas.create_text(500, 500, text= 'GET RICH FAST!', \
fill='black', font = ('Helvetica', 30))
directions = canvas.create_text(500, 300, text= 'Collect as much treasure as you can in 15 seconds!'\
                                , fill='black', font = ('Helvetica', 20))
# set up score display using label widget
score = 0
score_display = Label(window, text="Score :" + str(score))
score_display.pack()

# create an image object using the gif file
player_image = PhotoImage(file="corona-virus.gif")

# use image object to create a character at position 100, 300
mychar = canvas.create_image(100, 300, image = player_image)

# variables and lists needed for managing coins/treasure
treasure_list=[]
treasure_color='yellow'

# make coins at random places
def make_coins(): 
     # pick a random x position
     xposition = random.randint(100, 900)
     # pick a random y position
     yposition = random.randint(100, 500)
     # create a yellow coin at a random position
     treasure = canvas.create_oval(xposition, yposition, xposition+30, yposition+30, fill = treasure_color)
     # add coin to list
     treasure_list.append(treasure)
     # schedule this function to make coins again every 0.8 seconds
     window.after(800,make_coins)

# update score
def update_score():
     # global variable score
     global score
     score = score + 10
     # display updated score
     score_display.config(text="Score :" + str(score))
 
# display final score at the end of the game 
def end_game_score():
    #global variable score
    global score
    final_score = canvas.create_text(500, 300, text= 'Game over! Your final score is: ' \
                                     + str(score), fill='red', font = ('Helvetica', 20))
    # call the end_game_over function 4 second after displaying the final score
    window.after(4000, end_game_over)
    return

# close the game window 
def end_game_over():
    window.destroy()
    
# get rid of the instructions on the screen at the beginning of the game
def end_title():
 canvas.delete(title) # remove title
 canvas.delete(directions) # remove directions

# check distance between 2 objects - return true if they 'touch'
def collision(item1, item2, distance):
    
    #difference in x coordinates of two objects
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0]) 
    #difference in y coordinates of two objects
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1]) 
    #check whether the character "collides" with the coins
    overlap = xdistance < distance and ydistance < distance
    return overlap #this is a Boolean variable

# check if character hits coins
def check_hits():
 
     # for any coin, do the following       
     for treasure in treasure_list:
         #delete the coin if the character "collides" with it
         if collision(mychar, treasure, 30):
             canvas.delete(treasure) # remove from canvas
             # find where in list and remove and update score
             treasure_list.remove(treasure)
             update_score()
     # schedule check_hits again after 0.1 seconds
     window.after(100, check_hits)

move_direction = 0 # track which direction player is moving

# Function handles when user first presses arrow keys
def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"
    elif key=="Up":
        move_direction = "Up"
    elif key=="Down":
        move_direction = "Down"
        
# Function handles when user stop pressing arrow keys
def end_input(event):
    global move_direction
    move_direction = "None" #do not move the character when user is not pressing arrows
    
# move the character accordingly based on user input
def move_character():
 if move_direction == "Right" and canvas.coords(mychar)[0] < 1000:
     canvas.move(mychar, 10,0)
 if move_direction == "Left" and canvas.coords(mychar)[0] > 0 :
     canvas.move(mychar, -10,0)
 if move_direction == "Up" and canvas.coords(mychar)[0] > 0 :
     canvas.move(mychar, 0,-10)
 if move_direction == "Down" and canvas.coords(mychar)[0] < 1000 :
     canvas.move(mychar, 0,10)
 window.after(16, move_character) # Move character at 16 frames per second

# bind the keys to the character
canvas.bind_all('<KeyPress>', check_input) 
canvas.bind_all('<KeyRelease>', end_input)

# Start game loop by scheduling all the functions
window.after(3000, end_title) # destroy title and instructions after 3 seconds
window.after(4000,make_coins) #start making coins after 4 seconds
window.after(1000, check_hits) # check if character hit a coin
window.after(1000, move_character) # handle keyboard controls
window.after(18000, end_game_score) #display final score after 18 seconds (15 effective seconds)
#the end_game_score functions itself will then call the game over function to close the window

window.mainloop() # last line is the GUI main event loop