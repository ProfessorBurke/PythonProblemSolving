"""Respond to mouse events by drawing a dot."""

import turtle

def handle_click(x: float, y: float) -> None:
    """Make a dot at (x, y)."""
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.stamp()

def main() -> None:
    """Process click events by drawing dots."""
    turtle.tracer(0)
    turtle.shape("circle")
    turtle.Screen().onclick(handle_click)
    turtle.Screen().mainloop()

main()
