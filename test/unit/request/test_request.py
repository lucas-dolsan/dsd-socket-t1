import sys,os
sys.path.append(os.getcwd())

from dataclasses import dataclass
from src.common.actions import Actions
from src.common.request import Request

@dataclass
class SampleClass:
  sample_field: str

test_context = {
  "test_json_conversion": {
    "payload": SampleClass("test"),
    "action": Actions.CREATE
  }
}

class TestRequest:
  def create_request():
    request = Request(**test_context["test_json_conversion"])
    return request

  def test_json_conversion(self):
    request = TestRequest.create_request()

    request_json = request.to_json()
    converted_request = Request.from_json(request_json)

    assert type(converted_request).__name__ is Request.__name__

  def test_model_identifier(self):
    request = TestRequest.create_request()
    model_identifier=str(SampleClass.__name__)

    assert request.get_key_from_identifier() == model_identifier
    
