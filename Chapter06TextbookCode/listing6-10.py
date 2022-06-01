"""Read and process records of volunteer hours."""

from typing import List, TextIO

def process_student_hours(hours: List[str]) -> None:
    """Display a report of the hours in the list."""
    total: int = 0
    i: int = 0
    average: float
    if len(hours) != 0:
        # Loop over the list and accumulate a total.
        while i < len(hours):
            total += float(hours[i])
            i += 1
        # Compute an average and display the results.
        average = total / len(hours)
        print("Total hours worked: {}".format(total))
        print("Average hours worked: {:.2f}\n".format(average))
        
def main() -> None:
    """Read each comma-delimited line of the file and process."""
    hours_file: TextIO = open("hours.txt")
    hours_data: str = hours_file.readline()
    while (hours_data != ""):
        hours_data = hours_data.strip()
        if len(hours_data) != 0:
            hours_list = hours_data.split(",")
            process_student_hours(hours_list)
        hours_data = hours_file.readline()
    hours_file.close()

main()
