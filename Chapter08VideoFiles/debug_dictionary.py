"""
    Manipulating a dict in Python.
"""

##scores = {1:[], 2:["women", "cabin"],
##          3:["sable", "worth"], 4:["pixie"],
##          5:[], 6:[]}
##scores[3].append("spire")

def show_scores(scores: dict[list]) -> None:
    """Display the player's scores."""
    key: int
    value: list
    for key, value in scores.items():
        print("{}: {}".format(key, len(value)))
        

empty_scores = {1:[], 2:[],
          3:[], 4:[],
          5:[], 6:[]}
### Bad code!  This doesn't copy the dictionary.
##scores_Isaiah = empty_scores
##scores_Renata = empty_scores

scores_Isaiah = empty_scores.copy()
scores_Renata = empty_scores.copy()

scores_Renata[3].append("women")
scores_Renata[4].append("cabin")

scores_Isaiah[5].append("women")
scores_Isaiah[5].append("cabin")

show_scores(scores_Renata)
print()
show_scores(scores_Isaiah)














