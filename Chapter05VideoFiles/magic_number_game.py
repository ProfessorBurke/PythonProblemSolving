import random


def show_instructions() -> None:
    """Show the game instructions to the player."""
    print("Welcome to the magic number game!")
    print("Instructions will go here.")

def roll_die(sides: int) -> int:
    """Return the value of a simulated die roll."""
    return random.randint(1, sides)

def display_board(player: int, magic_number: int) -> None:
    """Display the board, showing the player's position
       and the magic number position."""
    print("Player position: {}".format(player))
    print("Magic number: {}".format(magic_number))

def valid_move(player: int, move: int, roll: int) -> bool:
    """Return True if move can be reached arithmetically
       using player and roll."""
    return True

def get_player_move(player: int, roll: int) -> int:
    """Return a valid player location from player input."""
    move: int

    # Obtain the player's move.
    print("You rolled a {}.".format(roll))
    move = int(input("Where do you move? "))
    while not valid_move(player, move, roll):
        print("You can't get to {} from {} with a roll of {}. Try again!"
              .format(move, player, roll)) 
        move = int(input("Where do you move? "))
    # Return the valid move
    return move

def main() -> None:
    """Play a magic arithmetic game."""

    # Annotate and initialize constants and variables.
    NUM_SIDES: int = 6
    roll: int
    player_location: int
    magic_number: int
    
    # Show the game instructions.
    show_instructions()

    # Roll the die for the first player move.
    player_location = roll_die(NUM_SIDES)
    
    # Generate the magic number and display the
    # board to the player.
    magic_number = random.randint(1, 100)
    display_board(player_location, magic_number)

    # Obtain valid player moves until they reach
    # the magic number.
    while player_location != magic_number:
        roll = roll_die(NUM_SIDES)
        player_location = get_player_move(player_location, roll)
        display_board(player_location, magic_number)
    print("You reached the magic number!")

main()
