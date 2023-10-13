"""
    Demonstrate processign records of data stored
    as record lists within a single list.
"""
# Annotate and initialize constants to access record fields.
SAMPLE_ID: int = 0
SPECIES_ID: int = 1
CARBON: int = 2

# Annotate the three list of records.
leaf_data: list[list[str, str, float]]

# Annotate and initialize total, count,
#and average for statistics, plus a loop control variable.
total_carbon: float = 0.0
count_oak: int = 0
average_carbon: float

# Initialize the list to hold the first five records.
leaf_data = [["92BHIS10BW1", "TIAM", 47.13],
             ["92BHIS10BW2", "TIAM", 47.72],
             ["92BHIS10BW3", "TIAM", 46.62],
             ["92BHIS10WO1", "QUAL", 49.42],
             ["92BHIS10WO2", "QUAL", 49.33]]

# What is the average percent carbon for White Oaks?
# Calculate and report.
for leaf_record in leaf_data:
    if leaf_record[SPECIES_ID] == "QUAL":
        total_carbon += leaf_record[CARBON]
        count_oak += 1
if count_oak != 0:
    average_carbon = total_carbon / count_oak
    print("The average carbon percent of dry weight for White Oak is {:.2f}."
          .format(average_carbon))
else:
    print("There were no White Oak readings in the sample.")


