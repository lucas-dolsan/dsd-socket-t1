from dataclasses import dataclass

from src.common.models.person import Person
from src.common.request import Request
from src.components.server.controllers.person_controller import PersonController

@dataclass
class RequestRouter:
    controllers={
        "person": PersonController(),
    }

    def get_controller(self, request: Request):
        return self.controllers[request.route]

    def route_to_controller(self, request: Request):
        controller = self.get_controller(request)
        controller.receive_request(request)
