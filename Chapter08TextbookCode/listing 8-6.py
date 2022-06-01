"""Demonstrate set operations."""
from typing import List, Set

def main() -> None:
    """Demonstrate set operations."""
    # Create a set from hard-coded values and from a list.
    cs101_list: List[str] = ["Ally", "Ben", "Cam", "Deb", "Ben"]
    ma150: Set[str] = {"Ben", "Del", "Jorge"}
    cs101: Set[str] = set(cs101_list)

    # Add and remove members from sets.
    ma150.add("Subi")
    cs101.remove("Cam")

    # Display the sets.
    print("Students in CS 101:", cs101)
    print("Students in MA 150:", ma150)

    # Test for membership in a set.
    print("Ally in CS 101: " + ("yes" if "Ally" in cs101 else "no"))
    print("Ally in MA 150: " + ("yes" if "Ally" in ma150 else "no"))

    # Set operations.
    print("Students in both CS 101 and MA 150: ", (cs101 & ma150))
    print("Students in CS 101 who are not in MA 150: ", (cs101 - ma150))
    print("Students in either course or both: ", (cs101 | ma150))
    print("Students in only one course or the other: ", (cs101 ^ ma150))

main()
