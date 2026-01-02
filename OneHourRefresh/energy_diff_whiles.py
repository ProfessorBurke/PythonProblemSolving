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

# Obtain country name.
country_name = input("Please enter the country name or 'done' to quit: ")
while country_name != "done":
    # Obtain and validate the years.
    year1 = int(input("What is the first year? "))
    while year1 < 1965 or year1 > 2024:
        print("That is not a valid year.")
        year1 = int(input("What is the first year? "))
        
    year2 = int(input("What is the second year? "))
    while year2 < 1965 or year2 > 2024:
        print("That is not a valid year.")
        year1 = int(input("What is the second year? "))

    # Obtain the energy usage data for the two years.
    energy1 = float(input("What is the energy usage for the first year? "))
    energy2 = float(input("What is the energy usage for the second year? "))

    # Calculate the difference in energy usage for the two years.
    diff = energy2 - energy1

    # Display the energy usage difference to the user.
    if diff > 0:
        print(f"Energy usage between {year1:d} and {year2:d} increased by {diff:.3f} kWh.")
    elif diff < 0:
        print(f"Energy usage between {year1:d} and {year2:d} decreased by {diff:.3f} kWh.")
    else:
        print(f"Energy usage between {year1:d} and {year2:d} did not change.")
    country_name = input("Please enter the country name or 'done' to quit: ")
    
