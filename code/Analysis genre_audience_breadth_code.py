# use python code and use movies.csv file we have scraped from the website to get the new csv file which can show the relationship between the genre and its breadth of a movie’s audience .
#now use the content rating to represent the the breadth of a movie’s audience
import pandas as pd  
import json  

# step1: extract the dataframe from the json file , then create the CSV file with specified columns
with open('imdb_top_movies.json', 'r') as f:
    data = json.load(f) 
df = pd.DataFrame(data)
df.to_csv('artifacts/moviesnew.csv', index=False, columns=['title', 'url', 'rating', 'rating_count', 'description', 'genre', 'content_rating', 'duration'])

# step 2: Read CSV file into a DataFrame
df = pd.read_csv('moviesnew.csv')
new_genres = []  
# step3: create the new genres list
for index, row in df.iterrows():
    genres = row['genre'].split(', ')  
    for genre in genres: 
        new_genres.append({'new_genre': genre.strip(), 'content_rating': row['content_rating']})
new_genres_df = pd.DataFrame(new_genres)
 
# step4: Group by 'new_genre' and 'content_rating'
count_df = new_genres_df.groupby(['new_genre', 'content_rating']).size().unstack(fill_value=0)

# step5: Calculate the total counts of content rating of each new genre
total_counts = count_df.sum(axis=1)

# step6: Calculate the proportion of each content rating of each new genre
probability_df = count_df.div(total_counts, axis=0)

# step7: create the new dataframe and save it to the new csv file
probability_df.columns.name = None  
probability_df.reset_index(inplace=True)
probability_df.rename(columns={'index': 'new_genre'}, inplace=True)
probability_df.to_csv('artifacts/genre_audience_breadth.csv', index=False)






