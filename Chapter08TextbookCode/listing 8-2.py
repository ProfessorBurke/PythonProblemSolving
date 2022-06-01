"""Display volunteering hours."""

from typing import Dict, List

# Annotate and initialize dictionary.
volunteers: Dict[str, List[int]] = {"Omer": [5, 2],
                                    "Anna": [10],
                                    "Liam": [1, 4, 6]}
# Iterate over dictionary and display sum of hours.
for key,value in volunteers.items():
    print("{} volunteered {} hours.".format(
        key, sum(value)))







