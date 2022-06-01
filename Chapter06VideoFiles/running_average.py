"""A program to calculate and graph a running
   average of weights.
   Maggie Burke
"""
from typing import List, TextIO
import turtle

def smooth(weights: List[float]) -> List[float]:
    """Smooth the values in weights using a weighted moving
       average."""
    averages = []
    for i in range(len(weights)):
        total = 0
        j = 0
        while j < 5 and i - j >= 0:
            total += weights[i - j] * (5 - j)
            j += 1
        # 15 - (5-j)(5-j+1)/2, simplified:
        num_values = ((11 * j) - (j ** 2)) / 2
        averages.append(total / num_values)
    return averages

def read_weights(file_name: str) -> List[float]:
    """Read the data from file_name into a list as float."""
    weights: List[float] = []
    weight_file: TextIO = open(file_name)
    weight: float = weight_file.readline()
    while weight != "":
        weights.append(float(weight))
        weight = weight_file.readline()
    weight_file.close()
    return weights

def write_weights(weights: List[float], file_name: str) -> None:
    """Write the weights to the file."""
    weight_file: TextIO = open(file_name, "w")
    for weight in weights:
        weight_file.write(str(weight) + "\n")
    weight_file.close()

def plot(values: List[float], color: str) -> None:
    """Plot the values in the color."""
    if len(values) > 0:
        mean: float = sum(values) / len(values)
        i: int
        turtle.penup()
        turtle.color(color)
        turtle.setpos(-150, (values[0] - mean) * 10)
        turtle.pendown()
        for i in range(1, len(values)):
            turtle.dot()
            turtle.setpos((i * 25) - 150, (values[i] - mean) * 10)
        turtle.dot()
        
def main() -> None:
    """Read a list of weights, obtain a new weight, plot, write
       the weights back to the file."""
    weights: List[float]
    smoothed: List[float]
    file_name: str = "weights.txt"
    new_weight: float

    # Read the weights from a file.
    weights = read_weights(file_name)
    
    # Obtain and append a new weight.
    new_weight = float(input("Please enter today's weight: "))
    weights.append(new_weight)

    # Smooth and plot the weights.
    smoothed = smooth(weights)
    plot(weights[-14:], "black")
    plot(smoothed[-14:], "red")

    # Write the weights to the file
    write_weights(weights, file_name)

main()

