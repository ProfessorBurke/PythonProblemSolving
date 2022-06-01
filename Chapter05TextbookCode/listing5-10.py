"""Illustrate shadowing."""

def shadowy() -> None:
    var: int = 0
    print(var)

def main() -> None:
    shadowy()
    print(var)

var: int = 10
print(var)
main()

