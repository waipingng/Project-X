import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import json


df = pd.read_csv('movies.csv')

df.to_csv('movies.csv', index=False, columns=['title', 'url', 'rating', 'rating_count', 'description', 'genre', 'content_rating', 'duration'])


import statsmodels.api as sm
import re

# Sample dataset with ISO 8601 duration format
data = pd.DataFrame({
    'duration': ['PT2H22M', 'PT2H55M', 'PT2H32M', 'PT3H22M', 'PT1H36M', 'PT3H21M', 'PT3H15M', 'PT2H34M'],
    'rating': [7.5, 8.0, 6.5, 8.5, 7.0, 9.0, 6.0, 8.8],  # Sample ratings
    'rating_count': [1000, 5000, 800, 3000, 1500, 7000, 600, 6500]  # Sample rating counts
})

# Regular expression to extract hours and minutes from ISO 8601 format
duration_regex = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?')

# Function to convert ISO 8601 duration to total minutes
def convert_duration(duration):
    match = duration_regex.match(duration)
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    return hours * 60 + minutes

# Apply the conversion to the 'duration' column
data['duration_minutes'] = data['duration'].apply(convert_duration)

# Step 2: Create duration ranges (categorize the movie durations)
def categorize_duration(duration):
    if duration < 90:
        return 'Short (<90 mins)'
    elif 90 <= duration <= 120:
        return 'Medium (90-120 mins)'
    elif 120 < duration <= 150:
        return 'Long (120-150 mins)'
    else:
        return 'Very Long (>150 mins)'

data['duration_range'] = data['duration_minutes'].apply(categorize_duration)

# Step 3: Calculate the average rating and rating count for each duration range
grouped_data = data.groupby('duration_range').agg({
    'rating': 'mean',
    'rating_count': 'mean'
}).reset_index()

# Step 4: Visualize the impact of duration range on average rating
sns.barplot(data=grouped_data, x='duration_range', y='rating')
plt.title('Average Rating by Movie Duration Range')
plt.xlabel('Duration Range')
plt.ylabel('Average Rating')
plt.show()

# Step 5: Visualize the impact of duration range on average rating count
sns.barplot(data=grouped_data, x='duration_range', y='rating_count')
plt.title('Average Rating Count by Movie Duration Range')
plt.xlabel('Duration Range')
plt.ylabel('Average Rating Count')
plt.show()

# Step 6: Perform regression analysis for the impact of duration range on rating and rating count
# Convert the duration ranges to dummy variables for regression
data = pd.get_dummies(data, columns=['duration_range'], drop_first=True)

# Regression for duration range and rating
X_rating = data[['duration_range_Medium (90-120 mins)', 'duration_range_Long (120-150 mins)', 'duration_range_Very Long (>150 mins)']]
y_rating = data['rating']
X_rating = sm.add_constant(X_rating)

model_rating = sm.OLS(y_rating, X_rating).fit()
print("Impact of Duration Range on Rating:")
print(model_rating.summary())

# Regression for duration range and rating count
y_rating_count = data['rating_count']
X_rating_count = sm.add_constant(X_rating)

model_rating_count = sm.OLS(y_rating_count, X_rating_count).fit()
print("\nImpact of Duration Range on Rating Count:")
print(model_rating_count.summary())

plt.savefig('artifacts/average_rating_count_by_duration.png')
plt.close() 