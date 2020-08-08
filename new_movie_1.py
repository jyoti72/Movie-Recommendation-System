# Get the libraries

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# Data Importing and Preprocessing

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

# Discovery and Visualization

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
data=movieRatings.head(5)

# Taking One Instance from the dataset for Analysis

#starWarsRatings = movieRatings['Star Wars (1977)']
toystoryRatings = movieRatings['Toy Story (1995)']
#analysis_data=starWarsRatings.head(20)
analysis_data_toystory=toystoryRatings.head(20)


# Calculating Correlation

similarMovies = movieRatings.corrwith(toystoryRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
df.head(20)

# Analyzing the results

results_imilear_movies=similarMovies.sort_values(ascending=False)

# Data Transformation

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movieStats.head()

# Sorting datasets by a metric

popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

# Joining two Data frames

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df.head()

# Analyzing the results

df.sort_values(['similarity'], ascending=False)[:15]












