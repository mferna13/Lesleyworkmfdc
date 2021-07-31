import turtle
lucid=turtle.Turtle()
lucid.begin_fill
lucid.color("red")
for i in range(4):
   lucid.forward(100)
   lucid.left(90)
   lucid.circle(20)
lucid.end_fill()
lucid.goto(1,0)
lucid.goto(5,0)
lucid.goto(5,4)
lucid.end_fill
lucid.forward(100)
lucid.left(90)
lucid.circle(40)
lucid.circle(60)
lucid.begin_fill
lucid.color("green")
lucid.end_fill