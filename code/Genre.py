import pandas as pd
from collections import Counter
import re
import os  # To handle directories

# Step 1: Load the CSV file
df = pd.read_csv('artifacts/movies.csv')

# Step 2: Clean the genres by removing unwanted characters and convert to lowercase
all_genres = df['genre'].str.split(',').explode().str.strip().str.lower()

# Step 3: Use regex to remove any extra characters like quotes or brackets
all_genres = all_genres.apply(lambda x: re.sub(r"[\'\]\[]", '', x))

# Step 4: Count the frequency of each genre
genre_count = Counter(all_genres)

# Step 5: Convert the genre count to a DataFrame
genre_freq_df = pd.DataFrame(genre_count.items(), columns=['genre', 'frequency'])

# Step 6: Sort the DataFrame by frequency in descending order
genre_freq_df = genre_freq_df.sort_values(by='frequency', ascending=False)

# Step 7: Ensure the 'artifacts' directory exists
artifacts_dir = 'artifacts'
if not os.path.exists(artifacts_dir):
    os.makedirs(artifacts_dir)

# Step 8: Save the cleaned and sorted DataFrame to a new CSV file with absolute path
output_path = os.path.join(artifacts_dir, 'genre_frequency.csv')
genre_freq_df.to_csv(output_path, index=False)

print(f"Cleaned genre frequency saved to {output_path} in descending order.")