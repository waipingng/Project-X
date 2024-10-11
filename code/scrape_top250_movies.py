#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:31:35 2024

@author: wangyuchen
"""
import requests
from bs4 import BeautifulSoup



def get_soup(url):

    """Takes a URL and returns a BeautifulSoup() instance representing the HTML of the page."""

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    return soup

URL = "https://www.imdb.com/chart/top/"

def scrape_page():
    """Takes a page and returns a list of links to the book that are on the page."""
    soup = get_soup(URL)
    movie_links = soup.find_all("div", class_ = "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-ab348ad5-9 cIVpMc cli-title")
    links = []                                        
    for movie in movie_links:
        for link in movie_links.find_all("a", href = True):
            links.append("https://www.imdb.com/" + str(link["href"]))
    return links
print(scrape_page())

