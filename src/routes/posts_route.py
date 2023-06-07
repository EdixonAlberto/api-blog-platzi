from typing import Literal, Literal
from fastapi import APIRouter
from src.modules.response import Response, JsonResponse
from src.modules.scraping import ScrapingPlatzi

router = APIRouter()


@router.get('/api/posts')
async def get_posts(filter: Literal['new', 'best', 'top'] = 'new', page: str = '1') -> Response:
  """ Get posts from blog of platzi """
  # TODO: create DTO to validate queries
  scraping_platzi = ScrapingPlatzi({
      'filter': filter,
      'page': page
  })
  posts = scraping_platzi.get_blog_posts()
  return JsonResponse.ok(posts)
