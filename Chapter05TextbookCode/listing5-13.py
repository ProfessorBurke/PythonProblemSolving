"""Convert a longitude from DMS to DD format."""

def valid_longitude(degrees: int, minutes: int,
                    seconds: int, direction: str) -> bool:
    """Return true if longitude is valid."""
    valid: bool = False
    # Check that the direction is E or W.
    if direction == "E" or direction == "W":
        # Check that minutes and seconds are between 0 and 60.
        if (minutes >= 0  and minutes < 60
            and seconds >= 0 and seconds < 60):
            # Check that degrees is < 180 or exactly 180
            # (okay only if minutes and seconds are 0).
            if degrees < 180:
                valid = True
            elif degrees == 180 and minutes == 0  and seconds == 0:
                valid = True
    return valid

def main() -> None:
    degrees: int
    minutes: int
    seconds: int
    direction: str
    longitude_dd: float
    
    # Obtain longitude values from the user.
    degrees = int(input("Please enter the degrees: "))
    minutes = int(input("Please enter the minutes: "))
    seconds = float(input("Please enter the seconds: "))
    direction = input("Enter E or W: ")

    # Validate the input values.
    while not valid_longitude(degrees, minutes, seconds, direction):
        print("That is not a valid longitude.")
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

main()
