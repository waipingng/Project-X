import pandas as pd
from collections import Counter

# Step 1: Load the CSV file
df = pd.read_csv('movies.csv')

# Step 2: Split the genres column, remove spaces, and convert to lowercase
all_genres = df['genre'].str.split(',').explode().str.strip().str.lower()

# Step 3: Count the frequency of each genre
genre_count = Counter(all_genres)

# Step 4: Convert the genre count to a DataFrame
genre_freq_df = pd.DataFrame(genre_count.items(), columns=['genre', 'frequency'])

# Step 5: Sort the DataFrame by frequency in descending order
genre_freq_df = genre_freq_df.sort_values(by='frequency', ascending=False)

# Step 6: Save the cleaned and sorted DataFrame to a new CSV file
genre_freq_df.to_csv('artifacts/genre_frequency.csv', index=False)

print("Cleaned genre frequency saved to artifacts/genre_frequency.csv in descending order.")