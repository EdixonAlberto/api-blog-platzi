from fastapi import APIRouter
from src.modules.response import Response, JsonResponse

router = APIRouter()


@router.get('/api')
async def get_status() -> Response:
  """ Get status api """
  return JsonResponse.ok({
      'status': 'OK'
  })
