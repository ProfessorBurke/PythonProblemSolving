"""
    An example of nested lists.
    The list represents books borrowed from a library
    in each of the twelve months over four years.
    Loops iterate over the list by year and by month.
"""
# Annotate and initialize constants for better output.
YEARS: list[int] = [2019, 2020, 2021, 2022]
MONTHS: list[str] = ["January", "February", "March", "April",
                     "May", "June", "July", "August", "September",
                     "October", "November", "December"]

# Annotate and initialize the list of borrowing statistics.
books = list[list[int]]
books = [[300, 305, 290, 274, 200, 150, 210, 220, 204, 246, 250, 201],
         [302, 299, 100, 0, 25, 50, 75, 80, 52, 74, 86, 102],
         [115, 90, 87, 92, 120, 117, 99, 115, 123, 150, 182, 178],
         [204, 199, 211, 203, 182, 130, 154, 168, 154, 203, 235, 164]]

# Annotate and initialize total and average variables.
total_year: int = 0
total_month: int = 0
average_year: float
average_month: float

# Annotate iterator variables.
month_index: int
year_index: int

# Find the average of books borrowed each year.
# Iterate over the list one row at a time.
for year_index in range(len(books)):
    total_year = 0
    for month_index in range(len(books[year_index])):
        total_year += books[year_index][month_index]
    average_year = total_year / len(books[year_index])
    print("The yearly average for {} is {:.2f}."
          .format(YEARS[year_index], average_year))


# Find the average of books borrowed each month.
# Iterate over one column of the list at a time.
for month_index in range(len(books[0])):
    total_month = 0
    for year_index in range(len(books)):
        total_month += books[year_index][month_index]
    average_month = total_month / len(books[0])
    print("The monthly average for {} is {:.2f}."
          .format(MONTHS[month_index], average_month))



