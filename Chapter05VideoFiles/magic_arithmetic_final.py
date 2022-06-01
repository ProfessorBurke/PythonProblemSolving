"""
    A program that allows the user to play a game that tests their
    arithmetic skills.
    Maggie Burke
"""

# Note that this code is accidentally different from the specs:
# The asterisks should be around the magic number, and the
# underscores should be around the player position, not vice-versa.

import random

def show_instructions() -> None:
    """Show the game instructions to the player."""
    print("Welcome to the magic number game!")
    print("Instructions will go here.")
    
def roll_die(sides: int) -> int:
    """Return the value of a simulated die roll."""
    return random.randint(1, sides)

def display_board(player: int, magic_number: int) -> None:
    """Display the board, showing the player's position and
        the magic number position."""
    board: str = ""
    num: str
    for i in range(1, 101):
        if i < 10:
            num = " " + str(i)
        else:
            num = str(i)
        if i == player:
            num = "*" + num + "*"
        if i == magic_number:
            num = "_" + num + "_"
        for j in range(len(num), 8):
            num += " "
        board += num
        if i % 10 == 0:
            board += "\n"
    print(board)

def valid_move(player: int, move: int, roll: int) -> bool:
    """Return true if move can be reached arithmetically
       using player and roll."""
    valid: bool = False
    if (0 < move and move <= 100):
        if (player + roll == move or player - roll == move or roll - player == move
            or player * roll == move or player / roll == move or roll / player == move):
            valid = True
    return valid

def get_player_move(player: int, roll: int) -> int:
    """Return a valid player location from player input."""
    # Annotate variables
    move: int
    
    # Obtain the player's move.
    print("You rolled a {}.".format(roll))
    move = int(input("Where do you move? "))
    
    # Validate and obtain new move if invalid.
    while not valid_move(player, move, roll):
        print("You can't get to {} from {} with a roll of {}.  Try again!"
              .format(move, player, roll))
        move = int(input("Where do you move? "))
        
    # Return the valid move
    return move

def main():
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

    # Generate the magic number and display the board.
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
