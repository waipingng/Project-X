# Distrubution of movie ratings across genres

# Awards vs box office performance
#"study whether the top 250 movies are teenager friendly enough, and different genre's movie's teenager friendly level"
#cal the average rate of different genera
#the proportion of the content-rating in  the different genera 
#divide in to group 
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
########### the probality of different genre's conten rating 

count_df = df.groupby(['genre', 'content_rating']).size().unstack(fill_value=0)


total_counts = count_df.sum(axis=1)


probability_df = count_df.div(total_counts, axis=0)


probability_df.columns.name = None  
probability_df.reset_index(inplace=True)  

probability_df.to_csv('genre_content_rating_probabilities.csv', index=False)
#
###### merge two csv
csv1 = pd.read_csv('average_ratings_by_genre.csv') 
csv2 = pd.read_csv('genre_content_rating_probabilities.csv')  

merged_df = pd.merge(csv1, csv2, on='genre')


sorted_df = merged_df.sort_values(by='average_rating', ascending=False)


sorted_df.to_csv('merge_genre_rating_ct_prob.csv', index=False)

####### redo 
#####average 
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

###########################the content rate by new genre##########
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

final_df.to_csv('contentrating_genre.csv', index=False)

################## content rate  by rate ############
df = pd.read_csv('movies.csv')

def classify_rating(rating):
    if 8.2 <= rating <= 8.4:
        return '8.2-8.4'
    elif rating == 8.5:
        return '8.5'
    elif 8.6 <= rating <= 8.7:
        return '8.6-8.7'
    elif 8.8 <= rating <= 8.9:
        return '8.8-8.9'
    elif 9.0 <= rating <= 9.3:
        return '9-9.3'
    else:
        return 'Other' 
df['rating_category'] = df['rating'].apply(classify_rating)

count_df = df.groupby(['rating_category', 'content_rating']).size().unstack(fill_value=0)

count_df.columns.name = None  
count_df.reset_index(inplace=True)

count_df.to_csv('new_counting_rating.csv', index=False)


# df['rating_category'] = df['rating'].apply(classify_rating)

# count_df = df.groupby(['rating_category', 'content_rating']).size().unstack(fill_value=0)

# total_counts = count_df.sum(axis=1)

# probability_df = count_df.div(total_counts, axis=0)

# probability_df.columns.name = None  
# probability_df.reset_index(inplace=True)

# probability_df.to_csv('content_rating_probabilities_by_rating_category.csv', index=False)
