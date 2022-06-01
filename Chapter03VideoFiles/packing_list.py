"""
    Determine what items should be packed depending on mode of travel
    and whether there will be outside activities.
"""

plane_answer: str
train_answer: str
car_answer: str
outside_answer: str
packing_list: str = ""

# Obtain answers to travel questions from the user.
plane_answer = input("Are you traveling by plane? (yes / no): ")
train_answer = input("Are you traveling by train? (yes / no): ")
car_answer = input("Are you traveling by automobile? (yes / no): ")
outside_answer = input("Will you be outside frequently during the trip? (yes / no): ")

# Determine what should be packed based on travel answers.
if plane_answer == "yes":
    packing_list += "headphones\nreading material"
if train_answer == "yes":
    if packing_list != "":
        packing_list += "\n"
    packing_list += "earplugs\nwater bottle"
# There is overlap between outside and car, so considered together.
if outside_answer == "yes":
     if packing_list != "":
        packing_list += "\n"    
     packing_list += "sunglasses\nwalking shoes\numbrella"
elif car_answer == "yes":
    if packing_list != "":
        packing_list += "\n"    
    packing_list += "sunglasses"

# Display the packing list to the user.
if packing_list != "":
    print(packing_list)
