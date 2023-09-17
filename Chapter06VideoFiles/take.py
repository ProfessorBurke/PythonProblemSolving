"""
    Allow the player to move items from the location to
    their inventory.
"""

# Annotate variables.
location_items: list[str]
inventory: list[str]
item: str

# Initialize the lists.
location_items = ["key", "potion", "Python book"]
inventory = []

# Allow the player to take an item.
print("You see")
print(location_items)
item = input("What would you like to take? ")
if item in location_items:
    inventory.append(item)
    location_items.remove(item)

# Show the player their inventory and location items.
print("You have")
print(inventory)
print("You see")
print(location_items)

