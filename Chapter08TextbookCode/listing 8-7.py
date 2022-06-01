"""Analyze video channel data."""

from itertools import combinations, chain
from typing import List, Set, TextIO, FrozenSet

def read_file() -> List[str]:
    """Return a list of the lines in the file."""
    # to-do:  take file name as parameter, confirm it exists
    channel_file: TextIO = open("channel_data.txt")
    file_data: List[str] = channel_file.readlines()
    return file_data

def get_tags(file_contents: List[str]) -> Set[FrozenSet[str]]:
    """Find the tags in the file contents."""
    TAGS_INDEX: int = 1
    line_tags: List[str]
    tags: Set[FrozenSet[str]] = set()
    line: str
    tags_string: str
    power_set_tags: Set[FrozenSet[str]] = []

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

    # Create and return the power set.
    return tags


def main() -> None:
    """Get the tags from the file data."""
    file_contents: List[str] = read_file()
    tags: Set[FrozenSet[str]] = get_tags(file_contents)
    print(tags)

main()
