"""
    Illustrate passing parameters of different
    data types.
"""

def change_references(number: int,
                      word: str,
                      decimal: float,
                      numbers: list[int]) -> None:
    """Assign a new value to each variable."""
    number = 1
    word = "hello"
    decimal = 2.5
    numbers = [1,2,3]
    print("\nIn change_references:")
    print(number, word, decimal, numbers)

def main() -> None:
    """Assign some values to variables, print them,
       and then pass them to change_references."""
    # Annotate and assign values.
    number: int = 200
    word: str = "world"
    decimal: float = 3.14159
    numbers: list[int] = [10, 20, 30]

    print("In main:")
    print(number, word, decimal, numbers)

    change_references(number, word, decimal, numbers)

    print("\nBack in main:")
    print(number, word, decimal, numbers)

main()
