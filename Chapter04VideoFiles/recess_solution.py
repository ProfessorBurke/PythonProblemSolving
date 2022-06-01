"""
    Read elementary school recess and enrollment data
    from a file and produce a report including total
    number of students and average amount of recess time
    for any number of schools.
    File is of the form:
    School /n Enrollment /n Recess minutes
"""
import typing
import os.path

# Annotate and initialize variables
school_data_file: typing.TextIO
school_name: str
enrollment: int
recess_time: int
total_enrollment: int = 0
num_schools: int = 0
total_recess_minutes: int = 0
average_recess_minutes: float = 0
file_name: str

# Obtain the file name from the user.
file_name = input("Please enter the name of the data file (with the .txt extension): ")

if os.path.isfile(file_name):
    # Open the school data file in read mode.
    school_data_file = open(file_name)

    # Read school name, enrollment, and recess minutes
    # for all records in the file.
    school_name = school_data_file.readline().strip()
    while school_name != "":
        num_schools += 1
        enrollment = int(school_data_file.readline())
        total_enrollment += enrollment
        recess_time = int(school_data_file.readline())
        total_recess_minutes += recess_time
        school_name = school_data_file.readline().strip()

    # Compute the average recess minutes if there was any data.
    if num_schools != 0:
        average_recess_minutes = total_recess_minutes / num_schools

    # Print the summary table of data from the file.
    print("{:<15s}{:<15s}{:<15s}".format("Num. Schools",
                                         "Num. Students",
                                         "Avg. Recess (minutes)"))
    print("{:<15d}{:<15d}{:<15.1f}".format(num_schools,
                                           total_enrollment,
                                           average_recess_minutes))
else:
    print(file_name + " doesn't exist.")





