import pandas as pd
import re

# Improved function to parse movie duration and handle different formats
def parse_duration(duration):
    match = re.match(r'(\d+)h(\d+)m', duration)  # "XhYm"
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        return hours * 60 + minutes
    match = re.match(r'(\d+)h', duration)  # "Xh"
    if match:
        hours = int(match.group(1))
        return hours * 60
    match = re.match(r'(\d+)m', duration)  # "Xm"
    if match:
        minutes = int(match.group(1))
        return minutes
    return 0  # Return 0 if the format doesn't match any pattern

# Function to categorize movie length
def categorize_length(total_minutes):
    if total_minutes <= 90:
        return 'short'
    elif 90 < total_minutes <= 150:
        return 'medium'
    else:
        return 'long'

# Step 1: Load the CSV file
df = pd.read_csv('artifacts/movies.csv')

# Step 2: Parse the duration column and categorize movie length
df['total_minutes'] = df['duration'].apply(parse_duration)
df['movie_length'] = df['total_minutes'].apply(categorize_length)

# Step 3: Count the frequency of each category
length_count = df['movie_length'].value_counts().reset_index()
length_count.columns = ['movie length', 'frequency']

# Step 4: Save the result as a CSV file in the artifacts folder
length_count.to_csv('artifacts/movie_length.csv', index=False)

print("Movie length categories saved to artifacts/movie_length.csv.")

