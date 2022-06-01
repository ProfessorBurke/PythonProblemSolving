"""Read vocabulary information from a file
   and quiz the user."""

import os.path
import typing

def quiz_word(word1: str, word2: str, language: str) -> None:
    """Quiz the user on word in language 2."""
    answer: str
    answer = input("What is {} in {}? "
                   .format(word1, language))
    if answer == word2:
        print("Correct!")
    else:
        print("No, {} in {} is {}."
              .format(word1, language, word2))

def main() -> None:
    file_name: str
    vocabulary_file: typing.TextIO
    language1: str
    language2: str
    vocab_lang1: str
    vocab_lang2: str
    
    # Obtain the file name from the user, check
    # that it exists, and open it if so.    
    file_name = input("Please enter the file name: ")
    if os.path.isfile(file_name):
        vocabulary_file = open(file_name)

        # Read the header record from the file.
        language1 = vocabulary_file.readline().strip()
        language2 = vocabulary_file.readline().strip()

        # Read the vocabulary from the file until the end
        # and quiz the user.
        vocab_lang1 = vocabulary_file.readline().strip()
        while vocabulary1 != "":
            vocab_lang2 = vocabulary_file.readline().strip()
            quiz_word(vocab_lang1, vocab_lang2, language2)
            vocab_lang1 = vocabulary_file.readline().strip()

    # Display an error if the file was not found.
    else:
        print("That file was not found.")

main()
