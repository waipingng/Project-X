# use python code and use movies.csv file we have scraped from the website to get the new csv file which can show the relationship between the genre and its breadth of a movie’s audience .
#now use the content rating to represent the the breadth of a movie’s audience
import pandas as pd  
import json  

# Step 1: Extract the DataFrame from the JSON file and create the CSV file with specified columns
def extract_and_save_json_to_csv(json_file, csv_file, columns):
    with open(json_file, 'r') as f:
        data = json.load(f) 
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False, columns=columns)

# Step 2: Read the CSV file into a DataFrame
def read_csv_to_dataframe(csv_file):
    return pd.read_csv(csv_file)

# Step 3: Function to create a new genres list from the DataFrame
def create_new_genres_list(df):
    new_genres = []  
    for index, row in df.iterrows():
        genres = row['genre'].split(', ')  
        for genre in genres: 
            new_genres.append({'new_genre': genre.strip(), 'content_rating': row['content_rating']})
    return pd.DataFrame(new_genres) 

# Step 4: Function to group by 'new_genre' and 'content_rating'
def group_by_genre_and_rating(new_genres_df):
    return new_genres_df.groupby(['new_genre', 'content_rating']).size().unstack(fill_value=0)

# Step 5: Function to calculate total counts of content ratings for each new genre
def calculate_total_counts(count_df):
    return count_df.sum(axis=1)

# Step 6: Function to calculate the proportions of each content rating for each new genre
def calculate_proportions(count_df, total_counts):
    return count_df.div(total_counts, axis=0)

# Step 7: Function to create a new DataFrame and save it to a new CSV file
def save_probability_df_to_csv(probability_df, csv_file):
    probability_df.columns.name = None  
    probability_df.reset_index(inplace=True)
    probability_df.rename(columns={'index': 'new_genre'}, inplace=True)
    probability_df.to_csv(csv_file, index=False)

# Main process
json_file = 'imdb_top_movies.json'
csv_file = 'artifacts/moviesnew.csv'
columns = ['title', 'url', 'rating', 'rating_count', 'description', 'genre', 'content_rating', 'duration']

# Execute functions in order
extract_and_save_json_to_csv(json_file, csv_file, columns)

#perform my analysis 
df = read_csv_to_dataframe(csv_file)
new_genres_df = create_new_genres_list(df)
count_df = group_by_genre_and_rating(new_genres_df)
total_counts = calculate_total_counts(count_df)
probability_df = calculate_proportions(count_df, total_counts)
save_probability_df_to_csv(probability_df, 'artifacts/genre_audience_breadth.csv')

