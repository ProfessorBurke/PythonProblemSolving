"""
    Estimate the global population for three years, given
    an initial population.
"""

# Annotate constants and variables.
GROWTH_RATE: float = 1.011
population_billions: float
i: int

# Obtain a population.
population_billions = float(input("Enter the population (billions): "))

# Calculate and display the next three years' population.
i = 0
while i < 3:
    population_billions *= GROWTH_RATE
    print("The next year's population projection is {:.1f} billion."
          .format(population_billions))
    i += 1
