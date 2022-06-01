"""Respond to mouse and key events by drawing a dot."""

import turtle

def handle_click(x: float, y: float) -> None:
    """Make a dot at (x, y)."""
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.stamp()

def increase() -> None:
    """Make the circle larger."""
    width: int
    length: int
    outline: int
    width, length, outline = turtle.shapesize()
    width += 1
    length += 1
    turtle.shapesize(width, length, outline)

def main() -> None:
    """Process click events by drawing dots."""
    turtle.tracer(0)
    turtle.shape("circle")
    turtle.Screen().onclick(handle_click)
    turtle.Screen().onkey(increase, "Up")
    turtle.Screen().listen()
    turtle.Screen().mainloop()

main()
