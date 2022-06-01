"""Draw a personal flag."""

import turtle

def draw_rectangle() -> None:
    """Draw a rectangle of length 200 and height 25."""
    i: int
    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
        
def draw_green_stripe() -> None:
    """Draw the green stripe of the flag."""
    # Move the turtle to the correct position.
    turtle.penup()
    turtle.setpos(-100,0)
    turtle.setheading(0)
    turtle.pendown()
    # Draw the rectangle.
    turtle.color("green")
    turtle.begin_fill()
    draw_rectangle()
    turtle.end_fill()

def draw_gold_stripe() -> None:
    """Draw the gold stripe of the flag."""
    # Move the turtle to the correct position.
    turtle.penup()
    turtle.setpos(-100,25)
    turtle.setheading(0)
    turtle.pendown()
    # Draw the rectangle.
    turtle.color("gold")
    turtle.begin_fill()
    draw_rectangle()
    turtle.end_fill()
    
def main() -> None:
    """Draw a personal flag."""
    draw_green_stripe()
    draw_gold_stripe()

main()
    
