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
        
def draw_stripe(color: str, y: int) -> None:
    """Draw a flag stripe in color at (-100, y)"""
    # Move the turtle to the correct position.
    turtle.penup()
    turtle.setpos(-100, y)
    turtle.setheading(0)
    turtle.pendown()
    # Draw the rectangle.
    turtle.color(color)
    turtle.begin_fill()
    draw_rectangle()
    turtle.end_fill()
    
def main() -> None:
    """Draw a personal flag."""
    draw_stripe("green", 0)
    draw_stripe("gold", 25)

main()
