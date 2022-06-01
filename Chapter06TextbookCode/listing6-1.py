"""Bad Pattern! Demonstrate an off-by-one error."""

from typing import List

def main():
    cities: List[str]
    i: int = 0
    
    # Declare a list of cities.
    cities = ["Providence", "Hanoi", "Monrovia"]

    # Loop over the list and print the cities,
    # but one too many times!
    while i <= len(cities):
        print(cities[i])
        i += 1

main()

