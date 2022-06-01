"""Query hours dictionary of dictionaries."""

from typing import Dict, List

# Annotate and initialize variables.
volunteers: Dict[str, Dict[str, int]] = {"Omer":
                                         {"1/2/21": 6,
                                          "1/4/21": 1,
                                          "1/6/21": 5},
                                         "Anna":
                                         {"1/3/21": 10,
                                          "1/5/21": 2}}
name: str
date: str
finished: bool = False

# Obtain query and return results until done.
name = input("Enter a name or 'done' when finished: ")
while name != "done":
    if name in volunteers:
        date = input("On what date? ")
        if date in volunteers[name]:
            print("{} worked {:d} hours on {}."
                  .format(name, volunteers[name][date], date))
        else:
            print("{} did not work on {}.".format(name, date))
    else:
        print("{} is not in the database.".format(name))
    name = input("Enter a name or 'done' when finished: ")







