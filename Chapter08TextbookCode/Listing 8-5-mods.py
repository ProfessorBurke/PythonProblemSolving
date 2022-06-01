"""Construct a tidy dictionary of social media data."""
from typing import List, Dict, TextIO
from math import nan, isnan

def read_csv(filename: str) -> List[List[float]]:
    """Return file processed into a list of lists."""
    tidy_file: TextIO
    data: List[str]
    observations: List[List[float]] = []
    row: str
    # Read file lines, split, convert, add to list.
    tidy_file = open(filename)
    data = tidy_file.readlines()
    observations = [[nan if d == "NA" else float(d) for d in row.split(",")] for row in data]
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

def main() -> None:
    """Read the file into a dict and sum columns."""
    data: List[List[float]] = read_csv("social_tidy.csv")
    data_dict: Dict[str, List[float]] = make_tidy_dict(data,
                                                  ["User ID",
                                                   "Followers",
                                                   "Status Updates"])
    for key, value in data_dict.items():
        if key != "User ID":
            print("Sum of {}: {}".format(key, sum([x for x in value if not isnan(x)])))


main()



