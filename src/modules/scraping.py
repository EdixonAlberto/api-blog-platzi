import requests
from bs4 import BeautifulSoup
# import json


class ScrapingPlatzi():
  def __init__(self) -> None:
    self.url = 'https://platzi.com'
    response = requests.get(self.url + '/blog/')
    self.soup = BeautifulSoup(response.text, 'html.parser')

  def get_blog_posts(self) -> list:
    articles = self.soup.find_all('article', class_='Contribution')
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
          'link': self.url + link,
          # 'likes':  int(likes)
      }

      posts.append(data)

    return posts
    # json_data = json.dumps(posts)
    # with open('public/data.json', 'w') as file:
    #   file.write(json_data)
    # print('✅ JSON data saved in public/data.json')


if __name__ == '__main__':
  sp = ScrapingPlatzi()
  sp.get_blog_posts()
