"""Recursively sum the integers from 1 to 100."""

def sum_ints(num: int) -> int:
    """Return the sum of the integers from 1 to num."""
    if num == 1:
        return 1
    else:
        return num + sum_ints(num-1)

def main() -> None:
    """Compute the sum of integers from 1 to n two ways."""
    n: int = 100
    print("The recursively computed sum is {:d}." 
          .format(sum_ints(n)))
    print("Gauss' formula tells us the sum is {:.0f}." 
          .format((n * (n+1) / 2)))

main()
