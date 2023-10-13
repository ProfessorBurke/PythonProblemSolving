"""
    Demonstrate processign records of data stored
    in parallel lists.
"""

# Annotate the three lists.
sample_ids: list[str]
species_ids: list[str]
carbon: list[float]

# Annotate and initialize total, count,
#and average for statistics, plus a loop control variable.
total_carbon: float = 0.0
count_oak: int = 0
average_carbon: float
i: int

# Initialize the lists to the first five values
# in the data.
sample_ids = ["92BHIS10BW1","92BHIS10BW2","92BHIS10BW3","92BHIS10WO1","92BHIS10WO2"]
species_ids = ["TIAM","TIAM","TIAM","QUAL","QUAL"]
carbon = [47.13, 47.72, 46.62, 49.42, 49.33]

# What is the average percent carbon for White Oaks?
# Calculate and report.
for i in range(len(sample_ids)):
    if species_ids[i] == "QUAL":
        total_carbon += carbon[i]
        count_oak += 1
if count_oak != 0:
    average_carbon = total_carbon / count_oak
    print("The average carbon percent of dry weight for White Oak is {:.2f}."
          .format(average_carbon))
else:
    print("There were no White Oak readings in the sample.")


