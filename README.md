**                       ****IMDb Top 250 Movies Analysis Report: What Contributes to High Ratings and Long-Term Success?******

**1. Introduction**

IMDb (Internet Movie Database) is a widely used online resource for information related to films, television programs, making it an ideal source for movie-related data. For this project, we specifically worked with the Top 250 movies on IMDb. Also, IMDb covers every latest movie to reflect the people's preferences. So, we would like to discover what types of movie can get higher rating and what makes the movies keep attracting viewers' attention.

**Purpose of the Research**

This research aims to investigate four critical factors:

    The correlation between word frequencies in movie descriptions and IMDb ratings.
    The relationship between genres and IMDb ratings.
    The effect of movie duration on ratings.
    How film genres affect the breadth of a movie’s audience and the correlation between the audience's breadth and the ratings.

By examining these factors, we aim to uncover patterns that can inform filmmakers, studios, and marketers on how to craft movies that resonate with audiences and maintain relevance over time.

**1.1 Instruction to rerun the file**

    a) Implement scrape.py by python3 code/scrape.py: We run common.py first to make URL(soup) to construct url to extract data. Also, you can use your own user agent to scrape the page. So, several functions are provided in the scrape_movies.py to extract specific information from the IMDb movie page such as movie title, year, runtime, rating, genre, description, director, cast, user reviews, budget, and worldwide gross and save to a csv file

    b) implement common_word_ratings by python3 code/common_word_ratings.csv: first by function def clean_description, we got clean words from the description and then compute correlation of word frequencies with ratings.

    c) implement genres function by python3 code/genre.py:Cleaned genre frequency saved to artifacts/genre_frequency.csv in descending order. python3 code/genre_rating.py:Average rating for each genre saved to artifacts/  genre_avg_rating.csv in descending order.python3 code/graph_genre.py to get the graph of genre

    d) implement the duration function by python3 code/rating_and_length.py: to get the relationship with duration and ratings, python3 code/Duration_frequency_graph.py to get the graph

    e) implement genre_audience_breadth_code.py by python3 code/genre_audience_breadth_code.py: figure out the coding part of  the relationship of film genres and the breadth of a movie’s audience and save to the new csv file; implement graph_genre_breadth.py by python3 code/graph_genre_breadth.py : draw the graph of the relationship between film genres and the breadth of a movie’s audience; implement breadth_rate_code.py by python3 code/breadth_rate_code.py : the coding part of the correlation between the audience's breadth and the ratings and save to the new csv file; implement graph_breadth_rate.py by python3 code/graph_breadth_rate.py : draw the graph of the correlation between the audience's breadth and the ratings 
 
**2. Data Source**

**2.1 Dataset Source**

The data for this project was sourced from IMDb’s Top 250 movies list. This list is publicly available on IMDb and ranks the top 250 movies based on user ratings. We also believe top 250 movies can capture people's likes and dislikes about movies and provide enough infomation for analyzing what can make movies successful. Moreover, IMDb has fairly wide databases containing wide range of movies and the viewers' ratings and reviews can replect how this movie stay in a high rating. To collect the data, we use web scrape techniques to collect the json data and define the relevant functions to grab the data we need to complete the analysis such as genres, description, content-rating and duration.

**2.2 Data Collection**

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
    Rating counts: The number of viewers who leave ratings
    Content rating: The category of the movie targets for

Each of these attributes was collected for all 250 movies, and the data was stored in a CSV file for further analysis.

**2.3 Limitations of the Data**

Despite its richness, the dataset has some limitations:

    1. Subjective Ratings: IMDb ratings are user-generated and are thus inherently subjective. Factors like recency bias (newer movies being rated higher) and popularity bias (more popular movies being rated by more people) can skew the results.
    2. Missing Data: Some movies may have incomplete information, particularly for older films that may not have detailed content ratings or full cast lists.
    3. Genre Ambiguity: Some films belong to multiple genres, which can create ambiguity when analyzing how specific genres correlate with ratings.
    4. Lack of Contextual Data: The dataset does not contain detailed information such as release date timing, promotional campaigns, or critical reception, which could also influence ratings.

**2.4 Suggested Extensions to Improve the Analysis**

To improve the quality of the analysis, the following data could be added:

    1. User Reviews: Including user review text would allow for sentiment analysis, providing deeper insights into how viewers perceive the film.
    2. Budget and Box Office Data: Understanding the movie’s budget and gross income could provide insights into how financial success correlates with ratings.
    3. Cross-Platform Ratings: Gathering ratings from other platforms like Rotten Tomatoes or Metacritic could provide a broader perspective and allow comparisons between critic and audience scores.
    4. Director and Actor Information: Analyzing the impact of certain directors and actors on ratings could provide insights into how these figures influence audience perception.
    
**3. Methodology**

**3.1 Goal of the Analysis**

The goal of this analysis is to investigate how different aspects of movies—such as the themes represented in descriptions, genres, duration, and content ratings—affect their IMDb scores. We seek to answer the following research questions:

    Do certain words in movie descriptions correlate with higher ratings?
    Are certain genres more likely to have higher ratings?
    Does movie length affect its IMDb rating?
    Does the content rating affect the film’s rating based on audience size?

**3.2 Data Preparation and Cleaning**

    Word Cleaning for Descriptions: The descriptions were cleaned by removing common stopwords (e.g., "the", "and") to focus on meaningful keywords.
    Handling Missing Data: Movies with missing key information, such as ratings or descriptions, were excluded from the analysis.
    Genre Processing: Movies with multiple genres were processed to ensure each genre was analyzed separately.
    Type Conversion: All relevant fields, such as ratings and durations, were converted into numerical formats to allow for statistical analysis.

**3.3 Analysis Techniques**

Correlation Analysis: We used the Pearson correlation coefficient to examine how word frequencies in movie descriptions relate to IMDb ratings.

Genre Analysis: The dataset was grouped by genre, and the average rating for each genre was calculated to understand how different genres perform.

Duration Analysis: We explored the relationship between movie length and IMDb ratings to identify any trends in how runtime affects audience reception.

Content Rating Analysis: We analyzed how different content ratings (e.g., PG, PG-13, R) impact IMDb scores, hypothesizing that broader audience ratings would correlate with higher scores.

  **4. Findings**
    
**4.1 Average Rating by Genre**


![top_13_genre_plot](https://github.com/user-attachments/assets/a0ee26b7-cce7-4fff-a587-9d2c4846a735)



The data reveals a clear distinction between the highest and lowest-rated genres based on user ratings. At the top, "Mountain Adventure" leads with an impressive rating of 9, followed closely by "Medical Drama" and "Gun Fu", both rated at 8.7. These top genres demonstrate a strong appeal across a range of themes, from thrilling action in "Gun Fu" to the human-centric drama of "Medical Drama."
The ratings then gradually taper down to "Prison Drama" at 8.54, which rounds off the top-rated list, signaling strong audience appreciation for intense and dramatic storytelling formats.

Conversely, at the lower end of the spectrum, a variety of genres including "Boxing," "Iyashikei," "Cyber Thriller," "Motorsport," and others share a uniform rating of 8.1. This grouping suggests that while these genres still hold some appeal, they may cater to more niche audiences or lack the broader mass appeal found in the higher-rated categories.

When analyzing the ratings, it becomes evident that comparing genres purely based on average scores can be misleading. Niche genres, like "Mountain Adventure" or "Gun Fu", benefit from having fewer films, which means even one highly rated movie can significantly raise the average. In contrast, more popular genres like crime or drama have a much larger selection of films, so their averages are more diluted. Even though many films in these popular genres may perform well, the sheer number of titles—both high- and low-performing—brings down the overall average rating.

In terms of frequency, drama clearly dominates with 186 films, far exceeding other genres like adventure (61), thriller (55), action (54), and crime (53). This also reinforces why the average ratings in popular genres tend to be lower: with such a vast number of entries, it’s inevitable that not all films will perform as well. In contrast, niche genres like "Mountain Adventure" or "Prison Drama" may have fewer films but benefit from higher average ratings due to the small sample size.

**4.2 Word Frequencies in description and IMDb Ratings**

 Do certain words in movie descriptions correlate with higher ratings?

![image](https://github.com/user-attachments/assets/c4cc0202-c325-4232-87ee-be3cd340be9e)

The chart reveals several insights into the relationship between certain thematic words and movie ratings:

Words with Positive Correlation:

"Son" shows the strongest positive correlation, indicating that movies mentioning "son" in their descriptions tend to receive higher ratings. This could reflect a preference for narratives that explore family dynamics, father-son relationships, or stories centered around younger characters.
"Young" also has a positive correlation, suggesting that themes involving youth, coming-of-age stories, or youthful energy are well-received by audiences. Films featuring younger characters often resonate with viewers, possibly due to their relatability and emotional depth.
"American" is positively correlated with ratings, highlighting that movies that focus on American culture, identity, or historical events may be particularly appealing to audiences. This theme could reflect a sense of familiarity or national pride among viewers.
"Woman" and "Story" show moderate positive correlations, indicating that films emphasizing female characters or storytelling elements tend to be appreciated by audiences. The focus on diverse narratives and strong character development may contribute to higher ratings.

Words with Negative Correlation:
"Read" and "Struggles" exhibit a negative correlation with ratings, suggesting that movies that emphasize challenges or struggles in their descriptions may not resonate as positively with viewers. While conflict is essential for storytelling, an excessive focus on hardship could make a film seem heavier or less enjoyable, potentially impacting ratings.
"Jewish" and "Journey" also show slight negative correlations, which may indicate that movies centered around specific cultural or religious experiences or those framed as journeys might have a more niche appeal. While these films can be critically acclaimed, their themes may not always attract broad audiences, resulting in varied ratings.
 "Mysterious" shows a slight negative correlation, suggesting that films focusing on mystery or suspense might not consistently achieve high ratings. This could be due to the challenges of delivering satisfying resolutions in suspenseful narratives, which can affect overall viewer satisfaction.

Neutral or Near-Zero Correlation:
Words like "Love", "Crime", "Life", and "Friends" have correlations close to zero, indicating that their presence in movie descriptions does not have a significant linear relationship with ratings. These are common themes across many film genres, and their impact on ratings may vary widely depending on the execution and context of each film. While such words are integral to storytelling, they do not appear to be strong predictors of a movie's rating by themselves.

This analysis demonstrates that certain words in movie descriptions have measurable correlations with IMDb ratings. Themes related to family ("son"), youth ("young"), and cultural identity ("American") tend to be associated with higher ratings, suggesting that audiences appreciate films that explore these themes deeply. Conversely, words like "struggles" and "read" correlate negatively with ratings, indicating that narratives focusing heavily on hardship or introspective themes might be less universally appealing. The presence of neutral correlations for terms like "love" or "crime" suggests that these themes, while popular, do not predict a film’s rating without considering the quality and context of their presentation.

Overall, this analysis provides valuable insights for filmmakers and content creators aiming to craft stories that resonate with audiences. Emphasizing themes that audiences connect with emotionally—such as family dynamics or youth-oriented stories—may be a strategic choice for achieving higher ratings, while films with more niche or intense themes should focus on delivering a satisfying and well-executed narrative.

**4.3 Duration insights:**

Does movie length affect its IMDb rating?

![image](https://github.com/user-attachments/assets/72e21adf-d4f2-459b-960d-b6682fe9b8ee)

The box plot above illustrates the distribution of IMDb ratings based on three categories of movie lengths: short (less than 90 mins), medium (90-150 mins), and long (above 150 mins). Long movies show a notably higher median rating, around 8.5, compared to their shorter counterparts. This suggests that longer films tend to achieve more favorable ratings, potentially because they have the time to delve into complex narratives, develop characters more fully, and create immersive experiences that resonate with viewers. The ratings of long movies, while varied, maintain a relatively high range, and a few outliers reach ratings above 9.0. These outliers indicate that when executed well, long films can achieve critical acclaim and high audience ratings.

In contrast, medium-length movies have a median rating slightly lower than long films, approximately 8.3. While they do not reach the same consistent heights as longer movies, their ratings are still solid. The interquartile range (IQR) for medium-length films spans from 8.0 to 8.6, showing a stable pattern, though with less variability compared to long films. This suggests that while medium-length films are capable of achieving high ratings, the scope for achieving the same level of deep narrative engagement as longer movies might be somewhat constrained. However, the presence of a few highly-rated outliers above 9.0 indicates that certain medium-length films can still resonate exceptionally well with audiences.

Short movies, meanwhile, tend to receive lower ratings overall, with a median of around 8.1, which is notably below that of both medium and long films. The IQR for short movies is more compressed, ranging from 8.0 to 8.3, indicating less variability in their ratings. This suggests that while short films tend to deliver a consistent viewer experience, their limited length may restrict their ability to fully develop complex stories or characters, which could be a factor in their generally lower ratings. However, the presence of an outlier above 8.8 shows that while most short movies may not achieve the same acclaim as longer films, there are exceptions that manage to captivate audiences and garner high ratings.

Overall, the analysis indicates a clear trend where longer movies tend to be rated higher on IMDb, likely due to their ability to provide more depth and richness in storytelling. Medium-length films also maintain strong ratings but do not reach the same level of acclaim as often as longer films. Short movies, while typically receiving lower ratings, still have the potential to impress viewers with the right content. This suggests that while longer films may have an inherent advantage in achieving higher ratings, the quality and execution of a film's content remain crucial for its success, regardless of length.

**4.4 Content Rating and Audience Reach**

Does Content Rating Affect a Film’s Rating Based on Audience Size?

![image](https://raw.githubusercontent.com/waipingng/Project-X/refs/heads/main/artifacts/genre_audience_breadth_table_part1.png)

![image](https://github.com/user-attachments/assets/3ba375b0-0b9c-42c8-9210-e4939692a0f9)

My values in the graph are rounded to the nearest whole percentage
The content rating of a movie plays a crucial role in determining its potential audience reach. Content ratings like "Approved" or "G" indicate that a film is suitable for all ages, making it accessible to a broader audience, including families and young viewers. Analysis of our dataset reveals that certain genres have a higher proportion of movies with these inclusive ratings. For example, Parody (50% "G"), Anime (50% "G"), and slapstick (100% "G") are more likely to have content suitable for general audiences. Producing films in these genres can attract a diverse audience base, from children to adults, offering the potential for widespread popularity.

In contrast, R rating restrict viewership to adults, significantly narrowing the potential audience. Our analysis shows that genres such as Cyberpunk, Docudrama, Samurai,Satire tend to have a higher proportion of films with an "R" rating. These genres often contain mature themes, violence, or intense content that limits their audience to adults. As a result, while these films might appeal strongly to a specific demographic, they generally lack the broad audience reach of family-friendly films.
    
![image](https://raw.githubusercontent.com/waipingng/Project-X/5647b2b9874d736ad2367c6a67165327d62249ac/artifacts/rate_audience_breadth.png)


while it might seem that having a restricted audience reach would be a disadvantage, our analysis suggests that it’s not always the case. From the graph, we observe that films with the highest IMDb ratings (8.8-9.3) are often R-rated, PG-13, or Approved films. This indicates that despite a narrower potential audience, R-rated films can achieve high critical acclaim and resonate deeply with their viewers. Films like Pulp Fiction or The Shawshank Redemption are examples of R-rated movies that have received outstanding ratings despite their limited audience.

PG and PG-13 movies, on the other hand, tend to perform well because they appeal to a broader range of viewers, including families and teenagers. This wider appeal allows these films to gather more ratings and potentially maintain high overall scores. PG-13 movies such as Star Wars and Harry Potter demonstrate how balancing engaging content with family-friendly themes can attract large audiences while still achieving high ratings.


**5. Limitations**

    Subjectivity of Ratings: IMDb ratings are subjective and based on user opinions. Factors like recency bias and popularity bias may skew the data.
    Genre Ambiguity: Some movies belong to multiple genres, which complicates analyzing how specific genres alone affect ratings.
    Limited Dataset Scope: The Top 250 list is a subset of all movies and reflects mainstream preferences. Independent or lesser-known films are underrepresented.

**6. Extensions and Future Research**

    Sentiment Analysis of User Reviews: Analyzing review text could provide deeper insights into why audiences rate certain movies highly or poorly.
    Incorporating Financial Data: Adding data such as budget and box office performance could reveal whether financial success correlates with audience satisfaction.
    Director and Actor Analysis: Understanding the influence of key filmmakers and stars on movie ratings could shed light on star power’s impact on success.

**Conclusion**

The findings from this analysis provide valuable insights into the factors that contribute to a movie’s success on IMDb. Genres play a crucial role, with drama, adventure, thriller, action, and crime performing best. Word frequencies in movie descriptions indicate that films emphasizing youth, family dynamics, and cultural identity resonate more with audiences than those focused on war or struggles. Longer movies are favored, likely due to their ability to offer more complex storytelling and character development. Finally, content ratings demonstrate that films with broader audience reach, such as PG and PG-13, perform better than those restricted to adult viewers.

The goal of this research was to uncover what makes a movie successful in terms of IMDb ratings and longevity. Based on our analysis, we can conclude that successful movies often focus on emotionally engaging and relatable themes, appeal to a broad audience, offer in-depth narratives, and are associated with longer runtimes. These findings offer valuable guidance for filmmakers and studios aiming to create films that not only perform well in the short term but also maintain lasting appeal over time.

Further research could incorporate sentiment analysis of user reviews, financial data, and comparisons across multiple rating platforms to deepen our understanding of what contributes to a movie’s success. By integrating these additional elements, future studies can provide a more comprehensive picture of the factors influencing movie ratings and longevity.

