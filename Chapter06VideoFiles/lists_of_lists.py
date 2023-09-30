"""
    A program to illustrate how memory management works
    with lists of lists in Python.
"""

# Annotate some lists.
dice_bags: list[list[int]]
copy_dice_bags: list[list[int]]
i: int

# Give the lists some values.
dice_bags = [[6, 5, 1, 2, 5], [1, 1, 3, 4, 6]]
copy_dice_bags = dice_bags.copy()

# A change to copy_dice_bags that does not change dice_bags.
copy_dice_bags[0] = [1, 1, 1, 1, 1]

# A change to copy_dice_bags that changes dice_bags.
copy_dice_bags[1][2] = 5

# Make a deep copy of dice_bags.
copy_dice_bags = dice_bags.copy()
for i in range(len(copy_dice_bags)):
    copy_dice_bags[i] = copy_dice_bags[i].copy()
    
