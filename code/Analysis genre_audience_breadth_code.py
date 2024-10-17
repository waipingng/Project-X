# use python code and use movies.csv file we have scraped from the website to get the new csv file which can show the relationship between the genre and its breadth of a movie’s audience .
#now use the content rating to represent the the breadth of a movie’s audience
import pandas as pd


# Reading the CSV file from the 'artifacts' directory
df = pd.read_csv('artifacts/movies.csv')

new_genres = []

# Iterating through each row, splitting the 'genre' column, and creating new records
for index, row in df.iterrows():
    genres = row['genre'].split(', ')  
    for genre in genres:
        new_genres.append({'new_genre': genre.strip(), 'rating': row['rating'], 'content_rating': row['content_rating']})

# Creating a new DataFrame from the new genres data
new_genres_df = pd.DataFrame(new_genres)

# Grouping by 'new_genre' and 'content_rating' and counting occurrences
count_df = new_genres_df.groupby(['new_genre', 'content_rating']).size().unstack(fill_value=0)

# Calculating the total count for each 'new_genre'
total_counts = count_df.sum(axis=1)

# Calculating the proportion of each 'content_rating' within each 'new_genre'
probability_df = count_df.div(total_counts, axis=0)

# Resetting the index to flatten the table
probability_df.columns.name = None  
probability_df.reset_index(inplace=True)

# Saving the final DataFrame to a CSV file
count_df.to_csv('artifacts/genre_audience_breadth.csv', index=False)






