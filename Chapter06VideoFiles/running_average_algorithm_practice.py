
from typing import List

weights: List[float] = [150, 152, 151, 152.5, 153.5,
                        152, 155, 154.5, 156.5, 152,
                        155, 156, 157, 156.5]
i: int
j: int
averages: List[float] = []
total: int

for i in range(len(weights)):
    total = 0
    j = 0
    while j<5 and i-j >=0:
        total += weights[i-j] * (5-j)
        j += 1
    # 15 - (5-j)*(6-j) / 2
    averages.append(total / (((11 * j) - (j**2)) / 2))
print(averages)
