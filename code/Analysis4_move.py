# We are building a Python program to clean and analyze IMDb data scraped from the top 250 movies, focusing on box office performance and awards, to determine if there is any correlation between the two. Below are the steps you need to follow to write the program for cleaning and analyzing the data, along with code explanations.

#Steps to clean data

import pandas as pd
import datetime

# Load the scraped data from a CSV file or JSON
def load_data(file_path):
    """Load the scraped data into a pandas DataFrame."""
    return pd.read_csv(file_path)

# Clean and filter relevant data columns
def clean_data(df):
    """Clean the data by dropping NaN values and formatting columns."""
    # Drop rows with missing Box Office or Awards data
    df = df.dropna(subset=['BoxOffice', 'Awards'])

    # Convert Box Office to numeric value, remove currency symbols, and handle millions/billions
    df['BoxOffice'] = df['BoxOffice'].replace({'\$':'', ',':''}, regex=True).astype(float)

    # Split Awards into Won and Nominated, calculate total
    df['AwardsWon'] = df['Awards'].apply(lambda x: int(x.split('win')[0].strip()) if 'win' in x else 0)
    df['AwardsNominated'] = df['Awards'].apply(lambda x: int(x.split('nomination')[0].strip()) if 'nomination' in x else 0)
    df['TotalAwards'] = df['AwardsWon'] + df['AwardsNominated']
    
    return df

# Load the data
data = load_data('imdb_top250.csv')
cleaned_data = clean_data(data)
