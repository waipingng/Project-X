IMDb Top 250 Movies Analysis Report: What Contributes to High Ratings and Long-Term Success?

1. Introduction

IMDb (Internet Movie Database) is a widely used online resource for information related to films, television programs, making it an ideal source for movie-related data. For this project, we specifically worked with the Top 250 movies on IMDb. Also, IMDb covers every latest movie to reflect the people's preferences. So, we would like to discover what types of movie can get higher rating and what makes the movies keep attracting viewers' attention.

Purpose of the Research

This research aims to investigate four critical factors:

    The correlation between word frequencies in movie descriptions and IMDb ratings.
    The relationship between genres and IMDb ratings.
    The effect of movie duration on ratings.
    How content ratings (e.g., PG, PG-13, R) affect the breadth of a movie’s audience and its correlation with ratings.

By examining these factors, we aim to uncover patterns that can inform filmmakers, studios, and marketers on how to craft movies that resonate with audiences and maintain relevance over time.

1.1 Instruction to rerun the file

    a) Implement scrape_movie by python3 code/scrape_movies.csv: The function scrape_movie scrapes detailed information about a specific movie given its IMDb URL. The function extracts the movie title, year, runtime, rating, genre, description, director, cast, user reviews, budget, and worldwide gross.

    b) Implement scrape_page by python3 code/common.py: The function scrape_page scrapes all the movie URLs from the IMDb Top 250 page. It returns a list of movie URLs that will later be used by the scrape_movies function.

    c) Implement scrape.py by python3 code/scrape.py:Several functions are provided to extract specific information from the IMDb movie page and save to a csv file

    d) implement common_word_ratings by python 3 code/common_word_ratings.csv: first by function def clean_description, we got clean words from the description and then compute correlation of word frequencies with ratings.

    e) implement genres function:to get the corelationo between genres and IMDb ratings.

    f) implement the duration function to get the relationship with duration and ratings

    g) implement the content ranting function to see how broad are the audiences and its relationship with the IMDb ratings.

2. Data Source

2.1 Dataset Source

The data for this project was sourced from IMDb’s Top 250 movies list. This list is publicly available on IMDb and ranks the top 250 movies based on user ratings. We also believe top 250 movies can capture people's likes and dislikes about movies and provide enough infomation for analyzing what can make movies successful. Moreover, IMDb has fairly wide databases containing wide range of movies and the viewers' ratings and reviews can replect how this movie stay in a high rating. To collect the data, we use web scrape techniques to collect the json data and define the relevant functions to grab the data we need to complete the analysis such as genres, description, content-rating and duration.

2.2 Data Collection

The dataset used in this analysis was sourced from IMDb’s Top 250 Movies list. This list ranks the top 250 movies based on user ratings and is widely recognized as a credible reflection of audience preferences. The data was gathered using web scraping techniques from IMDb’s public listings. The data collected includes:

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

2.3 Limitations of the Data

Despite its richness, the dataset has some limitations:

    1. Subjective Ratings: IMDb ratings are user-generated and are thus inherently subjective. Factors like recency bias (newer movies being rated higher) and popularity bias (more popular movies being rated by more people) can skew the results.
    2. Missing Data: Some movies may have incomplete information, particularly for older films that may not have detailed content ratings or full cast lists.
    3. Genre Ambiguity: Some films belong to multiple genres, which can create ambiguity when analyzing how specific genres correlate with ratings.
    4. Lack of Contextual Data: The dataset does not contain detailed information such as release date timing, promotional campaigns, or critical reception, which could also influence ratings.

2.4 Suggested Extensions to Improve the Analysis

To improve the quality of the analysis, the following data could be added:

    1. User Reviews: Including user review text would allow for sentiment analysis, providing deeper insights into how viewers perceive the film.
    2. Budget and Box Office Data: Understanding the movie’s budget and gross income could provide insights into how financial success correlates with ratings.
    3. Cross-Platform Ratings: Gathering ratings from other platforms like Rotten Tomatoes or Metacritic could provide a broader perspective and allow comparisons between critic and audience scores.
    4. Director and Actor Information: Analyzing the impact of certain directors and actors on ratings could provide insights into how these figures influence audience perception.
    
3. Methodology
3.1 Goal of the Analysis

The goal of this analysis is to investigate how different aspects of movies—such as the themes represented in descriptions, genres, duration, and content ratings—affect their IMDb scores. We seek to answer the following research questions:

    Do certain words in movie descriptions correlate with higher ratings?
    Are certain genres more likely to have higher ratings?
    Does movie length affect its IMDb rating?
    Does the content rating affect the film’s rating based on audience size?

3.2 Data Preparation and Cleaning

    Word Cleaning for Descriptions: The descriptions were cleaned by removing common stopwords (e.g., "the", "and") to focus on meaningful keywords.
    Handling Missing Data: Movies with missing key information, such as ratings or descriptions, were excluded from the analysis.
    Genre Processing: Movies with multiple genres were processed to ensure each genre was analyzed separately.
    Type Conversion: All relevant fields, such as ratings and durations, were converted into numerical formats to allow for statistical analysis.

3.3 Analysis Techniques

    Correlation Analysis: We used the Pearson correlation coefficient to examine how word frequencies in movie descriptions relate to IMDb ratings.
    Genre Analysis: The dataset was grouped by genre, and the average rating for each genre was calculated to understand how different genres perform.
    Duration Analysis: We explored the relationship between movie length and IMDb ratings to identify any trends in how runtime affects audience         reception.
    Content Rating Analysis: We analyzed how different content ratings (e.g., PG, PG-13, R) impact IMDb scores, hypothesizing that broader audience ratings would correlate with higher scores.

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

4.2 Word Frequencies in description and IMDb Ratings

![image](https://github.com/user-attachments/assets/e5ff057a-0abc-4476-bb8c-e31ac20d5597)


1. Words with Strong Positive Correlation:

    "Young" (~0.15 correlation):
        This word shows the strongest positive correlation with ratings. It suggests that movies where "young" appears frequently in the description (perhaps focusing on younger characters or youth-related themes) tend to receive higher IMDb ratings.
        Examples could be films like The Lion King or Harry Potter, where youth and coming-of-age narratives play a central role.

    "American" (~0.11 correlation):
        The word "American" also shows a high positive correlation. This may suggest that movies centering around American culture, identity, or historical events tend to be highly rated.
        Examples might include films about American history (Saving Private Ryan), the American Dream, or stories set in the US.

    "Son" (~0.08 correlation):
        Descriptions that include "son" tend to be correlated with higher ratings. This could reflect the success of family-focused movies or stories involving father-son relationships. Emotional family dynamics often resonate well with audiences.

    "Police" (~0.05 correlation):
        Movies with a focus on law enforcement or crime-solving seem to perform well. Crime dramas or thrillers where "police" play a central role might often receive favorable reviews, possibly because of their suspenseful nature.

2. Words with Negative Correlation:

    "Struggles" (~ -0.07 correlation):
        The word "struggles" shows a negative correlation with ratings, which suggests that movies that focus on difficult situations or challenges might not be as highly rated. While conflict is essential for storytelling, perhaps movies emphasizing hardship too heavily don't resonate as positively.

    "War" (~ -0.04 correlation):
        Surprisingly, "war" shows a slight negative correlation. This could be attributed to mixed audience reception of war films. While some war movies are critically acclaimed (Saving Private Ryan), others may not resonate as well with broader audiences, depending on the narrative's focus.

    "Jewish" (~ -0.05 correlation):
        The word "Jewish" shows a negative correlation. This might be related to the fact that movies centering around specific cultural or religious groups may have niche appeal and may not resonate as strongly with a wider audience. This is not indicative of quality but might reflect broader audience preferences.

    "Relationship" (~ -0.05 correlation):
        Surprisingly, "relationship" correlates negatively with ratings. This suggests that movies heavily marketed as focusing on relationships (especially romantic ones) may not always result in high IMDb scores, potentially reflecting oversaturation in certain genres (romantic comedies, dramas, etc.).

3. Neutral or Near-Zero Correlation:

    "Murder", "Love", "Life", "Friend", "Journey" (~0.0 correlation):

        These words have correlations close to zero, meaning their presence in movie descriptions does not strongly impact ratings one way or the other. This might be because these are common themes across many genres, and their mere presence does not necessarily predict the quality of the film.

        For instance, words like "love" or "life" are fundamental to storytelling, and their effect may vary depending on the execution, making them less predictive of high or low ratings.

4.3 Duration insights:
![image](https://github.com/user-attachments/assets/8be2b623-c2b8-401b-bf1a-feffcd7a8fae)


    The "Frequency of Movie Length Categories" graph shows that long movies dominate the dataset, with around 200 films. In contrast, medium and short movies are much less 
    common,with frequencies below 50 and 20, respectively. This suggests a bias toward longer films, potentially reflecting industry trends where longer runtimes are 
    associated with higher production values or audience preferences. The low representation of short and medium films might indicate their lesser production or inclusion 
    in mainstream datasets. Further analysis could explore whether longer runtimes correlate with better movie performance.

4.4 Content Rating and Audience Reach

    Wider Audience Appeal (PG, PG-13): Movies with PG or PG-13 ratings tend to perform better, likely because they reach broader audiences, including families and younger viewers. Films like Star Wars and Harry Potter are examples of high-performing movies with broad appeal.
    Restricted Audiences (R-rated): R-rated movies have a narrower audience due to content restrictions. While some, like Pulp Fiction, perform well, many others struggle to reach the same broad appeal as PG-13 films.

5. Limitations

    Subjectivity of Ratings: IMDb ratings are subjective and based on user opinions. Factors like recency bias and popularity bias may skew the data.
    Genre Ambiguity: Some movies belong to multiple genres, which complicates analyzing how specific genres alone affect ratings.
    Limited Dataset Scope: The Top 250 list is a subset of all movies and reflects mainstream preferences. Independent or lesser-known films are underrepresented.

6. Extensions and Future Research

    Sentiment Analysis of User Reviews: Analyzing review text could provide deeper insights into why audiences rate certain movies highly or poorly.
    Incorporating Financial Data: Adding data such as budget and box office performance could reveal whether financial success correlates with audience satisfaction.
    Director and Actor Analysis: Understanding the influence of key filmmakers and stars on movie ratings could shed light on star power’s impact on success.

Conclusion

The findings from this analysis provide valuable insights into the factors that contribute to a movie’s success on IMDb. Genres play a crucial role, with drama, documentaries, and animated films performing best, while action and comedy tend to receive lower ratings. Word frequencies in movie descriptions indicate that films emphasizing youth, family dynamics, and cultural identity resonate more with audiences than those focused on war or struggles. Longer movies are favored, likely due to their ability to offer more complex storytelling and character development. Finally, content ratings demonstrate that films with broader audience reach, such as PG and PG-13, tend to perform better than those restricted to adult viewers.

The goal of this research was to uncover what makes a movie successful in terms of IMDb ratings and longevity. Based on our analysis, we can conclude that successful movies often focus on emotionally engaging and relatable themes, appeal to a broad audience, offer in-depth narratives, and are associated with longer runtimes. These findings offer valuable guidance for filmmakers and studios aiming to create films that not only perform well in the short term but also maintain lasting appeal over time.

Further research could incorporate sentiment analysis of user reviews, financial data, and comparisons across multiple rating platforms to deepen our understanding of what contributes to a movie’s success. By integrating these additional elements, future studies can provide a more comprehensive picture of the factors influencing movie ratings and longevity.

