"""Draw a stack of five boxes."""
import turtle

# Assumption: turtle starts at 0,0 with a heading of 0.
SIDE: int = 50
num_boxes: int = 0
y_coordinate: int = 0

# Draw five boxes.
while num_boxes < 5:
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.forward(SIDE)
    # Move turtle to next box start.
    turtle.penup()
    y_coordinate = y_coordinate + SIDE
    turtle.setpos(0, y_coordinate)
    turtle.setheading(0)
    turtle.pendown()
    num_boxes = num_boxes + 1
