"""Demonstrate pass by value parameters with lists."""

from typing import List

def side_effect(x: List[int]) -> None:
    """Change the value of the parameter x."""
    x[0] = 10
    print("In side_effect, x = {}.".format(x))

def main() -> None:
    """Pass an actual parameter to side_effect."""
    x: List[int] = [5, 5, 5, 5]
    print("Before side_effect, x = {}.".format(x))
    side_effect(x)
    print("After side_effect, x = {}.".format(x))

def alternate_main() -> None:
    """Pass an actual parameter to side_effect."""
    x: List[int] = [5, 5, 5, 5]
    print("Before side_effect, x = {}.".format(x))
    y: List[int] = x.copy()
    side_effect(y)
    print("After side_effect, x = {}.".format(x))
    
main()


