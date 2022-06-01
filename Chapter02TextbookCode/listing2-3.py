"""Produce a table of final grades, given current average."""

average: float
average_75_percent: float
final_100_grade: float
final_90_grade: float
final_80_grade: float
final_70_grade: float

# Obtain the current average.
average = float(input("Please enter your average: "))

# Calculate the final grades for different exam grades.
average_75_percent = average * .75
final_100_grade = average_75_percent + 100 * .25
final_90_grade = average_75_percent + 90 * .25
final_80_grade = average_75_percent + 80 * .25
final_70_grade = average_75_percent + 70 * .25

# Display a table of results.
print("{:<15}{:<15}".format("Final Exam", "Final Grade"))
print("{:<15d}{:<15.1f}".format(100, final_100_grade))
print("{:<15d}{:<15.1f}".format(90, final_90_grade))
print("{:<15d}{:<15.1f}".format(80, final_80_grade))
print("{:<15d}{:<15.1f}".format(70, final_70_grade))
