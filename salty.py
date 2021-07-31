import turtle

lucid=turtle.Turtle()

lucid.speed("fastest")

num_circles = 40
for i in range(num_circles):
    lucid.color("gold")
    lucid.begin_fill()
    lucid.circle(20)
    # c = 0 0.025 0.05 ... 1
    c = (i/num_circles) * turtle.colormode()
    r = 0
    g = 0
    b = c
    lucid.color((r, g, b))
    lucid.end_fill()
    lucid.penup()
    lucid.left(20)
    lucid.forward(30+i**0.5)
    lucid.pendown()

lucid.hideturtle()

#for i in range (4):
#    lucid.forward(100)
#    lucid.left(90)
#lucid.circle(10)

#lucid.begin_fill()
#lucid.color("red")
#lucid.right(90)
#lucid.circle(20)
#lucid.end_fill()

turtle.exitonclick()
