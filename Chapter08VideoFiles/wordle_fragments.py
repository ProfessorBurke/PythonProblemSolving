"""
    The beginnings of a text version of wordle.
"""

def get_word() -> str:
    return "sieve"

def get_user_word() -> str:
    """Obtain a guess from the user."""
    word: str = input("What is your guess? ")
    return word[:5]

def word_to_ordered_pairs(word: str) -> set:
    """Return the word as a set of ordered pairs of
       tuples of (letter, index)."""
    i: int = 0
    letter: str
    result: list = []
    for letter in word:
        result.append((i, letter))
        i += 1
    return set(result)

def pairs_to_letter_list(pairs: set) -> list:
    """Take a set of ordered pairs and convert to a list of letters."""
    letters: list = []
    for pair in pairs:
        letters.append(pair[1])
    return letters

def main() -> None:
    """Test out some functions that will be used in a wordle game."""
    # Get the puzzle word and user guess and convert to a set
    # of ordered pairs.
    word: str = get_word()
    winning_word_set: set = word_to_ordered_pairs(word)
    user_word: str = get_user_word()
    user_guess_set: set = word_to_ordered_pairs(user_word)

    # Remove the correct words in the correct location from
    # both sets
    green_letters: set = winning_word_set & user_guess_set
    rest_of_puzzle: set = winning_word_set - green_letters
    rest_of_guess: set = user_guess_set - green_letters

    # Convert those to lists of just the letters.
    rest_of_puzzle_letters: list = pairs_to_letter_list(rest_of_puzzle)
    rest_of_guess_letters: list = pairs_to_letter_list(rest_of_guess)

    # Now iterate through the guess and assign the letters in the guess
    # to one of two lists.
    not_in_word: list = []
    wrong_location: list = []
    for letter in rest_of_guess_letters:
        if letter in rest_of_puzzle_letters:
            wrong_location.append(letter)
            rest_of_puzzle_letters.remove(letter)
        else:
            not_in_word.append(letter)

    # Print the results.
    print("Letters in the correct location: " + str(green_letters))
    print("Letters in the word in the wrong location: " + str(wrong_location))
    print("Letters not in the word: " + str(not_in_word))

main()






