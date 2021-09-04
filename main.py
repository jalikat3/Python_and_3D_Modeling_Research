import pandas as pd
import geopandas as gpd
import requests
import matplotlib.pyplot as plt

# covidHeatMap.py
# Jali Purcell
# Purpose: research how to turn data into a heatmap by combining
# data and a geodataframe for the shapes of countries
# 8/28/2021

# tutorial source: https://www.youtube.com/watch?v=cxLht5KN3pQ&t=1720s

# problem: when path is imported, not enough of the countries are imported over
# attempted fixes: importing new data, issues still arise

# GET DATA
path='https://news.google.com/covid19/map?hl=en-AU&gl=AU&ceid=AU%3Aen'
r = requests.get(path).text
data = pd.read_html(r)


# make a pandas data frame from the data
# print check
for data_cases in data:
    print(data_cases)

# SPECIFY WHICH COLUMNS TO USE
data_cases = data_cases[['Location', 'Total cases']]

# MAKE A DATA FRAME WITH SPECIFIED DATA
data_casesDF=pd.DataFrame(data_cases)

# print(data_casesDF) check

# MAKE A GEOPANDAS DATA FRAME WITH SHAPEFILE OF WORLD
world=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
print(world)

# FIND WHICH COUNTRIES ARE NAMED DIFFERENTLY, CHANGE THE NAMES AS NEEDED

#for items in data_cases['Location'].tolist():
#    world_data_list = world['name'].tolist()
#    if items in world_data_list:
#        pass
#    else:
#        print(items + " is not in the world list")

# RENAME NEEDED: UNITED STATES
world.replace('United States of America', 'United States', inplace = True)

# RENAME LOCATION TO NAME OF COLUMN IN WORLD
data_casesDF.rename(columns={'Location': 'name'}, inplace=True)

# MERGE THE TWO DATA FRAMES INTO ONE
combined=world.merge(data_casesDF, on = 'name')
combined.to_csv("combined.csv")

ax=combined.plot(column='Total cases',
                     cmap='coolwarm',
                     figsize=(15, 9),
                     k=3,
                     legend=True)
ax.set_title("Total coronavirus cases (in millions) per country")
ax.set_axis_off()

# print(combined) check

plt.show()