"""Analyze video channel data."""

from typing import List, TextIO

def read_file() -> List[str]:
    """Return a list of the lines in the file."""
    # to-do:  take file name as parameter, confirm it exists
    channel_file: TextIO = open("channel_data.txt")
    file_data: List[str] = channel_file.readlines()
    return file_data

def get_tags(file_contents: List[str]) -> List[str]:
    """Find the tags in the file contents."""
    TAGS_INDEX: int = 1
    tags: List[str] = []
    line: str
    line_list: List[str]
    tags_string: str
    tags_list: List[str]
    for line in file_contents:
        # Separate each line in the file into pieces.
        line_list = line.split(",")
        # Pull the tags piece out of the line, then
        # pull the tags out of that; ignore blank first tag.
        tags_string = line_list[TAGS_INDEX]
        tags_list = tags_string.split("#")
        # For each tag, if it's not already in tags, add it.
        for tag in tags_list[1:]:
            if not tag in tags:
                tags.append(tag)
    return tags


def main() -> None:
    """Get the tags from the file data."""
    file_contents: List[str] = read_file()
    tags: List[str] = get_tags(file_contents)
    print(tags)

main()
