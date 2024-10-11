from imdb import Cinemagoer
import csv
import time


ia = Cinemagoer()
top_250_movies = ia.get_top250_movies()

def scrape_top_250_movies():
    try:
        with open('top_250_movies.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Rank", "Title", "Year", "Rating", "Genres", "Director", "Casts", "Budget", "Gross Worldwide"])

            for i, movie in enumerate(top_250_movies):
                try:
                    movie_id = movie.movieID
                    movie_details = ia.get_movie(movie_id)
                    title = movie_details['title']
                    year = movie_details['year']
                    rating = movie_details.get('rating', 'N/A')
                    genres = ', '.join(movie_details.get('genres', []))
                    director = ', '.join([str(d) for d in movie_details.get('director', [])])
                    casts_objects = movie_details.get("cast", [])
                    casts = [person['name'] for person in casts_objects]
                    cast_list = ', '.join(casts)


                    budget = movie_details.get('budget', 'N/A')
                    gross = movie_details.get('gross', {}).get('worldwide', 'N/A')
                    writer.writerow([i + 1, title, year, rating, genres, director, cast_list, budget, gross])

                except Exception as e:
                    print(f"Error processing movie {i + 1}: {e}")
                
                time.sleep(1)

        print("Top 250 movies saved to 'top_250_movies.csv'")
    
    except Exception as e:
        print(f"Error creating or writing to the file: {e}")
scrape_top_250_movies()

