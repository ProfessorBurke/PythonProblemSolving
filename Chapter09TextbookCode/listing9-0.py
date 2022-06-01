# -*- coding: utf-8 -*-
"""
Combine death rate for pneumonia and influenza with health insurance by state to 
look for a correlation.

@author: Maggie
"""
# Import data analytics libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Import our data sets
illness_data = pd.read_csv("flu_mortality.csv")
healthcare = pd.read_csv("healthcare.csv")

# Narrow this down to 2016 and combine the tables
flu_2016 = illness_data.loc[illness_data.YEAR == 2016]
data_2016_merged = pd.merge(flu_2016, healthcare, on="STATE")

# Plot the death rate vs. insurance rate
mpl.style.use("seaborn")
mpl.style.use("seaborn-colorblind")
fig, ax = plt.subplots()
ax.scatter(data_2016_merged.RATE, data_2016_merged.PERC_2016)
ax.set_title("Insurance Percent vs. Flu and Pneumonia Death Rates")
ax.set_xlabel("Flu and Pneumonia Death Rate")
ax.set_ylabel("Percentage Insured")

# Add a regression line
x = data_2016_merged.RATE
m, b = np.polyfit(data_2016_merged.RATE, data_2016_merged.PERC_2016, 1)
ax.plot(x, m*x+b)

