"""Display eight planets."""

from typing import List

def main():
    planets: List[str]
    planet: str
    
    # Declare the list of planets.
    planets = ["Mercury", "Venus", "Earth", "Mars", 
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Loop over the list and print the planets.
    for planet in planets:
        print(planet)

main()
