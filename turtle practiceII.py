import turtle
lucid=turtle.Turtle()
for i in range (4):
    lucid.forward(100)
    lucid.left(90)
lucid.circle(10)

lucid.begin_fill()
lucid.color("red")
lucid.right(90)
lucid.circle(20)
lucid.end_fill()
lucid.begin_fill()
lucid.color("blue")
lucid.circle(40)
lucid.begin_fill()
lucid.color("green")
lucid.end_fill()
lucid.circle(60)
lucid.begin_fill()
lucid.color("green")
lucid.end_fill()
lucid.circle(80)
lucid.begin_fill()
lucid.color("gold")
lucid.end_fill()
lucid.circle(100)
lucid.begin_fill()
lucid.color("light blue")
lucid.end_fill()
lucid.circle(110)
lucid.begin_fill()
lucid.color("purple")
lucid.end_fill()
turtle.exitonclick()