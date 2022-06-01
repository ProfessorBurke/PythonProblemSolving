"""A simple adventure game."""
import random

def print_item() -> None:
    """Randomly generate an item."""
    item_number: int = random.randint(1,3)
    if item_number == 1:
        print("There is a laptop here.")
    elif item_number == 2:
        print("There is a cold cup of coffee here.")
    else:
        print("There is nothing else here.")
        
def print_classroom() -> None:
    """Describe a classroom."""
    print("You are in a classroom with a whiteboard " +\
          "and computers.  Let's start programming!")
    print_item()

def print_great_hall() -> None:
    """Describe the great hall."""
    print("You are in giant space full of tables " +\
          "and friendly-looking students.  Let's study!")
    print_item()
    
def main() -> None:
    """Describe the building."""
    print_great_hall()
    print("You decide to visit another area.")
    print_classroom()

main()
    
