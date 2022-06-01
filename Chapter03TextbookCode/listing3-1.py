"""Convert a longitude from DMS to DD format."""

degrees: int
minutes: int
seconds: float
direction: str
longitude_dd: float

# Obtain longitude values from the user.
degrees = int(input("Please enter the degrees: "))
minutes = int(input("Please enter the minutes: "))
seconds = float(input("Please enter the seconds: "))
direction = input("Enter E or W: ")

# Convert to DD format (absolute distance).
longitude_dd = degrees + minutes/60 + seconds/3600

# If west of the prime meridian, multiply by -1.
if direction == "W":
    longitude_dd = longitude_dd * -1

# Display the DD longitude to the user.
print("The longitude in decimal degrees format is {:.6f}."
      .format(longitude_dd))


