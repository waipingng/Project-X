import pandas as pd
import re
import os  # To handle directories

# Step 1: Load the CSV file
df = pd.read_csv('artifacts/movies.csv')

# Step 2: Clean the genres by removing unwanted characters and convert to lowercase
df['genre'] = df['genre'].str.split(',').apply(lambda x: [re.sub(r"[\'\]\[]", '', genre.strip().lower()) for genre in x])

# Step 3: Explode the DataFrame so each genre has its own row
df_exploded = df.explode('genre')

# Step 4: Group by genre and calculate the average rating
genre_avg_rating_df = df_exploded.groupby('genre')['rating'].mean().reset_index()

# Step 5: Sort the DataFrame by average rating in descending order
genre_avg_rating_df = genre_avg_rating_df.sort_values(by='rating', ascending=False)

# Step 6: Ensure the 'artifacts' directory exists
artifacts_dir = 'artifacts'
if not os.path.exists(artifacts_dir):
    os.makedirs(artifacts_dir)

# Step 7: Save the cleaned and sorted DataFrame to a new CSV file with absolute path
output_path = os.path.join(artifacts_dir, 'genre_avg_rating.csv')
genre_avg_rating_df.to_csv(output_path, index=False)

print(f"Average rating for each genre saved to {output_path} in descending order.")
