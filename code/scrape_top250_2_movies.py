import requests
from bs4 import BeautifulSoup
import json



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


url = 'https://www.imdb.com/chart/top/'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')


    script_tag = soup.find('script', type='application/ld+json')
    
    if script_tag:

        json_data = json.loads(script_tag.string)


        movies = json_data['itemListElement']


        movie_data_list = []

        for movie in movies:
            item = movie['item']
            title = item.get('name')
            url = item.get('url')
            rating = item.get('aggregateRating', {}).get('ratingValue', 'N/A')
            rating_count = item.get('aggregateRating', {}).get('ratingCount', 'N/A')
            description = item.get('description')
            genre = item.get('genre', 'N/A')
            content_rating = item.get('contentRating', 'N/A')
            duration = item.get('duration', 'N/A')


            movie_info = {
                'title': title,
                'url': url,
                'rating': rating,
                'rating_count': rating_count,
                'description': description,
                'genre': genre,
                'content_rating': content_rating,
                'duration': duration
            }

            movie_data_list.append(movie_info)


        with open('imdb_top_movies.json', 'w', encoding='utf-8') as f:
            json.dump(movie_data_list, f, indent=4, ensure_ascii=False)

        print("successful save to imdb_top_movies.json 文件中。")
    else:
        print("no data")
else:
    print(f"error, status code: {response.status_code}")

