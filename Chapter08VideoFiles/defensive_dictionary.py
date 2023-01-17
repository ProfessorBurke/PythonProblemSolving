"""
    Example of using try/except around a dictionary access.
"""

scores = {}
try:
    print(scores[1])
except KeyError:
    print("Logging a KeyError.")
