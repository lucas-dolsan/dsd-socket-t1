import sys,os
sys.path.append(os.getcwd())

from src.common.actions import Actions
from src.components.server.request_router import RequestRouter
from src.common.models.model import Model
from src.common.request import Request

test_context={
  "controllers": {
        str(Model.__name__): "ExpectedController",
  },
  "request_args": {
    "payload": Model("1"),
    "action": Actions.CREATE
  }
}

class TestRequestRouter:
    def test_route_to_controller(self):
        request = Request(**test_context["request_args"])

        request_router=RequestRouter()
        request_router.controllers = test_context['controllers']

        key = request.get_key_from_identifier()
        routed_controller = request_router.get_controller(key)

        assert routed_controller == "ExpectedController"
