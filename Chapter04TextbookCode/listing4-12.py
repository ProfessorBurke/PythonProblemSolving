"""Sentinel loop to average the runner ages."""

# Initialize the sum, count, and age.
total_ages: int = 0
count: int = 0
age: int = 0

# Obtain age, add to sum, increment count until the sentinel.
while age != -1:
    age = int(input("Please enter the runner's age, -1 to quit: "))
    if age != -1:
        total_ages += age
        count += 1
        
# If any ages were entered, average them.
if count != 0:
    average = total_ages / count
    print("The average age is {:.1f}.".format(average))
else:
    print("No ages were entered.")
