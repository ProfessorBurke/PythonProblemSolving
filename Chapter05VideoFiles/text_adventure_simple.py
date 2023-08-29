"""
    A simple text adventure.
    
"""

def print_field_description():
    """Describe the field, including the directions that can be moved."""
    print("You are standing in a field of long grass dotted with wildflowers.")
    print("To the (N)orth, you see what looks like an abandoned settlement.")
    print("To the (E)ast, you see a forest.")
    print("To the (S)outh is a fast-flowing river.  It looks dangerous.")
    print("To the (W)est is an unscalable cliff face.")

def visit_field(direction: str) -> str:
    """Return the player's new location based on direction they want to move."""
    # Annotate and initialize local variables.
    #location: str = "field"

    # Determine the new location based on direction.
    if direction == "E":
        location = "field"
    elif direction == "N":
        location = "field"
    elif direction == "S":
        location = "field"
        print("You've fallen in the river and have been swept out to sea.")
    elif direction == "W":
        print("There is an impassable cliff in that direction.")
    return location

# Annotate variables.
choice: str = "X"
location: str = "field"

# Print a welcome message.
print("Welcome to Simple Adventure!")
print("You may type N, S, E, or W to move in a direction, or Q to quit.")

# Obtain the user's action and handle it.  The action will
# be a direction to move or to quit.
while choice != "Q":

    # Describe the current location
    if location == "field":
        print_field_description()
        
    # Obtain the user's command and update the location accordingly.
    choice = input("What is your command? (N, S, E, W, Q): ")
    if choice != "Q":
        location = visit_field(choice)

