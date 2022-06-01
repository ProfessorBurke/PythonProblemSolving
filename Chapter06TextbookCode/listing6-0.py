"""Display eight planets."""

from typing import List

def main():
    planets: List[str]
    i: int = 0
    
    # Declare the list of planets.
    planets = ["Mercury", "Venus", "Earth", "Mars", 
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Loop over the list and print the planets.
    while i < len(planets):
        print(planets[i])
        i += 1

main()
