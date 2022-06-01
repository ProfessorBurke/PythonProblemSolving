"""Find the location closest to Warwick, RI."""

import math

closest_location: str
location: str
latitude: float
longitude: float
closest_distance: float
a: float
distance: float
i: int

# Define some constants for the calculations.
LAT_CCRI: float = 41.712935
LON_CCRI: float = -71.481696

# Get the first set of coordinates from the user and
# compute the distance.  We will store this in our
# most wanted holder variables.
closest_location = input("Enter the location name: ")
latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))
closest_distance = (math.sqrt((LAT_CCRI - latitude)**2 +
                              (LON_CCRI - longitude)**2) * 100)

# Now loop, getting four new locations, and find the closest.
i = 0
while i < 4:
    # Get the inputs and calculate the distance.
    location = input("Enter the location name: ")
    latitude = float(input("Enter the latitude: "))
    longitude = float(input("Enter the longitude: "))
    distance = (math.sqrt((LAT_CCRI - latitude)**2 +
                          (LON_CCRI - longitude)**2) * 100)

    # Compare to the closest distance and replace if closer.
    if distance < closest_distance:
        closest_distance = distance
        closest_location = location

    # Update the loop control variable.
    i += 1

# Display the closest location to the user
print(closest_location + " is the closest location, with a " + 
      "distance of {:.1f} km.".format(closest_distance))
