from imdb import IMDb
import csv

def scrape_top_250_movies():
    # Initialize IMDbPY instance
    ia = IMDb()

    # Get the top 250 movies from IMDb
    top_250_movies = ia.get_top250_movies()

    # Open a CSV file to save the data
    with open('top_250_movies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Title", "Year", "Rating", "Genres", "Director"])

        # Loop through each movie and extract relevant details
        for i, movie in enumerate(top_250_movies):
            movie_id = movie.movieID
            movie_details = ia.get_movie(movie_id)

            # Extract details
            title = movie_details['title']
            year = movie_details['year']
            rating = movie_details.get('rating', 'N/A')
            genres = ', '.join(movie_details.get('genres', []))
            director = ', '.join([str(d) for d in movie_details.get('director', [])])

            # Write the movie details into the CSV file
            writer.writerow([i+1, title, year, rating, genres, director])

    print("Top 250 movies saved to 'top_250_movies.csv'")

# Run the function to scrape the movies and save them to a CSV file
scrape_top_250_movies()