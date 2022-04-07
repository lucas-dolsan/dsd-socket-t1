import sys,os
sys.path.append(os.getcwd())

from uuid import uuid4 as Uuid
from src.common.response import Response


test_context = {
  "test_json_conversion": {
    "payload": 201,
    "request_id": Uuid()
  }
}

class TestResponse:
  def create_response():
    request = Response(**test_context["test_json_conversion"])
    return request

  def test_json_conversion(self):
    response = TestResponse.create_response()

    response_json = response.to_json()
    converted_response = Response.from_json(response_json)

    assert type(converted_response).__name__ is Response.__name__
