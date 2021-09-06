
#import relevant modules
from tkinter import *
from tkinter.ttk import Combobox
import webbrowser

#create window object
window = Tk()
window.title("Renewable energy sources in MA")

# create a canvas to put objects on the screen
canvas = Canvas(window, width=1000, height=600, bg = '#ccffcc')
canvas.pack()

#intro message
intro = canvas.create_text(500, 200, text= 'We are going to learn about renewable energy sources in Massachusetts. \n' \
                           'Press the button below to get started!', fill='black', font = ('Helvetica', 20))

#display relevant information based on renewable resource selection
def resource_info(event):
    global resource
    global info
    
    selection = resource.current() #get the current selection from the dropdown list
    
    canvas.delete(info) #delete whatever info is displayed once a new selection is made
    
    if (selection == 0): #display info on solar energy if solar selected
        
        info = canvas.create_text(500,400,text="Solar powered generating units started operating in MA in 2008. \n"\
                                  "By 2019, solar powered energy account for 14% of net energy generation in MA. \n"\
                                  "If MA had solar panels on every rooftop, it could generate 47% of the state\'s electricity.", fill='black', font = ('Helvetica', 18))
        
    if (selection==1): #display info on wind energy if wind selected
                
        info = canvas.create_text(500,400,text="Wind power accounted for about 1% of MA\'s net energy generation in 2019. \n"\
                                  "MA\'s first offshore windfarm is under construction off of Martha's Vineyard. \n"\
                                  "MA plans to have 3200 megawatts of offshore windpower capacity by 2035.", fill='black', font = ('Helvetica', 18))
        
    if (selection==2): #display info on hydro energy if water selected
        
        info = canvas.create_text(500,400,text="In 2019, hydropower was the second-largest renewable source of electricity in MA. \n"\
                                  "MA has about 30 hydroelectric power plants. \n"\
                                  "MA\'s oldest operating hydroelectric plant is located near Holyoke.", fill='black', font = ('Helvetica', 18))

#opens a relevant website with information on renewable energy sources 
def web_info():
    webbrowser.open('https://www.eia.gov/renewable/')
    
#closes the app window
def exit_app():
    window.destroy()

#erases the intro message and intro button and populates window with dropdown list
def end_intro():
    
    global window
    #delete the intro message and button
    canvas.delete(intro) 
    intro_button.forget()
    
    #display prompt
    prompt = canvas.create_text(400, 150, text = "Please select the resource you would like to learn about:",
                                fill='black', font = ('Helvetica', 20))
    
    #display the source of the information being presented
    info_source = canvas.create_text(800, 550, text = "Source: eia.gov", fill='black', font = ('Helvetica',20))
    
    #place the dropdown list on the canvas
    resource.place(x=250, y=200)
    
    #create a widget that takes the user to eia.gov, to learn more about renewables
    more_info = Button(window, text="Learn more!", command = web_info)
    more_info.pack()    
         

#create a dropdown list which includes three renewable energy sources
resource=Combobox(window, font=('Helvetica',14),width=15, values=['Solar', 'Wind', 'Water'], state='readonly')

#bind selection from the dropdown list to the resource_info function
resource.bind("<<ComboboxSelected>>", resource_info)

#create a dummy info variable, which will be reassigned within the resource_info function
info = canvas.create_text(400,400,text=" ", fill='black', font = ('Helvetica', 20))
 
#create intro widget and place on window
intro_button = Button(window, text="Let's go!", command = end_intro)
intro_button.pack()

#create exit widget and place on window
exit_button = Button(window, text="Exit", command = exit_app)
exit_button.pack()

#last line of tkinter GUI
window.mainloop()
