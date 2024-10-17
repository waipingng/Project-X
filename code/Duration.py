import pandas as pd
import re

# Function to convert ISO 8601 duration (PTxHyM) to total minutes
def parse_duration(duration):
    # Use regex to extract hours and minutes
    match = re.match(r'PT(\d+)H(\d+)M', duration)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        return hours * 60 + minutes  # Convert to total minutes
    return 0

# Function to categorize movie length
def categorize_length(total_minutes):
    if total_minutes <= 60:
        return 'short'
    elif total_minutes <= 90:
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