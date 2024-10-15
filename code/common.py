<<<<<<< Updated upstream
# install imdbpy
  pip install git+https://github.com/alberanid/imdbpy


=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:31:35 2024

@author: wangyuchen
"""
>>>>>>> Stashed changes
import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_soup(url, headers):

    """Takes a URL and returns a BeautifulSoup() instance representing the HTML of the page."""

    response = requests.get(url, headers = headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    return soup

def scrape_page():
    """Takes a page and returns a list of links to the book that are on the page."""
    soup = get_soup(url, headers)
    movie_links = soup.find_all("ul", class_ = "ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 dHaCOW compact-list-view ipc-metadata-list--base")[0]                                     
    links = []
    for link in movie_links.find_all("a", class_ = "ipc-lockup-overlay ipc-focusable", href = True):
        links.append("https://www.imdb.com/" + str(link["href"]))
    return links
