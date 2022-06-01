"""Draw a personal flag."""

import turtle
        
def draw_green_stripe() -> None:
    """Draw the green stripe of the flag."""
    i: int
    # Move the turtle to the correct position.
    turtle.penup()
    turtle.setpos(-100,0)
    turtle.setheading(0)
    turtle.pendown()
    # Draw the rectangle.
    turtle.color("green")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
    turtle.end_fill()

draw_green_stripe()
    
