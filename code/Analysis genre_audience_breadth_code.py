# use python code and use movies.csv file we have scraped from the website to get the new csv file which can show the relationship between the genre and its breadth of a movie’s audience .
#now use the content rating to represent the the breadth of a movie’s audience
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import json
with open('imdb_top_movies.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.to_csv('movies.csv', index=False, columns=['title', 'url', 'rating', 'rating_count', 'description', 'genre', 'content_rating', 'duration'])

df = pd.read_csv('movies.csv')

########### the average rate of the different genre 
average_ratings = df.groupby('genre')['rating'].mean().reset_index()

average_ratings.columns = ['genre', 'average_rating']

average_ratings.to_csv('average_ratings_by_genre.csv', index=False)

#######################################the average rate of the new genre
df = pd.read_csv('movies.csv')
new_genres = []

for index, row in df.iterrows():
    genres = row['genre'].split(', ')  
    for genre in genres:
        new_genres.append({'new_genre': genre, 'rating': row['rating']})

new_genres_df = pd.DataFrame(new_genres)

average_ratings = new_genres_df.groupby('new_genre')['rating'].mean().reset_index()

average_ratings.columns = ['new_genre', 'average_rating']

average_ratings.to_csv('average_ratings_by_new_genre.csv', index=False)

###########################the content rate by new genre###############
import pandas as pd


df = pd.read_csv('movies.csv')
new_genres = []

for index, row in df.iterrows():
    genres = row['genre'].split(', ')  
    for genre in genres:
        new_genres.append({'new_genre': genre.strip(), 'rating': row['rating'], 'content_rating': row['content_rating']})


new_genres_df = pd.DataFrame(new_genres)


average_ratings = new_genres_df.groupby('new_genre')['rating'].mean().reset_index()
average_ratings.columns = ['new_genre', 'average_rating']  


count_df = new_genres_df.groupby(['new_genre', 'content_rating']).size().unstack(fill_value=0)


total_counts = count_df.sum(axis=1)

probability_df = count_df.div(total_counts, axis=0)

probability_df.columns.name = None  
probability_df.reset_index(inplace=True)

final_df = pd.merge(average_ratings, probability_df, on='new_genre', how='outer')

final_df.to_csv('genre_audience_breadth.csv', index=False)





