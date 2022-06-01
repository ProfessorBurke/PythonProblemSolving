"""Display the numbers for an apartment building
   with three floors and eight rooms per floor."""

floor: int
room: int
room_number: int

# Initialize the value of floor.
floor = 0

# Loop over three floors, printing the room number.
while floor < 3:

    # Loop through the rooms and print.
    room = 1
    while room < 9:
        room_number = floor * 100 + room
        print("Room number {}".format(room_number))
        room += 1

    # Update to the next floor.
    floor += 1
