from src.modules.response import Request, Response, JsonResponse
from src.modules.config import Config
from fastapi import Request


async def handler(request: Request, call_next) -> Response:
  """Authentication"""
  config = Config()

  # Show documentation
  if (request.url.path in ('/docs', '/openapi.json')):
    return await call_next(request)

  if not 'authorization' in request.headers:
    return JsonResponse.error(401, ["Header 'Authorization' is required"])

  headerToken = request.headers['authorization'].strip('Bearer ')
  token = config.env('ACCESS_TOKEN')

  if (headerToken == token):
    return await call_next(request)
  else:
    return JsonResponse.error(401, ['Unauthorized, this token is invalid'])
