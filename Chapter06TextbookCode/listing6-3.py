"""Display eight planets."""

from typing import List

def main():
    planets: List[str]
    i: int
    
    # Declare the list of planets.
    planets = ["Mercury", "Venus", "Earth", "Mars", 
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Loop over the list and print the planets.
    for i in range(len(planets)):
        print(planets[i])

main()
