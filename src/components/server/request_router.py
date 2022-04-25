from dataclasses import dataclass


from src.common.models.person import Person
from src.common.request import Request
from src.common.response import Response
from src.components.server.controllers.person_controller import PersonController

@dataclass
class RequestRouter:
    controllers={
        "person": PersonController(),
    }

    def get_controller(self, request: Request):
        return self.controllers[request.route]

    def handle_request(self, request: Request) -> Response:
        controller = self.get_controller(request)
        return controller.receive_request(request)
