from dataclasses import dataclass

from src.common.models.person import Person
from src.common.request import Request
from src.components.server.controllers.person_controller import PersonController

def _get_key_from_identifier(identifier: str) -> str:
    return identifier.split('.')[-1][:-2]

@dataclass
class RequestRouter:
    controllers={
        str(Person.__name__): PersonController(),
    }

    def get_controller(self, model_identifier: str):
        return self.controllers[model_identifier]

    def route_to_controller(self, request: Request):
        key = _get_key_from_identifier(request.model_identifier)
        controller = self.get_controller(key)
        controller.receive_request(request)
