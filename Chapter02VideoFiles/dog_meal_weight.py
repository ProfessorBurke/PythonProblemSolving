"""Obtain an ideal adult dog weight from the user,
   then calculate and display the appropriate meal weight."""

MEAL_WEIGHT_PERCENTAGE: float = .03
dog_weight: float
meal_weight: float

# Obtain the dog's ideal adult weight from the user.
dog_weight = float(input("Please enter the dog's ideal adult weight: "))

# Calculate the weight of the dog's meal.
meal_weight = dog_weight * MEAL_WEIGHT_PERCENTAGE

# Display the weight of the dog's meal to the user.
print("The meal for a dog weighing {} lbs should weigh {:.2f} lbs."
      .format(dog_weight, meal_weight))
