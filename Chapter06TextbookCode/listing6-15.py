"""Process a user response of yes."""

def main() -> None:
    """Ask the user to type yes."""

    answer: str = input("Please enter yes: ")
    upper_answer: str = answer.upper()
    if upper_answer == "YES":
        print("You entered yes!")

main()
