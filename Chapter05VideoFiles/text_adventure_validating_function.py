"""
    A simple text adventure.
    
"""

def print_field_description() -> None:
    """Describe the field, including the directions that can be moved."""
    print("You are standing in a field of long grass dotted with wildflowers.")
    print("To the (N)orth, you see what looks like an abandoned settlement.")
    print("To the (E)ast, you see a forest.")
    print("To the (S)outh is a fast-flowing river.  It looks dangerous.")
    print("To the (W)est is an unscalable cliff face.")

def print_wood_description() -> None:
    """Describe the woods, including the directions that can be moved."""
    print("You are in a quiet, dense wood with no discernible path.")
    print("To the (N)orth, you see what looks like an abandoned settlement.")
    print("To the (E)ast, you see more forest.")
    print("To the (S)outh is a fast-flowing river.  It looks dangerous.")
    print("To the (W)est is a field.")

def print_settlement_description() -> None:
    """Describe the settlement, including the directions that can be moved."""
    print("This appears to be an abandoned settlement.  You are standing in what appears to have been the town square.")
    print("To the (N)orth, you see more of the settlement.")
    print("To the (E)ast, you see a forest.")
    print("To the (S)outh is a field.")
    print("To the (W)est is an unscalable cliff face.")

def visit_field(direction: str) -> str:
    """Return the player's new location based on direction they want to move."""
    # Annotate and initialize local variables.
    location: str = "field"

    # Determine the new location based on direction.
    if direction == "E":
        location = "wood"
    elif direction == "N":
        location = "settlement"
    elif direction == "S":
        location = "gameover"
        print("You've fallen in the river and have been swept out to sea.")
    elif direction == "W":
        print("There is an impassable cliff in that direction.")
    return location

def visit_wood(direction: str) -> str:
    """Return the player's new location based on the direction they want to move."""
    # Annotate and initialize local variables.
    location: str = "wood"

    # Determine the new location based on direction.
    if direction == "E":
        location = "wood"
    elif direction == "N":
        location = "settlement"
    elif direction == "W":
        location = "field"
    elif direction == "S":
        location = "gameover"
        print("You've fallen in the river and have been swept out to sea.")
    return location

def visit_settlement(direction: str) -> str:
    """Return the player's new location based on the direction they want to move."""
    # Annotate and initialize local variables.
    location: str = "settlement"

    # Determine the new location based on direction.
    if direction == "E":
        location = "wood"
    elif direction == "N":
        location == "settlement"
    elif direction == "W":
        print("There is an impassable cliff in that direction.")
    elif direction == "S":
        location = "field"
    return location

def get_new_location(current_location: str, direction: str) -> str:
    """Return the player's new location based on their current location
       and the direction they want to move."""
    # Annotate variables.
    new_location: str

    # Get the new location by calling the appropriate function.
    if current_location == "field":
        new_location = visit_field(direction)
    elif current_location == "settlement":
        new_location = visit_settlement(direction)
    elif current_location == "wood":
        new_location = visit_wood(direction)

    return new_location

def valid_input(user_choice: str) -> bool:
    """Return True if user_choice is a valid menu choice and False otherwise."""
    # Annotate and initialize local variables.
    valid: bool = False

    # Convert user_choice to uppercase.
    user_choice = user_choice.upper()

    # Determine if user_choice is one of the valid choices and return valid.
    if (user_choice == "N" or user_choice == "S"
        or user_choice == "E" or user_choice == "W"
        or user_choice == "Q"):
        valid = True

    return valid

def main() -> None:
    """Set up the game and run the main game loop."""

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
        elif location == "wood":
            print_wood_description()
        elif location == "settlement":
            print_settlement_description()
            
        # Obtain the user's command and update the location accordingly.
        choice = input("What is your command? (N, S, E, W, Q): ")
        while not valid_input(choice):
            choice = input("What is your command? (N, S, E, W, Q): ")
        if choice != "Q":
            location = get_new_location(location, choice)


        # If the game ended in one of the locations, set choice to Q.
        if location == "gameover":
            choice = "Q"

main()
