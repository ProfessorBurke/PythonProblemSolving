"""Demonstrate pass by value parameters."""

def no_side_effect(x: int) -> None:
    """Change the value of the parameter x."""
    x = 10
    print("In no_side_effect, x = {}.".format(x))

def main() -> None:
    """Pass an actual parameter to no_side_effect."""
    x: int = 5
    print("Before no_side_effect, x = {}.".format(x))
    no_side_effect(x)
    print("After no_side_effect, x = {}.".format(x))
    
main()
