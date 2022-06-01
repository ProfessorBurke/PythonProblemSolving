"""Construct a tidy dictionary of social media data."""
from typing import List, Dict, TextIO
from math import nan, isnan

def to_float_na(data_list: List[str]) -> List[float]:
    """Return float version of the parameter or nan."""
    result: List[float] = []
    for value in data_list:
        if value == "NA":
            result.append(nan)
        else:
            result.append(float(value))
    return result

def read_csv(filename: str) -> List[List[float]]:
    """Return file processed into a list of lists."""
    tidy_file: TextIO
    data: List[str]
    observations: List[List[float]] = []
    row: str
    # Read file lines, split, convert, add to list.
    tidy_file = open(filename)
    data = tidy_file.readlines()
    for row in data:
        observations.append(to_float_na(row.split(",")))
    tidy_file.close()
    return observations

def make_tidy_dict(data: List[List[float]], headings: List[str]) -> Dict[str, List[float]]:
    """Return a dictionary from a list of lists."""
    result: Dict[str, List[float]] = {}
    flat: List[float] = []
    row: List[float]
    item: float
    # Flatten the list of lists
    for row in data:
        for item in row:
            flat.append(item)
    # Reshape and add to the dictionary.
    for i in range(len(headings)):
        result[headings[i]] = flat[i::len(headings)]
    return result

def total_list(data: List[float]) -> float:
    """Return the total of all non-nan values."""
    total: float = 0
    for value in data:
        if not isnan(value):
            total += value
    return total

def main() -> None:
    """Read the file into a dict and sum the columns."""
    key: str
    value: List[float]
    data: List[List[float]] = read_csv("social_tidy.csv")
    data_dict: Dict[str, List[float]] = make_tidy_dict(data,
                                                  ["User ID",
                                                   "Followers",
                                                   "Status Updates"])
    for key, value in data_dict.items():
        if key != "User ID":
            print("Sum of {}: {}".format(key, total_list(value)))

main()



