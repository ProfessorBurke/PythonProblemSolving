"""
   Modify an inventory with functions.
"""

def create_inventory() -> list[str]:
    """For now, hard-code and return an inventory."""
    new_inventory: list[str]
    new_inventory = ["talisman", "oar", "lime"]
    return new_inventory

def drop(item: str, from_inventory: list[str]) -> bool:
    """Drop item from from_inventory if it's in the inventory
       and return True; otherwise return False."""
    success: bool = True
    # Remove the item from inventory if it's there.
    if item in from_inventory:
        from_inventory.remove(item)
    # If it's not there, set the flag to False.
    else:
        success = False
    # Return the success code.
    return success

def main() -> None:
    """Create an inventory and allow the user to drop one item."""
    # Annotate inventory, item, and dropped, and create the inventory.
    inventory: list[str]
    item: str
    dropped: bool
    inventory = create_inventory()

    # Get the item the user wants to drop and drop it.
    print(inventory)
    item = input("What would you like to drop? ")
    dropped = drop(item, inventory)

    # Print a message to the user.
    if dropped:
        print("You've successfully dropped {}.".format(item))
    else:
        print("You don't have a {}.".format(item))
    print(inventory)

main()
    
    
