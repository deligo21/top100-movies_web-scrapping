from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/');

top_movies_response = response.text
soup = BeautifulSoup(top_movies_response, 'html.parser')

divs = soup.findAll('div', {'class':'article-title-description__text'})
titles_movies = [a.find('h3').getText() for a in divs][::-1]

with open("./list_of_movies.txt", "w") as list:
    for movie in titles_movies:
        list.write(movie + "\n") 