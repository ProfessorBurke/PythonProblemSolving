"""The turtle travels around the globe."""
import turtle, math

def main():
    radius: int
    num_degrees: int
    num_radians: float
    x: float
    y: float
    # Set the turtle's shape and color.
    turtle.shape("turtle")
    turtle.color("green")
    # Set the circle size.
    radius = 100
    # Loop through 360 degrees.
    for num_degrees in range(0, 360, 20):
        # Calculate the coordinates.
        num_radians = math.radians(num_degrees)
        x = radius * math.cos(num_radians)
        y = radius * math.sin(num_radians)
        # Stamp the turtle.
        turtle.penup()
        turtle.setheading(num_degrees + 90)
        turtle.setpos(x,y)
        turtle.pendown()
        turtle.stamp()

main()
        
