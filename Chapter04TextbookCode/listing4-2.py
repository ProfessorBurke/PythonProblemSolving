"""Calculate and print box coordinates."""
SIDE: int = 50
num_boxes: int = 0
y_coordinate: int = 0

# Print coordinates of five boxes.
while num_boxes < 3:
    print("X: {}, Y: {}".format(0, y_coordinate))
    y_coordinate = y_coordinate + SIDE
    num_boxes = num_boxes + 1
