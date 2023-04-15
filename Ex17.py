import requests
from bs4 import BeautifulSoup

articles = []

url = "https://www.imdb.com/chart/top/"
r = requests.get(url)
read_html = r.text

soup = BeautifulSoup(read_html, "lxml")

for story_heading in soup.find_all(class_="titleColumn"):
    if story_heading.a:
        articles.append(story_heading.a.text.strip())

print("\n".join(articles))
