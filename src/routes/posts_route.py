from fastapi import APIRouter
from src.modules.response import Response, JsonResponse
from src.modules.scraping import ScrapingPlatzi

router = APIRouter()


@router.get('/api/posts')
async def get_posts() -> Response:
  """ Get posts from blog of platzi """
  scraping_platzi = ScrapingPlatzi()
  posts = scraping_platzi.get_blog_posts()
  return JsonResponse.ok(posts)
