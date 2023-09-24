"""
    Demonstrate some basic looping algorithms for lists
    using our inventory example.
"""
import random

# Annotate variables.
inventory: list[str]
i: int
item: str
dice: list[int]
count: int
winning_number: int
die: int
highest: int

# Roll the dice.
dice = []
for i in range(5):
    dice.append(random.randint(1, 6))

print(dice)

# Play the tavern dice game.
winning_number = random.randint(1, 6)
count = 0
for die in dice:
    if die == winning_number:
        count += 1

print("Winning number", winning_number)
print("Count", count)

# Find the highest die in the roll.
highest = 0
for die in dice:
    if die > highest:
        highest = die

print("Highest", highest)

### Initialize the inventory.
##inventory = ["key", "potion", "Python book", "apple", "coin"]
##
### Show the player the inventory.
##for i in range(len(inventory)):
##    print(inventory[i])
##
### Replace every inventory element with "toy " + element.
##for i in range(len(inventory)):
##    inventory[i] = "toy " + inventory[i]
##
### Show the player the inventory.
##print()
##for item in inventory:
##    print(item)
