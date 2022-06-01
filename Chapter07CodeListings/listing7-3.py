"""Detect a palindrome recursively."""

def is_palindrome(string: str, first: int, last: int) -> bool:
    """Return True if string is a palindrome."""
    # Base case string is a palindrome.
    if first >= last:
        return True
    # Base case string is not a palindrome.
    elif string[first] != string[last]:
        return False
    # Recursive case.
    else:
        return is_palindrome(string, first+1, last-1)


def main() -> None:
    """Obtain a string and determine if it's a palindrome."""
    # Obtain the string.
    string: str = input("Please enter a string: ")

    # Determine if it's a palindrome and report.
    if is_palindrome(string, 0, len(string)-1):
        print("That is a palindrome!")
    else:
        print("That is not a palindrome.")

main()
