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
            Actions.CREATE: self.create,
            Actions.READ: self.read,
            Actions.UPDATE: self.update,
            Actions.DELETE: self.delete,

        }
        request_handler=action_map[request.action]
        request_handler(request)

    def create(self, request: Request):
        person = Person.from_json(request.payload)
        self.repository.create(person)

    def read(self, request: Request) -> Person:
        id = request.payload["id"]
        # request should have an id, or params/args, if payload 
        # truly is an analog por HTTP Body, then maybe I should just rename it
        return self.repository.findById(id)

    def update(self, request: Request):
        id = request.payload["id"]
        self.repository.findById(id)
        

    def delete(self, request: Request):
        pass