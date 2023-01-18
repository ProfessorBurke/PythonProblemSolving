# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:25:45 2023

@author: Maggie
Source: Michael Clark et al (2022). Estimating the environmental impacts of 57,000 food products. PNAS.
Retrieved from https://ourworldindata.org/explorers/food-footprints?facet=none&uniformYAxis=0&Commodity+or+Specific+Food+Product=Specific+food+products&Environmental+Impact=Carbon+footprint&Kilogram+%2F+Protein+%2F+Calories=Per+kilogram&By+stage+of+supply+chain=false&country=Beef+%28beef+herd%29~Lamb+%26+Mutton~Beef+%28dairy+herd%29~Prawns+%28farmed%29~Cheese~Pig+Meat~Poultry+Meat~Eggs~Rice~Tofu+%28soybeans%29~Milk~Tomatoes~Maize~Wheat+%26+Rye~Peas~Bananas~Potatoes~Nuts~Almonds~Avocados~Beef+burger~Cow%27s+milk~Dairy-free+ice+cream~Lentils~Vegan+pizza~Almond+milk~Bread~Meat+pizza~Vegetable+lasagne~Macaroni+cheese~Coconut+milk~Beans
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

food_footprints = pd.read_csv("food-footprints.csv")

greenhouse = food_footprints[["Emissions per kilogram",
                              "Entity"]]
foods = ["Beef burger", "Macaroni cheese", "Meat pizza", 
                  "Eggs", "Rice", "Cow's milk", "Vegetable lasagne", 
                  "Coconut milk", "Lentils", "Dairy-free ice cream", 
                  "Tomatoes", "Vegan pizza", "Beans", "Avocados", 
                  "Bread", "Bananas", "Almond milk", "Almonds", "Potatoes"]

foods_rows = greenhouse[greenhouse["Entity"].isin(foods)]

sorted_rows = foods_rows.sort_values(by="Emissions per kilogram")

fig, ax = plt.subplots()
hbars = ax.barh(sorted_rows["Entity"], sorted_rows["Emissions per kilogram"],
        color = mcolors.TABLEAU_COLORS)

plt.bar_label(hbars, fmt = "%.2f")
ax.set_title("Greenhouse gas emissions per kilogram of food")
ax.axis((0, 60, -2, 20))
ax.set_xticks([0, 10, 20, 30, 40, 50], labels = ["0kg", "10kg", "20kg",
                                                 "30kg", "40kg", "50kg"])
