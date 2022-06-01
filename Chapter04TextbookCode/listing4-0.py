"""Draw a stack of two boxes."""
import turtle

SIDE: int = 50
# Assumption: turtle starts at 0,0 with a heading of 0.

# Draw first box.
turtle.forward(SIDE)
turtle.left(90)
turtle.forward(SIDE)
turtle.left(90)
turtle.forward(SIDE)
turtle.left(90)
turtle.forward(SIDE)

# Move turtle to start of next box.
turtle.penup()
turtle.setpos(0, 50)
turtle.setheading(0)
turtle.pendown()

# Draw second box.
turtle.forward(SIDE)
turtle.left(90)
turtle.forward(SIDE)
turtle.left(90)
turtle.forward(SIDE)
turtle.left(90)
turtle.forward(SIDE)

# Move turtle to start of next box.
turtle.penup()
turtle.setpos(0,100)
turtle.setheading(0)
turtle.pendown()
