from typing import Union, List
from http.client import OK
from fastapi.responses import JSONResponse
from fastapi import Query, Request, Response


class JsonResponse():
  @staticmethod
  def ok(response: Union[str, int, bool, dict, list]) -> Response:
    return JSONResponse(
        status_code=OK,
        content={
            'error': [],
            'response': response,
            'status_code': OK
        }
    )

  @staticmethod
  def error(code: int, error_messages: List[str]) -> Response:
    return JSONResponse(
        status_code=code,
        content={
            'error': error_messages,
            'response': None,
            'status_code': code
        }
    )
