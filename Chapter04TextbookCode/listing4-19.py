"""Tidy a file of social media user data
   and calculate updates average."""

import typing

# Initialize the total and count.
total_updates: int = 0
count: int = 0
user_id: str
followers_str: str
updates_str: str
raw_social_file: typing.TextIO
tidy_social_file: typing.TextIO

# Open and read the input file.
raw_social_file = open("social.txt")
user_id = raw_social_file.readline()

# Open the output file.
tidy_social_file = open("social_tidy.csv", "w")

# Tidy input file and output to tidy file.
while user_id != "":
    followers_str = raw_social_file.readline().strip()
    updates_str = raw_social_file.readline().strip()
    if updates_str == "-":
        updates_str = "NA"
    else:
        count += 1
        total_updates += int(updates_str)
    if followers_str == "-":
        followers_str = "NA"
    tidy_social_file.write(user_id.strip() + "," + followers_str +
                           "," + updates_str + "\n")
    user_id = raw_social_file.readline()

tidy_social_file.close()
raw_social_file.close()
    
# If we found any updates, average them
if count != 0:
    print("The average number of updates is {:.1f}."
          .format(total_updates / count))
else:
    print("There were no updates in the file.")
