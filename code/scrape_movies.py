#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:32:30 2024

@author: wangyuchen
"""

from common import get_soup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_title(soup):
    movie_name = soup.find_all("span", class_ = "hero__primary-text")[0].text
    print(movie_name)

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
    genre = []
    for i in range(len(genre_tags)):
        genre.append(genre_tags[i].text)
    
    return genre


def get_director(soup):
    movie_director = soup.find_all("div", class_ = "ipc-metadata-list-item__content-container")[4]
    a_tag = movie_director.find_all("a", class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")[0].text
    return a_tag

def get_top_casts(soup):
    movie_casts = soup.find_all("a", class_ = "sc-cd7dc4b7-1 kVdWAO")
    cast_members = []
    for i in range(len(movie_casts)):
        cast_members.append(movie_casts[i].text)

    return cast_members


def get_num_user_reviews(soup):
    user_reviews= soup.find_all("a", class_ = "ipc-link ipc-link--baseAlt ipc-link--touch-target sc-b782214c-2 kqhWjl isReview")
    if len(user_reviews) < 3:
        num_user_reviews = user_reviews[0].find_all("span", class_ = "less-than-three-Elements")[0].text.split("U")[0]
    else: 
        num_user_reviews = user_reviews[0].find_all("span", class_ = "three-Elements")[0].text.split("U")[0]

    return num_user_reviews




def scrape_movie(url, headers):

    soup = get_soup(url, headers = headers)
    title = get_title(soup) 
    year = get_year(soup) 
    movie_length = get_movie_length(soup)
    rating = get_rating(soup)
    genre = get_genre(soup)
    movie_director = get_director(soup)
    movie_top_casts = get_top_casts(soup)
    num_user_reviews = get_num_user_reviews(soup)

    
    scrape_top250_dict = {
        "title": title,
        "year": year,
        "movie length": movie_length,
        "rating": rating,
        "genre": genre,
        "movie director": movie_director, 
        "movie top casts": movie_top_casts,
        "number of user reviews ": num_user_reviews,

    }

    return scrape_top250_dict

def scrape_movies(movie_urls, headers):
    scrape_movies_info = []
    for movie_url in movie_urls:
        scraped_movie = scrape_movie(movie_url, headers = headers)
        scrape_movies_info.append(scraped_movie)
    return scrape_movies_info

