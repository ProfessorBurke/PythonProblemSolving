"""
    Allow the player to display and edit an inventory.
"""

# Annotate and initialize variables.
inventory: list[str] = ["key", "Awful Awful", "Python book"]
index: int
item: str

# Show the player the inventory.
print("You have: ")
print(inventory)

# Find out what the player wants to replace.
print("You have {} items.".format(len(inventory)))
index = int(input("What is the nubmer of the item you want to replace? "))
index -= 1
item = input("What do you want to replace it with? ")

# Replace the item.
if index >= 0 and index < len(inventory):
    inventory[index] = item

# Show the player the inventory.
print("You have: ")
print(inventory)
