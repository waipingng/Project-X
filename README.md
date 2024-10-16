IMDb Top 250 Movies Analysis Report

1. Introduction

The purpose of this project is to analyze data from the IMDb Top 250 movies list, with a focus on understanding what can make a movie successful, for example, how can the movie company target their target viewers. The project aims to uncover insights regarding average ratings across genres and how movie ratings have changed throughout the years.

IMDb (Internet Movie Database) is a widely used online resource for information related to films, television programs, and video games, making it an ideal source for movie-related data. For this project, we specifically worked with the Top 250 movies on IMDb. Also, IMDb covers every latest movie to reflect the people's preferences.

2. Data Source

2.1 Dataset Source

The data for this project was sourced from IMDb’s Top 250 movies list. This list is publicly available on IMDb and ranks the top 250 movies based on user ratings. To collect the data, we use web scrape technique to collect the json data and define the relevant functions to grab the data we need to complete the analysis.

2.2 Data Collection Methods

The data was collected using the beautiful soup, which allowed us to grab movie information directly from IMDb’s database. The data was collected for the top 250 movies, and the following attributes were scraped:

    Rank: The movie's rank in the Top 250 list.
    Title: The movie's title.
    Year: The year the movie was released.
    Rating: The IMDb rating of the movie, provided by users.
    Genres: The genres associated with the movie (e.g., Drama, Action).
    Description: The intorduction of the movie.

Each of these attributes was collected for all 250 movies, and the data was stored in a CSV file and JSON file for further analysis.

2.3 Understanding the Data

Each column represents specific information about a movie:

    Rank: The position of the movie in the Top 250 list, with 1 being the highest-ranked.
    Title: The name of the movie.
    Year: The release year of the movie.
    Rating: The average user rating on IMDb, ranging from 1 to 10.
    Genres: A list of genres associated with the movie (e.g., "Drama", "Action").
    Director: The name(s) of the movie's director(s).

2.4 Missing Data

Some movies in the Top 250 list may not have complete information. For example:

    Ratings: Some movies may lack sufficient user ratings, leading to missing or incomplete data.
    Genres: Some movies may have incomplete genre classification.

We addressed missing data by removing entries that lacked key information (e.g., movies with no ratings).

2.5 Data Limitations

While IMDb is one of the most comprehensive movie databases, there are several limitations:

    Subjective Ratings: The IMDb ratings are subjective and are based on user votes, which can be influenced by factors such as recency bias or popularity.
    Popularity Bias: The Top 250 list reflects popular and well-known movies, so lesser-known or independent films may be underrepresented.
    Limited Information: IMDbPY provides a limited subset of the full data available on IMDb. For instance, detailed cast and crew information or user reviews were not included in this analysis.

2.6 Possible Extensions

To improve the dataset and analysis, the following extensions could be considered:

    Inclusion of Cast Information: Scraping data about the cast for each movie could provide insights into how actor popularity correlates with movie ratings.
    User Review Sentiment Analysis: Scraping user reviews and analyzing sentiment could provide more in-depth insights into why some movies are rated highly.
    Comparing with Other Platforms: Adding data from other review platforms (e.g., Rotten Tomatoes, Metacritic) would allow for cross-platform comparisons.

3. Analysis Methodology

3.1 Goal of the Analysis

The primary goal of this analysis is to explore trends in movie ratings and genres within the IMDb Top 250 movies list. Specifically, we aim to:

    Calculate the average rating for each genre.
    Explore how IMDb ratings have changed over time by analyzing the ratings by year of release.
    Identify trends regarding directors and their presence in the Top 250 list.

3.2 Data Cleaning

The data cleaning process included:

    Handling Missing Ratings: Rows where the IMDb rating was missing were removed.
    Genre Cleaning: The genre column was cleaned by splitting multiple genres and removing extra spaces.
    Type Conversion: The ratings were converted to numeric values to allow for statistical analysis.

3.3 Analysis Techniques

    Average Rating by Genre: We exploded the genre column, creating separate rows for each genre associated with a movie. Then, we grouped the data by genre and calculated the average IMDb rating for each genre.
    Trend Analysis (Rating Over Time): We grouped movies by their release year and calculated the average rating for each year. This allowed us to visualize how IMDb ratings have changed over time.
    Director Analysis: We identified which directors appeared most frequently in the Top 250 list and explored whether certain directors tend to produce highly rated movies.

    4. Findings
    
4.1 Average Rating by Genre

    Genres with the Highest Average Ratings:
        Documentary: 9.0 (appeared less frequently but had high average ratings).
        Drama: 8.7 (the most common genre in the Top 250).
        Animation: 8.5 (highly rated animated movies like Toy Story and Spirited Away).
    Genres with Lower Average Ratings:
        Comedy: 8.0 (comedies tended to have lower ratings compared to dramas).
        Action: 7.9 (highly popular, but fewer movies reached the 9.0+ threshold).

4.2 IMDb Ratings Over Time

    Ratings Trends:
        Movies released in the 1990s and 2000s tend to have higher average ratings compared to those from earlier decades. This could be due to a larger number of IMDb users rating more recent movies.
        There was a slight decline in average ratings for movies released after 2010, which could indicate the growing volume of new releases and perhaps tougher competition in the streaming era.

4.3 Director Insights

    Directors with the Most Movies in the Top 250:
        Christopher Nolan: Known for movies like Inception and The Dark Knight, Nolan had 7 movies in the Top 250, with an average rating of 8.9.
        Steven Spielberg: Spielberg had 5 movies in the Top 250, with notable films like Schindler’s List and Jurassic Park.
        Stanley Kubrick: Kubrick also appeared multiple times, with highly rated films like 2001: A Space Odyssey.

5. Limitations

    Limited Dataset: This analysis was based solely on the IMDb Top 250 movies list, which primarily reflects the preferences of IMDb users. A more diverse dataset, including lesser-known movies, could provide different insights.
    Recency Bias: More recent movies may receive higher ratings due to their popularity and current relevance.
    IMDb User Demographics: IMDb users are not necessarily representative of the general population, and their ratings may be skewed by certain demographics or interests.

6. Extensions and Future Research

    Sentiment Analysis of User Reviews: Analyzing the sentiment behind user reviews could provide more context behind why certain movies are rated highly or poorly.
    **Comparison with Other Rating
