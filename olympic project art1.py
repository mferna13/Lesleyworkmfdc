import turtle
lucid=turtle.Turtle()
lucid.speed("fastest")
N=10
for i in range(30):
    lucid.left(2*360/3)
    lucid.forward(N)
    N=N+4
lucid.right(200)
lucid.color("gold")
lucid.begin_fill()
for i in range(10):
    lucid.left(99)
    lucid.forward(N)
    N=N+4
lucid.end_fill()   
lucid.hideturtle()
turtle.exitonclick()
