import turtle
from math import sin, pi, e

decay1, decay2, decay3, decay4 = 0.02, 0.5, 0.2, 0.005  #The oscillation decay coefficients
phase1, phase2, phase3, phase4 = pi/6, pi/2, pi/6, pi/2  #Phase shifts
freq1, freq2, freq3, freq4 = 3, 2, 6, 4 #Frequencies

t = 0 #Initial time
dt = .001 #Time shift between each points of the graph

while t < 10: #Drawing graph finishes at time t = 60 seconds
    x = 100 * pow(e, -decay1 * t) * sin(t * freq1 + phase1) + 100 * pow(e, -decay2 * t) * sin(t * freq2 + phase2) #x axis position via formula
    y = 100 * pow(e, -decay3 * t) * sin(t * freq3 + phase3) + 100 * pow(e, -decay4 * t) * sin(t * freq4 + phase4) #y axis position
    turtle.setposition(x, y) #Setting the position of the pen
    t += dt #Next (new) value of time