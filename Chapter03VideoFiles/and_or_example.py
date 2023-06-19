"""
    Demonstrate and and or.
"""

# Annotate variables.
clean_room: str
empty_dishes: str
num_ice_cream: int
hours_at_park: float

### Ask the user whether they've completed their chores.
##clean_room = input("Did you clean your room? (yes/no) ")
##empty_dishes = input("Did you empty the dishwasher? (yes/no) ")
##
### If they both cleaned their room and emptied the dishwasher,
### they can go to the beach.
##if clean_room  == "yes" and empty_dishes == "yes":
##    print("You may go to the beach.")
##else:
##    print("You must finish your chores if you want to go to the beach.")

num_ice_cream = int(input("How many ice creams did you buy your sister? "))
hours_at_park = float(input("How many hours did you spend at the park? "))

if num_ice_cream > 0  or hours_at_park > .5:
    print("Your sister is very happy.")
else:
    print("Your sister is bored.")

### Examples of wrong and and or expressions:
##if answer == "yes" or "YES"
##if clean_room and empty_dishes == "yes"


    
