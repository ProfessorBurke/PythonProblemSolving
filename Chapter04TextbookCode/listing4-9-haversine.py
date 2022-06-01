"""Compute the distance between two locations."""

import math

# Define some constants for the calculations.
RADIUS_EARTH = 6371000
LAT_CCRI = 41.712935
LON_CCRI= -71.481696
LAT_CCRI_RADIANS = math.radians(LAT_CCRI)
LON_CCRI_RADIANS = math.radians(LON_CCRI)

# Get the first set of coordinates from the user and
# compute the distance.  We will store this in our
# most wanted holder variables.
closest_location = input("Please enter the location name: ")
latitude = float(input("Please enter the latitude: "))
longitude = float(input("Please enter the longitude: "))
a = math.sin(math.radians(latitude - LAT_CCRI)/2)**2 + \
    math.cos(LAT_CCRI_RADIANS) * math.cos(math.radians(latitude) * \
    math.sin(math.radians(longitude - LON_CCRI)/2)**2
closest_distance = RADIUS_EARTH * 2 * \
                   math.atan2(math.sqrt(a), math.sqrt(1-a)) / 1000

# Now loop, getting four new locations, and find the closest.
i = 0
while i < 4:
    # Get the inputs and calculate the distance.
    location = input("Please enter the location name: ")
    latitude = float(input("Please enter the latitude: "))
    longitude = float(input("Please enter the longitude: "))
    a = math.sin(math.radians(latitude - LAT_CCRI)/2)**2 + \
        math.cos(LAT_CCRI_RADIANS)**2 * \
        math.sin(math.radians(longitude - LON_CCRI)/2)**2
    distance = RADIUS_EARTH * 2 * \
               math.atan2(math.sqrt(a), math.sqrt(1-a)) / 1000

    # Compare to the closest distance and replace if closer.
    if distance < closest_distance:
        closest_distance = distance
        closest_location = location

    # Update the loop control variable.
    i += 1

# Display the closest location to the user
print("{} is the closest location, with a distance of " + \
      "{:.1f} km.".format(closest_location, closest_distance))
