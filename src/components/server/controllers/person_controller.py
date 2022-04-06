from dataclasses import dataclass

from src.common.actions import Actions
from src.common.models.person import Person
from src.common.request import Request
from src.components.server.controllers.controller import Controller
from src.components.server.repositories.person_repository import PersonRepository


@dataclass
class PersonController(Controller):
    def __init__(self):
        self.repository=PersonRepository

    def receive_request(self, request: Request):
        action_map={
            Actions.CREATE: self.create
        }
        request_handler=action_map[request.action]
        request_handler(request)


    def create(self, request: Request):
        person = Person.from_json(request.payload)
        self.repository.create(person)
