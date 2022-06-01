"""Vocabulary quiz."""
def quiz_word(word1: str, word2: str, language: str) -> None:
    """Quiz the user on word in language 2."""
    answer: str
    # Get the user's answer.
    answer = input("What is {} in {}? ".\
                   format(word1, language))
    # Compare it to the correct answer
    # and print a message.
    if answer == word2:
        print("Correct!")
    else:
        print("No, {} in {} is {}.".\
              format(word1, language, word2))        
    
def main() -> None:
    """Quiz the user on vocabulary."""
    quiz_word("book", "kitab", "Arabic")
    quiz_word("school", "madrasa", "Arabic")

main()
