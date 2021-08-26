from tkinter import *
import random
# make window
window = Tk()
window.title('I Am?')

canvas = Canvas(window, width=400, height=400)
canvas.pack()
title = canvas.create_text(200, 200, text= 'I Am...', fill='black', font = ('Helvetica', 30))
directions = canvas.create_text(200, 300, text= 'How are you feeling?', fill='black', font = ('Helvetica', 20))
background_image=PhotoImage(file="mirror.gif")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.mainloop() # last line is the GUI main event loop