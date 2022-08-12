"""
    A recursive solution to the hailstone problem.
"""

def hailstone(value: int) -> str:
    """Return a list that is the hailstone sequence for
       the value passed."""

    # Base case.
    if value == 1:
        return 1
    # Recursive cases.
    else:
        if value % 2 == 0:
            return str(value) + "," + str(hailstone(value // 2))  
        else:
            return str(value) + "," + str(hailstone(value*3+1))  



def main() -> None:
    """Obtain a value from the user, compute the hailstone
       sequence for that number, and then report the sequence
       and the number of steps."""
    value: int = int(input("What is the value? "))
    while value < 1:
        print("The value should be a positive integer.")
        value = int(input("What is the value? "))
    hailstone_seq: str = hailstone(value)
    print("The sequence is: " + hailstone_seq)
    print("The number of steps is: " + str(hailstone_seq.count(",")))

main()
