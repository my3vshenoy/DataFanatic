## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

## 2. Mean ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

columns = ["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]
user_reviews = movie_reviews[columns]
user_reviews_means = user_reviews.apply(calc_mean)

rt_mean = user_reviews_means["RT_user_norm"]
mc_mean = user_reviews_means["Metacritic_user_nom"]
fg_mean = user_reviews_means["Fandango_Ratingvalue"]
id_mean = user_reviews_means["IMDB_norm"]

print("Rotten Tomatoes (mean):", rt_mean)
print("Metacritic (mean):", mc_mean)
print("Fandango (mean):",fg_mean)
print("IMDB (mean):",id_mean)

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean


def calc_variance(series):
    variance = 0
    sq_deviations = (series - calc_mean(series))**2
    #variance = 
    return calc_mean(sq_deviations)

def calc_std_dev(series):
    std_dev = calc_variance(series) ** (1/2)
    return std_dev

columns = ["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]

user_variance =  movie_reviews[columns].apply(calc_variance)
user_std_dev =  movie_reviews[columns].apply(calc_std_dev)

rt_var = user_variance["RT_user_norm"]
rt_stdev = user_std_dev["RT_user_norm"]

mc_var = user_variance["Metacritic_user_nom"]
mc_stdev = user_std_dev["Metacritic_user_nom"]

fg_var = user_variance["Fandango_Ratingvalue"]
fg_stdev = user_std_dev["Fandango_Ratingvalue"]

id_var = user_variance["IMDB_norm"]
id_stdev = user_std_dev["IMDB_norm"]

print("RT Variance:",rt_var)
print("RT Std Dev:",rt_stdev)

print("MC Variance:",mc_var)
print("MC Std Dev:",mc_stdev)

print("Fandango Variance:",fg_var)
print("Fandango Std Dev:",fg_stdev)

print("IMDB Variance:",id_var)
print("IMDB Std Dev:",id_stdev)



## 4. Scatter plots ##

from matplotlib import pyplot as plt
fig = plt.figure(figsize = (4, 8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0, 5.0)
ax2.set_xlim(0, 5.0)
ax3.set_xlim(0, 5.0)

ax1.scatter(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
ax2.scatter(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
ax3.scatter(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(series_1, series_2):
    x = series_1.values
    y = series_2.values
    x_mean = calc_mean(series_1)
    y_mean = calc_mean(series_2)
    x_diff = [i - x_mean for i in x]
    y_diff = [i - y_mean for i in y]
    covariance = [(x_diff[i]*y_diff[i]) for i in range(len(x))]
    return sum(covariance)/len(covariance)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Covariance between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Covariance between Metacritic and Fandango", mc_fg_covar)
print("Covariance between IMDB and Fandango", id_fg_covar)
    



## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(series_1, series_2):
    covariance = calc_covariance(series_1, series_2)
    x_std_dev =  calc_variance(series_1) ** (1/2)
    y_std_dev =  calc_variance(series_2) ** (1/2)
    correlation = covariance / (x_std_dev*y_std_dev)
    return correlation
    
#Calculate Covariance
rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

#Calculate Correlation
rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango", rt_fg_corr)
print("Correlation between Metacritic and Fandango", mc_fg_corr)
print("Correlation between IMDB and Fandango", id_fg_corr)