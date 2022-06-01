"""Analyze video channel data."""

from itertools import combinations, chain
from typing import List, Set, TextIO, FrozenSet, Dict
from collections import defaultdict

def read_file() -> List[str]:
    """Return a list of the lines in the file."""
    # to-do:  take file name as parameter, confirm it exists
    channel_file: TextIO = open("channel_data.txt")
    file_data: List[str] = channel_file.readlines()
    return file_data

def get_tags(file_contents: List[str]) -> Dict[FrozenSet[str], List[int]]:
    """Find the tags in the file contents."""
    TAGS_INDEX: int = 1
    SUBSCRIBES_INDEX: int = 5
    COMMENTS_INDEX: int = 4
    line_tags: List[str]
    tags: Set[FrozenSet[str]] = set()
    line: str
    tags_string: str
    power_set_tags: Set[FrozenSet[str]] = []
    result: Dict[FrozenSet[str],
                 List[int]] = defaultdict(lambda: [0,0])

    for line in file_contents:
        # Separate each line in the file into pieces.
        # Pull the tags piece out of the line, then
        # pull the tags out of that; ignore blank first tag.
        tags_string = line.split(",")[TAGS_INDEX]
        line_tags = tags_string.split("#")[1:]
        # Add the power set of the new tags to the set.
        power_set_tags = [[frozenset(s) for s in combinations(line_tags, i)]
                  for i in range(1, len(line_tags)+1)]
        power_set_tags = set(chain.from_iterable(power_set_tags))
        tags = tags | power_set_tags
        for tag_set in power_set_tags:
            split_line = line.split(",")
            result[tag_set][0] += int(split_line[COMMENTS_INDEX])
            result[tag_set][1] += int(split_line[SUBSCRIBES_INDEX])

    # Create and return the power set.
    return result


def main() -> None:
    """Get the tags from the file data."""
    file_contents: List[str] = read_file()
    result: Dict[FrozenSet[str], List[int]] = get_tags(file_contents)
    result_sorted = sorted(result, key = lambda k: sum(result[k]), reverse = True)
    for k in result_sorted:
        print(k, result[k])

main()
