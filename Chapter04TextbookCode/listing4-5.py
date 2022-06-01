"""Produce a table of final grades, given current average."""

average: float
average_75_percent: float
final_exam: int
final_grade: float

# Obtain the current average.
average = float(input("Please enter your average: "))

# Print the table header.
print("{:<15}{:<15}".format("Final Exam", "Final Grade"))

# Calculate the final grades for different exam grades
# in a loop, using exam grades from 90 down to 70 by 10.
average_75_percent = average * .75
final_exam = 100
while final_exam > 60:
    # Calculate the grade and display it.
    final_grade = average_75_percent + final_exam * .25
    print("{:<15d}{:<15.1f}".format(final_exam, final_grade))
    # Update the final exam grade for the next iteration.
    final_exam -= 10

