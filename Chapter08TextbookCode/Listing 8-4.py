"""Sort by inner dictionary length."""

from typing import Dict, List

# Annotate and initialize variables.
volunteers: Dict[str, Dict[str, int]] = {"Omer":
                                         {"1/2/21": 6},
                                         "Anna":
                                         {"1/3/21": 10,
                                          "1/5/21": 2}}
# Sort the dictionary by number of days volunteered.
print(sorted(volunteers, key = lambda k: len(volunteers[k])))
