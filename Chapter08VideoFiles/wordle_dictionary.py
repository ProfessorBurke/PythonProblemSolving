"""
    An example of how we'd use a dictionary to store the words
    associated with each wordle score.
"""
from collections import defaultdict

def main() -> None:
    scores: defaultdict = defaultdict(list)
    scores[4].append("sieve")
    print(scores)
    print(scores[4])
    print(scores[2])
    print(scores)

main()
