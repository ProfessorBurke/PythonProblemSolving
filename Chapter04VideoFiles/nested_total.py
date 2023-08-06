"""
    Nested totals.
"""

# Annotate variables.
day: int
week: int
day_hours: float
week_total: float
month_total: float

# Obtain the hours volunteered for four weeks and total them.
month_total = 0
week = 0
while week < 4:
    
    # Obtain the hours volunteered every day for a week and total them.
    week_total = 0
    day = 0
    while day < 7:
        day_hours = float(input("How many hours did you volunteer on day {} of week {}? "
                                .format(day + 1, week + 1)))
        week_total += day_hours
        day += 1
    print("The weekly total is {}.".format(week_total))
    month_total += week_total

    week += 1

print("The monthly total is {}.".format(month_total))
