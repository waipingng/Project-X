import pandas as pd

def clean_movie_data():
    # Load the scraped data into a pandas DataFrame
    movies_df = pd.read_csv('top_250_movies.csv')

    # Convert the 'Rating' column to numeric (some values may be 'N/A')
    movies_df['Rating'] = pd.to_numeric(movies_df['Rating'], errors='coerce')

    # Drop rows with missing ratings
    movies_df = movies_df.dropna(subset=['Rating'])

    # Clean up genres by stripping spaces
    movies_df['Genres'] = movies_df['Genres'].apply(lambda x: [genre.strip() for genre in x.split(',')])

    # Save the cleaned data back into a CSV file
    movies_df.to_csv('cleaned_top_250_movies.csv', index=False)

    return movies_df

# Run the function to clean the movie data
movies_df = clean_movie_data()
print(movies_df.head())