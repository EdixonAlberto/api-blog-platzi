import requests
from bs4 import BeautifulSoup
import json

url = 'https://platzi.com/blog'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article', class_='Contribution')

posts: list = []

for article in articles:
    title: str = article.find('h3', class_='Contribution-title').text
    preview: str = article.find('p', class_='Contribution-extract').text
    author: str = article.find('a', class_='ContributionAuthor-username').text
    link: str = article.find('a', class_='Contribution-link')['href']

    data = {
        'title': title,
        'preview': preview,
        'author': author,
        'link': url + link,
        # 'likes':  int(likes)
    }

    posts.append(data)

json_data = json.dumps(posts)

with open('public/data.json', 'w') as file:
    file.write(json_data)

print('✅ JSON data saved in public/data.json')
