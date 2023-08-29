"""
    Illustrate that global (main / module) variables cannot be
    modified inside functions.
"""

def cannot_change() -> None:
    """Try to change a global variable."""
    x = 5
    print(x)

x = 10
print(x)
cannot_change()
print(x)
