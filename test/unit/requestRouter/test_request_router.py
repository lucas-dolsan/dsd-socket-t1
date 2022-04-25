import sys,os
sys.path.append(os.getcwd())

from src.common.actions import Actions
from src.components.server.request_router import RequestRouter
from src.common.models.model import Model
from src.common.request import Request

test_context={
  "controllers": {
        "ExampleModel": "ExpectedController",
  },
  "request_args": {
    "route": "ExampleModel",
    "payload": Model("1"),
    "action": Actions.CREATE
  }
}

class TestRequestRouter:
  def test_handle_request(self):
    request = Request(**test_context["request_args"])

    request_router=RequestRouter()
    request_router.controllers = test_context['controllers']

    routed_controller = request_router.get_controller(request=request)

    assert routed_controller == "ExpectedController"
