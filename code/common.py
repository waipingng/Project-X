
import requests
import json
from bs4 import BeautifulSoup

"""Please type your user agent"""

url = "https://www.imdb.com/chart/top"
headers = {
    "User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
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
    script_tag = soup.find("script", type = "application/ld+json")
    json_data = json.loads(script_tag.string)
    movies = json_data["itemListElement"]
    movie_links = []
    for movie in movies:
        link = movie["item"].get("url")
        movie_links.append(link)
    return movie_links
