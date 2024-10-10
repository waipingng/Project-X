def calculate_avg_rating_by_genre(movies_df):
    # Explode the 'Genres' column so that each genre gets its own row
    movies_genres_df = movies_df.explode('Genres')

    # Group by genre and calculate the average rating for each genre
    avg_rating_by_genre = movies_genres_df.groupby('Genres')['Rating'].mean().sort_values(ascending=False)

    print("Average Rating by Genre:")
    print(avg_rating_by_genre)
    return avg_rating_by_genre

# Run the function to calculate the average rating by genre
avg_rating_by_genre = calculate_avg_rating_by_genre(movies_df)