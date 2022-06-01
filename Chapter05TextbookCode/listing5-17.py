"""Draw a turtle graphics image from
   instructions in a file."""

import turtle, os, typing

def set_up_turtle(x: float, y: float) -> None:
    """Move the turtle into position at heading 0."""
    turtle.penup()
    turtle.setpos(x, y)
    turtle.setheading(0)
    turtle.pendown()

def read_and_draw_rect(file: typing.TextIO) -> None:
    """Read square information and draw."""
    i: int
    x: int = float(file.readline())
    y: int = float(file.readline())
    length: int = float(file.readline())
    width: int = float(file.readline())
    set_up_turtle(x, y)
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

def read_and_draw_circle(file: typing.TextIO) -> None:
    """Read circle information and draw."""
    x: int = float(file.readline())
    y: int = float(file.readline())
    radius: int = float(file.readline())
    set_up_turtle(x, y)
    turtle.circle(radius)

def get_file() -> typing.TextIO:
    """Return a valid file obtained from the user."""
    file: typing.TextIO = open("drawing.txt")
    return file

def main() -> None:
    """Draw the image described in a file using turtle graphics."""
    file: typing.TextIO = get_file()
    # Read from the file as long as it's a valid shape type.
    drawing_type: str = file.readline().strip()
    while drawing_type == "rectangle" or drawing_type == "circle":
        # Draw the correct shape.
        if drawing_type == "rectangle":
            read_and_draw_rect(file)
        elif drawing_type == "circle":
            read_and_draw_circle(file)
        drawing_type = file.readline().strip()

main()
    
