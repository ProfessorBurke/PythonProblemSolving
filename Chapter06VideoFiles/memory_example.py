"""
    A program to illustrate how memory management works
    with lists in Python.
"""

# Annotate some lists.
dice: list[int]
also_dice: list[int]
copy_dice: list[int]

# Give the lists values.
dice = [6, 5, 1, 2, 5]
also_dice = dice
copy_dice = dice.copy()
