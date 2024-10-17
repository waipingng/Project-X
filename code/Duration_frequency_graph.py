import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

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

# Step 3: Group by movie length and analyze ratings
grouped = df.groupby('movie_length')['rating']

# Calculate summary statistics for each group
summary_stats = grouped.describe()

# Step 4: Save the summary statistics as a CSV file in the artifacts folder
summary_stats.to_csv('artifacts/movie_length_rating_summary.csv')

print("Rating summary saved to artifacts/movie_length_rating_summary.csv.")

# Step 5: Plot the rating distribution for each movie length category (Box plot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='movie_length', y='rating', data=df)
plt.title('Rating Distribution by Movie Length (Box Plot)')
plt.savefig('artifacts/rating_distribution_by_length_boxplot.png')
plt.show()

# Step 6: Plot the rating distribution for each movie length category (Histograms)
plt.figure(figsize=(12, 6))
sns.histplot(df[df['movie_length'] == 'short']['rating'], bins=10, kde=True, color='blue', label='Short', stat='density', element='step')
sns.histplot(df[df['movie_length'] == 'medium']['rating'], bins=10, kde=True, color='green', label='Medium', stat='density', element='step')
sns.histplot(df[df['movie_length'] == 'long']['rating'], bins=10, kde=True, color='red', label='Long', stat='density', element='step')
plt.title('Rating Distribution by Movie Length (Histograms)')
plt.xlabel('Rating')
plt.ylabel('Density')
plt.legend()
plt.savefig('artifacts/rating_distribution_by_length_histogram.png')
plt.show()

# Step 7: Plot the rating distribution using Kernel Density Estimation (KDE Plot)
plt.figure(figsize=(12, 6))
sns.kdeplot(df[df['movie_length'] == 'short']['rating'], color='blue', label='Short', fill=True)
sns.kdeplot(df[df['movie_length'] == 'medium']['rating'], color='green', label='Medium', fill=True)
sns.kdeplot(df[df['movie_length'] == 'long']['rating'], color='red', label='Long', fill=True)
plt.title('Rating Distribution by Movie Length (KDE Plot)')
plt.xlabel('Rating')
plt.ylabel('Density')
plt.legend()
plt.savefig('artifacts/rating_distribution_by_length_kde.png')
plt.show()
