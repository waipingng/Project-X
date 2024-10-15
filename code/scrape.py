#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:04:48 2024

@author: wangyuchen
"""

import os
import json
import csv

from common import scrape_page
from scrape_movies import scrape_movies

BASE_DIR = "artifacts"
CSV_PATH = os.path.join(BASE_DIR, "results.csv")

URL = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def scrape():
    """Scrape everything and return a list of books."""
    movie_urls = scrape_page()
    movies = scrape_movies(movie_urls, headers)
    return movies

print(scrape())


def write_books_to_csv(data, path):
    with open (path, "w", newline = "") as file:
        write = csv.DictWriter(file, data[0].keys())
        write.writeheader()
        write.writerows(movies)
    return


if __name__ == "__main__":

    BASE_DIR = "/Users/wangyuchen/Desktop/Project-X/artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "results.csv")

    os.makedirs(BASE_DIR, exist_ok=True)

    movies = scrape()
    write_books_to_csv(movies, CSV_PATH)
