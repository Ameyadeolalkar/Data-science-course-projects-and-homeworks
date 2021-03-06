'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')
'''
print(movies)
'''
# check the number of rows and columns
movies.shape
# check the data type of each column
movies.dtypes
# calculate the average movie duration
movies.duration.mean()
# sort the DataFrame by duration to find the shortest and longest movies
movies.sort(['duration'])
# create a histogram of duration, choosing an "appropriate" number of bins
#movies.duration.plot(kind='hist',bins=30,title='histogram of duration')
#movies.duration.plot(kind='hist',bins=30,title='histogram of duration')
# use a box plot to display that same data
movies.duration.describe()
#movies.duration.plot(kind='box')
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()
# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar')
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.replace({'content_rating':{'NOT RATED':'UNRATED','APPROVED':'UNRATED','PASSED':'UNRATED','GP':'UNRATED'}})
# convert the following content ratings to "NC-17": X, TV-MA
movies.replace({'content_rating':{'X':'NC-17','TV-MA':'NC-17'}})
# count the number of missing values in each column
movies.isnull().sum()
# if there are missing values: examine them, then fill them in with "reasonable" values
movies.fillna(value='NA',inplace=True)
# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration > 200].star_rating.mean()
movies[movies.duration < 200].star_rating.mean()
# use a visualization to detect whether there is a relationship between duration and star rating
#movies[['star_rating','duration']].sort('duration').values
#movies.plot(kind='scatter', x='duration', y='star_rating', c='duration',colormap='Blues')
# calculate the average duration for each genre
#movies.groupby('genre').duration.agg('mean')
'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.groupby('content_rating').duration.mean().plot(kind='bar')
# determine the top rated movie (by star rating) for each genre
movies.groupby(['title','genre']).star_rating.agg('max')
# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
dupe_titles = movies[movies.title.duplicated()].title
movies[movies.title.isin(dupe_titles)]
# calculate the average star rating for each genre, but only include genres with at least 10 movies
movies.groupby('genre').star_rating.agg('mean')[movies.genre.value_counts()>=10]
'''
BONUS
'''

# Figure out something "interesting" using the actors data!
