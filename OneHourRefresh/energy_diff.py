"""
    Obtain energy usage per capita data for two years for the same
    country and calculate the difference.
"""
# Annotate variables.
country_name: str
year1: int
year2: int
energy1: float
energy2: float
diff: float

# Obtain country name, years, and energy usage data for two years.
country_name = input("Please enter the country name: ")
year1 = int(input("What is the first year? "))
year2 = int(input("What is the second year? "))
energy1 = float(input("What is the energy usage for the first year? "))
energy2 = float(input("What is the energy usage for the second year? "))

# Calculate the difference in energy usage for the two years.
diff = energy2 - energy1

# Display the energy usage difference to the user.
print("In " + country_name + ", the difference in energy usage between "
      + str(year1) + " and " + str(year2) + " is " + str(diff) + ".")
print("In {:s}, the difference in energy usage between {:d} and {:d} is {:.3f}."
      .format(country_name, year1, year2, diff))
print(f"In {country_name:s}, the difference in energy usage between {year1:d} and {year2:d} is {diff:.3f}.")
