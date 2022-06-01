"""Tidy a directory of social media user data."""

import typing
import pathlib

def replace_missing(data: str) -> str:
    """Return NA if value passed is a dash."""
    result: str = data
    if data == "-":
        result = "NA"
    return result

def tidy_file(raw_file_name: str, output_file_name: str) -> None:
    """Tidy raw_file lines and append to output_file."""

    user_id: str
    followers_str: str
    updates_str: str
    raw_social_file: typing.TextIO
    tidy_social_file: typing.TextIO

    # Open and read the input file.
    raw_social_file = open(raw_file_name)
    user_id = raw_social_file.readline()

    # Open the output file.
    tidy_social_file = open(output_file_name, "a")

    # Tidy input file and output to tidy file.
    while user_id != "":
        followers_str = raw_social_file.readline().strip()
        updates_str = raw_social_file.readline().strip()
        updates_str = replace_missing(updates_str)
        followers_str = replace_missing(followers_str)
        tidy_social_file.write(user_id.strip() + "," + followers_str +
                               "," + updates_str + "\n")
        user_id = raw_social_file.readline()

    # Close the files.
    tidy_social_file.close()
    raw_social_file.close()


def main() -> None:
    """Tidy files into one tidy output file."""
    current: pathlib.Path
    filepath: pathlib.Path
    
    current = pathlib.Path("social")
    for filepath in current.iterdir():
        tidy_file(filepath, "social_tidy.csv")
    
main()
