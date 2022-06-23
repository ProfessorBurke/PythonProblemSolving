"""
    Determine what items should be packed depending on mode of travel.
"""

plane_answer: str
packing_list: str = ""

# Obtain the answer to the air travel question from the user.
plane_answer = input("Are you traveling by plane? (yes / no): ")

# Determine what should be packed based on the travel answer.
if plane_answer == "yes":
    packing_1ist = "\nheadphones\nreading material"

# Display the packing list to the user.
if packing_list != "":
    print(packing_list)
