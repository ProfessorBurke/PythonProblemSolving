"""
    An inventory piece of an adventure game.
"""
from typing import List

def show_items(items: List[str], heading: str) -> None:
    """Display the items."""
    item: str
    print(heading)
    if len(items) > 0:
        for item in items:
            print("\t{}".format(item))
    else:
        print("\tNothing.")

def pick_up(inv: List[str], items: List[str]) -> None:
    """Allow the user to pick up one of the available
       items.  Lists passed might be modified."""
    choice: str
    show_items(items, "You see: ")
    choice = input("What do you want to pick up? ")
    if choice in items:
        items.remove(choice)
        inv.append(choice)
    else:
        print("I don't see that here.")
    
def main() -> None:
    inventory: List[str] = []
    items: List[str] = ["a well-read Python textbook",
                        "gum",
                        "two nickels",
                        "one ring to rule them all"]
    # Show the user their inventory.
    show_items(inventory, "You have: ")
    # Allow the user to pick up an item.
    pick_up(inventory, items)
    # Show the user their inventory.
    show_items(inventory, "You have: ")

main()
    
    
    
