import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file containing the genre frequencies
genre_data = pd.read_csv('artifacts/genre_frequency.csv')

# Step 2: Sort the data by frequency and select the top 13 genres
top_genres = genre_data.sort_values(by='frequency', ascending=False).head(13)

# Step 3: Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(top_genres['genre'], top_genres['frequency'], color='blue')

# Step 4: Customize the plot
plt.title('Top 13 Movie Genre Categories by Frequency', fontsize=14)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Rotate the genre labels to be vertical for better readability
plt.xticks(rotation=90)

# Step 5: Save the plot as an image file
plt.tight_layout()
plt.savefig('artifacts/top_13_genre_plot.png')

# Step 6: Show the plot
plt.show()