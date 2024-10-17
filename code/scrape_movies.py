
from common import get_soup

def get_title(soup):
    movie_name = soup.find_all("span", class_ = "hero__primary-text")[0].text

    return movie_name


def get_year(soup):
    if len(soup.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--inherit-color")) < 6:
        movie_year = soup.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--inherit-color")[4].text
    else:
        movie_year = soup.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--inherit-color")[5].text
    
    return movie_year

def get_movie_length(soup):
    ul_tag = soup.find_all("ul", class_ ="ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt")[0]
    if len(ul_tag.find_all("li", class_ = "ipc-inline-list__item")) < 3:
        li_tag = ul_tag.find_all("li", class_ = "ipc-inline-list__item")[1].text
    else:
        li_tag = ul_tag.find_all("li", class_ = "ipc-inline-list__item")[2].text
    
    return li_tag


def get_rating(soup):
    movie_rating = soup.find_all("div", attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"})[0]
    span_tag = movie_rating.find_all("span", class_ = "sc-d541859f-1 imUuxf")[0].text

    return span_tag


def get_genre(soup):
    div_tag = soup.find_all("div", class_ = "ipc-chip-list__scroller")[0]
    genre_tags = div_tag.find_all("span", class_ = "ipc-chip__text")
    genre = str()
    for i in range(len(genre_tags)):
        genre += (genre_tags[i].text + ", ")
        
    
    return genre

def get_description(soup):
    description = soup.find_all("span", attrs = {"data-testid": "plot-xs_to_m"})[0].text

    return description


def get_director(soup):
    movie_director = soup.find_all("div", class_ = "ipc-metadata-list-item__content-container")[4]
    a_tag = movie_director.find_all("a", class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")[0].text
    return a_tag

def get_top_casts(soup):
    movie_casts = soup.find_all("a", class_ = "sc-cd7dc4b7-1 kVdWAO")
    cast_members = str()
    for i in range(len(movie_casts)):
        cast_members += (movie_casts[i].text + ", ")

    return cast_members


def get_num_user_reviews(soup):
    user_reviews= soup.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--touch-target sc-b782214c-2 kqhWjl isReview")
    if len(user_reviews) < 3:
        num_user_reviews = user_reviews[0].find_all("span", class_ = "less-than-three-Elements")[0].text.split("U")[0]
    else:
        num_user_reviews = user_reviews[0].find_all("span", class_ = "three-Elements")[0].text.split("U")[0]

    return num_user_reviews

def get_movie_budget(soup):
    if len(soup.find_all("div", attrs={"data-testid": "title-boxoffice-section"})) != 0:
        movie_est_budget = soup.find_all("div", attrs = {"data-testid": "title-boxoffice-section"})[0]
        if len(movie_est_budget.find_all("li", attrs = {"data-testid": "title-boxoffice-budget"})) != 0:
            est_budget_raw = movie_est_budget.find_all("li", attrs = {"data-testid": "title-boxoffice-budget"})[0]
            est_budget = est_budget_raw.find_all("span", class_ = "ipc-metadata-list-item__list-content-item")[0].text
            est_budget = est_budget.split(" (")[0]
        else:
            est_budget = "N/A"
    else:
        est_budget = "N/A"
    
    return est_budget

def get_movie_gross_worldwide(soup):
    gross_worldwide_flag = False
    if len(soup.find_all("div", attrs={"data-testid": "title-boxoffice-section"})) != 0:
        movie_gross_world = soup.find_all("div", attrs = {"data-testid": "title-boxoffice-section"})[0]
        if len(movie_gross_world.find_all("li", attrs = {"data-testid": "title-boxoffice-cumulativeworldwidegross"})) != 0:
            gross_worldwide_raw = movie_gross_world.find_all("li", attrs = {"data-testid": "title-boxoffice-cumulativeworldwidegross"})[0]
            gross_worldwide = gross_worldwide_raw.find_all("span", class_ = "ipc-metadata-list-item__list-content-item")[0].text

        else:
            gross_worldwide = "N/A"
    else:
        gross_worldwide = "N/A"

    return gross_worldwide

def get_rating_count(soup):
    movie_rating_raw = soup.find_all("div", attrs={"data-testid": "hero-rating-bar__aggregate-rating"})[0]
    rating_count = movie_rating_raw.find_all("div", class_ = "sc-d541859f-3 dwhNqC")[0].text
    return rating_count
    
def get_content_rating(soup):
    content_rating_raw = soup.find_all("ul", class_ = "ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt")[0]
    if len(content_rating_raw.find_all("li", class_ = "ipc-inline-list__item")) == 3:
        content_rating = content_rating_raw.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--inherit-color")[1].text
    else:
        content_rating = "N/A"

    return content_rating

    return rating_count
    
def get_content_rating(soup):
    content_rating_raw = soup.find_all("ul", class_ = "ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt")[0]
    if len(content_rating_raw.find_all("li", class_ = "ipc-inline-list__item")) == 3 :
        content_rating = content_rating_raw.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--inherit-color")[1].text
    else:
        content_rating = "N/A"

    return content_rating
    
def scrape_movie(url, headers):

    soup = get_soup(url, headers = headers)
    title = get_title(soup)
    year = get_year(soup)
    duration = get_movie_length(soup)
    rating = get_rating(soup)
    genre = get_genre(soup)
    description = get_description(soup)
    movie_director = get_director(soup)
    movie_top_casts = get_top_casts(soup)
    num_user_reviews = get_num_user_reviews(soup)
    movie_budget = get_movie_budget(soup)
    movie_gross_worldwide = get_movie_gross_worldwide(soup)
    rating_count = get_rating_count(soup)
    content_rating = get_content_rating(soup)
    
    scrape_top250_dict = {
        "title": title,
        "year": year,
        "duration": duration,
        "rating": rating,
        "genre": genre,
        "description": description,
        "movie director": movie_director,
        "movie top casts": movie_top_casts,
        "number of user reviews ": num_user_reviews,
        "movie budget": movie_budget,
        "movie gross worldwide": movie_gross_worldwide,
        "rating_count": get_rating_count(soup),
        "content_rating": get_content_rating(soup),
        "rating_count": rating_count,
        "content_rating": content_rating
    }

    return scrape_top250_dict

def scrape_movies(movie_urls, headers):
    scrape_movies_info = []
    for movie_url in movie_urls:
        scraped_movie = scrape_movie(movie_url, headers = headers)
        scrape_movies_info.append(scraped_movie)
    return scrape_movies_info
