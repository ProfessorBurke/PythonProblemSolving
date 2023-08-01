"""
    Examples of counting loops.
"""

# Annotate variables.
i: int
num_loops: int
patient_age: int

# A while loop that executes five times.
i = 0
while i < 5:
    print("I'm in the loop!")
    i += 1

for i in range(5):
    print("I'm in the loop!")

# A while loop that executes num_loops times.
num_loops = int(input("How high should I count? "))
i = 0
while i < num_loops:
    print(i)
    i += 1

for i in range(num_loops):
    print(i)

# Obtain the patient's age.
# The age must be between 1 and 130.
patient_age = int(input("What is the patient's age? "))
while patient_age < 1 or patient_age > 130:
    print("The age must be between 1 and 130.")
    patient_age = int(input("What is the patient's age? "))
