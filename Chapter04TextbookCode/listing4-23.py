"""Compute and print cicada emergence every 13 years
   since 2018 in the 21st century."""

# Define constants for the start and end years
# and the emergence period.
START_YEAR: int = 2018
END_YEAR: int = 2100
PERIOD: int = 13
emergency_year: int

# Display the years the cicada will emerge.
print("Cicadas will emerge in the following years:")
for emergence_year in range(START_YEAR, END_YEAR, PERIOD):
    print("{}".format(emergence_year))
