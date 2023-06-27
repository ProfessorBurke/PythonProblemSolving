"""
    Setting a flag in multiple places.
"""

# Annotate variables.
temperature: int
rain: str
good_conditions: bool = True

# Obtain conditions from the user and
# change the flag if the inputs indicate conditions aren't good.
temperature = int(input("What is the temperature (F) outside? "))

if temperature <= 50:
    good_conditions = False

rain = input("Is it raining outside? (yes/no) ")
if rain == "yes":
    good_conditions = False

# Test if conditions are good and send the user outside if so.
if good_conditions:
    print("Go outside.")
