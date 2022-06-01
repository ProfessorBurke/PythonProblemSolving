"""
    Program with functions to predict the
    time to finish a road race.
    This program assumes distances are in the
    same units.
"""

def get_positive_value(prompt: str) -> float:
    """Obtain a positive value."""
    value: float
    value = float(input(prompt))
    while not value > 0:
        print("The value must be positive.")
        value = float(input(prompt))
    return value

def predict_time(t1: float, d1: float,
                 d2: float) -> float:
    """Calculate and return the predicted time."""
    t2: float
    t2 = t1 * 1.06 * (d2 / d1)
    return t2

def main() -> None:
    """Obtain a a distance and time for one race, and a
       distance for a second race, and predict the time."""
    time1: float
    time2: float
    distance1: float
    distance2: float
    # Obtain positive values for the first time and both distances.
    time1 = get_positive_value("How many seconds to complete the short distance? ")
    distance1 = get_positive_value("What is the short distance? ")
    distance2 = get_positive_value("What is the long distance (same units)? ")

    # Calculate the area.
    time2 = predict_time(time1, distance1, distance2)

    # Display the result.
    print("The predicted time to run {:.1f} is {:.1f} seconds."
          .format(distance2, time2))

main()
