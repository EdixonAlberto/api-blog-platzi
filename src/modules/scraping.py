from typing import TypedDict, Literal
import requests
from bs4 import BeautifulSoup
# import json


class QueryDict(TypedDict):
  filter: Literal['new', 'best', 'top']
  page: str


class ScrapingPlatzi():
  def __init__(self, query: QueryDict) -> None:
    self.url = 'https://platzi.com'
    query_params = f"?contribution_filter={query['filter']}&contribution_page={query['page']}"
    response = requests.get(f"{self.url}/blog/{query_params}")
    self.soup = BeautifulSoup(response.text, 'html.parser')

  def get_blog_posts(self) -> list:
    articles = self.soup.find_all('article', class_='Contribution')
    posts: list = []

    for article in articles:
      link: str = self.url + article.find('a', class_='Contribution-link')['href']
      title: str = article.find('h3', class_='Contribution-title').text
      preview: str = article.find('p', class_='Contribution-extract').text
      author: str = article.find('a', class_='ContributionAuthor-username').text
      author_picture: str = article.find('figure', class_='ContributionAuthor-avatar').find('img')['src']
      likes: int = int(article.find('span', class_='Star-number').text)
      # Get quatity of comments
      comments_text: str = article.find('div', class_='ContributionComment').find('span').text.split()[0]
      comments: int = int(comments_text) if comments_text.isnumeric() else 0
      timeago: str = article.find('time', class_='ContributionDate').find('span').text

      data = {
          'link':  link,
          'title': title,
          'preview': preview,
          'author': author,
          'author_picture': author_picture,
          'likes':  likes,
          'comments': comments,
          'relative_time': timeago
      }

      posts.append(data)

    return posts

    # json_data = json.dumps(posts)
    # with open('public/data.json', 'w') as file:
    #   file.write(json_data)
    # print('✅ JSON data saved in public/data.json')


if __name__ == '__main__':
  sp = ScrapingPlatzi({
      'filter': 'new',
      'page': '1'
  })
  sp.get_blog_posts()
