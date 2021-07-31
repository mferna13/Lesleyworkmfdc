import turtle
lucid=turtle.Turtle()
lucid.speed("fastest")
turtle.bgcolor("slate grey")

# ring positions, colors, and shapes
NumShapes = 5
Xpos = [-100, -50, 0, 50, 100]
Ypos = [50, 0, 50, 0, 50]
Colors = ["blue", "gold", "black", "green", "red"]
Angles = [90,64,74,80,50]

# draw rings
for ShapeNo in range(NumShapes):
    lucid.color(Colors[ShapeNo])
    lucid.penup()
    lucid.goto(Xpos[ShapeNo], Ypos[ShapeNo])
    lucid.pendown()
    N=10
    for i in range(30):
        lucid.left(Angles[ShapeNo])
        lucid.forward(N)
        N=N+2

# draw text
lucid.penup()
lucid.goto(0,-40)
lucid.pendown()
lucid.color("black")
# Google for "python turtle write text"
lucid.write("Tokyo 2020!", font=("Arial", 20, "normal"))

# draw flag
lucid.penup()
# https://docs.python.org/3/library/turtle.html#turtle.setheading
lucid.setheading(0)
lucid.goto(0,-150)
lucid.pendown()
lucid.begin_fill()
lucid.color("white")
for i in range(4):
    lucid.forward(100)
    lucid.left(90)
lucid.end_fill()
lucid.goto(50,-130)
lucid.begin_fill()
lucid.color("red")
lucid.circle(30)
lucid.end_fill()
lucid.hideturtle()
turtle.exitonclick()
