IMDb Top 250 Movies Analysis Report: How can make movie last longer?

1. Introduction

IMDb (Internet Movie Database) is a widely used online resource for information related to films, television programs, making it an ideal source for movie-related data. For this project, we specifically worked with the Top 250 movies on IMDb. Also, IMDb covers every latest movie to reflect the people's preferences. So, we would like to discover what types of movie can get higher rating and what makes the movies keep attracting viewers' attention.

The purpose of this project is to analyze data from the IMDb Top 250 movies list, with a focus on understanding what can make a movie successful, for example, how can the movie company target their target viewers. The project aims to uncover insights regarding average ratings across genres and how movie ratings reflect people's preferences.

1.1 Instruction to rerun the file

a) Implement scrape_movie by python3 code/scrape_movies.csv: The function scrape_movie scrapes detailed information about a specific movie given its IMDb URL. The function extracts the movie title, year, runtime, rating, genre, description, director, cast, user reviews, budget, and worldwide gross.

b) Implement scrape_page by python3 code/common.py: The function scrape_page scrapes all the movie URLs from the IMDb Top 250 page. It returns a list of movie URLs that will later be used by the scrape_movies function.

c) Implement scrape.py by python3 code/scrape.py:Several functions are provided to extract specific information from the IMDb movie page and save to a csv file

d) implement common_word_ratings by python 3 code/common_word_ratings.csv: first by function def clean_description, we got clean words from the description and then compute correlation of word frequencies with ratings.

2. Data Source

2.1 Dataset Source

The data for this project was sourced from IMDb’s Top 250 movies list. This list is publicly available on IMDb and ranks the top 250 movies based on user ratings. We also believe top 250 movies can capture people's likes and dislikes about movies and provide enough infomation for analyzing what can make movies successful. Moreover, IMDb has fairly wide databases containing wide range of movies and the viewers' ratings and reviews can replect how this movie stay in a high rating. To collect the data, we use web scrape techniques to collect the json data and define the relevant functions to grab the data we need to complete the analysis such as casts, description, and estimated budget.

2.2 Data Collection

To collect the data, we use web scrape techniques to collect the json data and define the relevant functions to grab the data we need to complete the analysis such as casts, description, and estimated budget. During the process, using the beautiful soup allows us to grab movie information directly from IMDb’s database. 

The data was collected for the top 250 movies, and the following attributes were scraped:

    Rank: The movie's rank in the Top 250 list
    Title: The movie's title
    Year: The year the movie was released
    Rating: The IMDb rating of the movie, provided by users
    Genres: The genres associated with the movie (e.g., Drama, Action)
    Description: The intorduction of the movie
    Casts: The names of stars
    Estimated budget: The cost of making the movie
    Gross worlwide: The revenue from releasing movie to movie theaters

Each of these attributes was collected for all 250 movies, and the data was stored in a CSV file for further analysis.

2.3 Data Limitations

Some movies in the Top 250 list may not have complete information. For example:

    1. Ratings: Some movies may lack sufficient user ratings, leading to missing or incomplete data. Also, some movie has higher reputation in people's mind,but the viewers are not willing to reveal their thought in IMDb website.
    2. Genres: Some movies may have incomplete genre classification which can makes some movies has same genre tags have different ranking.
    3. Subjective Ratings: The IMDb ratings are subjective and are based on user votes, which can be influenced by factors such as recency bias or popularity.
    4. Popularity Bias: The Top 250 list reflects popular and well-known movies, so lesser-known or independent films may be underrepresented.

2.4 Possible Extensions

To improve the dataset and further analysis, the following extensions could be considered:

    1. Inclusion of Cast Information: For exampl, the details for the cast members, so we can analyse how diversity affects movies in a more detailed way.
    2. User Review Sentiment Analysis: Scraping user reviews to capture some keywords for people's feelings could provide more in-depth insights into why some movies are rated highly.
    3. Comparing with Other Platforms: Adding data from other review platforms, for instance, Rotten Tomatoes would allow for cross-platform comparisons becasue it also contains the rating from professional critics and the popularity from the audiences.

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

Based on the analysis of the genre distribution among the top 250 rated movies, it is clear that drama emerges as the most dominant genre, boasting a substantial frequency of 182 films. This suggests a strong audience preference for emotionally engaging narratives. Following drama, adventure and action genres also show significant representation, with 61 and 54 films, respectively, indicating a market for thrilling and action-packed content. Other genres like crime and comedy follow closely, appealing to viewers' interests in suspenseful and humorous storytelling. Genres such as horror and musical show much lower frequencies, suggesting these may have a more niche audience. For anyone considering producing a film, focusing on drama or incorporating adventure and action elements could be a promising strategy to attract a wider audience.

4.2 IMDb Ratings Over Time

    Ratings Trends:
        Movies released in the 1990s and 2000s tend to have higher average ratings compared to those from earlier decades. This could be due to a larger number of IMDb users rating more recent movies.
        There was a slight decline in average ratings for movies released after 2010, which could indicate the growing volume of new releases and perhaps tougher competition in the streaming era.

4.3 Director Insights

    Directors with the Most Movies in the Top 250:
        Christopher Nolan: Known for movies like Inception and The Dark Knight, Nolan had 7 movies in the Top 250, with an average rating of 8.9.
        Steven Spielberg: Spielberg had 5 movies in the Top 250, with notable films like Schindler’s List and Jurassic Park.
        Stanley Kubrick: Kubrick also appeared multiple times, with highly rated films like 2001: A Space Odyssey.

4.4 Duration insights:

    The "Frequency of Movie Length Categories" graph shows that long movies dominate the dataset, with around 200 films. In contrast, medium and short movies are much less 
    common,with frequencies below 50 and 20, respectively. This suggests a bias toward longer films, potentially reflecting industry trends where longer runtimes are 
    associated with higher production values or audience preferences. The low representation of short and medium films might indicate their lesser production or inclusion 
    in mainstream datasets. Further analysis could explore whether longer runtimes correlate with better movie performance.

5. Limitations

    Limited Dataset: This analysis was based solely on the IMDb Top 250 movies list, which primarily reflects the preferences of IMDb users. A more diverse dataset, including lesser-known movies, could provide different insights.
    Recency Bias: More recent movies may receive higher ratings due to their popularity and current relevance.
    IMDb User Demographics: IMDb users are not necessarily representative of the general population, and their ratings may be skewed by certain demographics or interests.

6. Extensions and Future Research

    Sentiment Analysis of User Reviews: Analyzing the sentiment behind user reviews could provide more context behind why certain movies are rated highly or poorly.
    **Comparison with Other Rating
