## 1. Data Structures ##

import pandas as pd

#Read the csv file to create a dataframe
fandango = pd.read_csv("fandango_score_comparison.csv")

#use the .head() method to print the first two rows.
print(fandango.head(2))

## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')

#Select the FILM column, assign it to the variable series_film, and print the first five values.
series_film = fandango["FILM"]
print(series_film[0:5])

#select the RottenTomatoes column, assign it to the variable series_rt, and print the first five values.
series_rt = fandango["RottenTomatoes"]
print(series_rt[0:5])

## 3. Custom Indexes ##

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
#Create a new Series object named series_custom that has a string index (based on the values from film_names), and contains all of the Rotten Tomatoes scores from series_rt
series_custom = Series(rt_scores, index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

## 4. Integer Index Preservation ##

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
#Assign the values in series_custom at indexes 5 through 10 to the variable fiveten
fiveten = series_custom[5:11]
print(fiveten)


## 5. Reindexing ##

original_index = series_custom.index
x = sorted(original_index)
sorted_by_index = series_custom.reindex(x)

## 6. Sorting ##

#Sort series_custom by index using sort_index(), and assign the result to the variable sc2.
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()

print(sc2[0:11])
print(sc3[0:11])


## 7. Transforming Columns With Vectorized Operations ##

#Normalize series_custom (which is currently on a 0 to 100-point scale) to a 0 to 5-point scale by dividing each value by 20.
series_normalized = series_custom/20

## 8. Comparing and Filtering ##

criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

rt_mean = (rt_critics + rt_users)/2

print(rt_mean)