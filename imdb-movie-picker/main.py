import random
import requests
import sys
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/chart/top/'

def main():
    print("Downloading Top 250 list... please wait...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    movietags = soup.select('li.ipc-metadata-list-summary-item')

    movies = []
    for tag in movietags:
        title_el = tag.select_one('h3.ipc-title__text')
        year_el = tag.select('span.cli-title-metadata-item')
        rating_el = tag.select_one('span.ipc-rating-star')
        
        if title_el:
            title = title_el.text.split('. ', 1)[-1]
            year = year_el[0].text if year_el else "N/A"
            
            rating = 0.0
            if rating_el:
                try:
                    rating = float(rating_el.text.split()[0])
                except ValueError:
                    pass
            
            movies.append({'title': title, 'year': year, 'rating': rating})

    if not movies:
        print("No movies found! IMDb structure might have changed.")
        return

    print(f"Successfully found {len(movies)} movies.\n")

    while True:
        choice = random.choice(movies)
        print(f"🍿 Suggestion: {choice['title']} ({choice['year']}) - Rating: {choice['rating']}")
        
        user_input = input("\nHit [Enter] for another movie, or type 'q' to quit: ")
        
        if user_input.lower().strip() == 'q':
            print("Enjoy your movie! Bye.")
            break
        print("-" * 40)

if __name__ == '__main__':
    main()
