import turtle

def draw_branch(x: float, y: float, heading: int, length: float) -> None:
    """Recursive function to draw one branch of a fractal tree."""
    # Set up the drawing environment.
    turtle.penup()
    turtle.setpos(x, y)
    turtle.setheading(heading)
    turtle.pendown()
    # Recursive case: draw the stem and two smaller branches.
    if length > 5:
        # Draw the stem.
        turtle.forward(length)
        # Draw branches 30 degrees to each side and reduce length.
        x = turtle.xcor()
        y = turtle.ycor()
        draw_branch(x, y, heading-30, length*.7)
        draw_branch(x, y, heading+30, length*.7)
    # Base case:  draw a leaf.
    else:
        turtle.right(90)
        turtle.circle(length // 4)

def main() -> None:
    """Draw a fractal tree with a starting length of 100."""
    turtle.speed(0)
    draw_branch(0,-200,90,100)

main()
