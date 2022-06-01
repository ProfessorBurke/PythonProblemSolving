"""Average the number of social media followers."""

from typing import List, TextIO

def read_csv(filename: str) -> List[List[str]]:
    """Return file processed into a list of lists."""
    tidy_file: TextIO
    data: List[str]
    observations: List[List[str]] = []
    row: str
    # Read file lines, split, and append into a list.
    tidy_file = open(filename)
    data = tidy_file.readlines()
    for row in data:
        observations.append(row.split(","))
    tidy_file.close()
    return observations

def remove_na(observations: List[List[str]],
              column: int) -> List[List[str]]:
    """Return observations with NA's removed from column."""
    result: List[List[str]] = []
    observation: List[str]
    for observation in observations:
        if not "NA" in observation[column]:
            result.append(observation)
    return result
    
def average_column(observations: List[List[str]],
                   column: int) -> int:
    """Return the average of column."""
    total: int = 0
    observation: List[str]
    for observation in observations:
        total += int(observation[column])
    return total / len(observations)

def main() -> None:
    FOLLOWERS: int = 1
    data: List[List[str]]
    average: float
    data = read_csv("social_tidy.csv")
    data = remove_na(data, FOLLOWERS)
    average = average_column(data, FOLLOWERS)
    print("Average followers: {:.1f}.".format(average))

main()


