"""
    Demonstrate input validation with a loop.
"""

# Annotate variables.
password: str
patient_temp: float
patient_age: int

# Obtain the user's password.
# Password must be at least eight characters.
password = input("Please enter your password: ")
while len(password) < 8:
    print("The password must be at least eight characters.")
    password = input("Please enter your password: ")

# Obtain the patient's temperature.
# The temperature must be between 65 and 110 degrees Fahrenheit.
patient_temp = float(input("What is the patient's temperature? "))
while patient_temp < 65 or patient_temp > 110:
    print("Patient temperature must be between 65 and 110.")
    patient_temp = float(input("What is the patient's temperature? "))

# Obtain the patient's age.
# The age must be between 1 and 130.
patient_age = int(input("What is the patient's age? "))
while patient_age < 1 or patient_age > 130:
    print("The age must be between 1 and 130.")
    patient_age = int(input("What is the patient's age? "))
    
