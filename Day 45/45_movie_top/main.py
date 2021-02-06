import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

my_request = requests.get(URL)
website_html = my_request.text
soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3")

print(all_movies)

# movies_title = []
# for movie in all_movies:
#     movies_title.append(movie.getText())

# for i in movies_title:
#     print(i)