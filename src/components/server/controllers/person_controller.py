from dataclasses import dataclass
import json
from src.common.actions import Actions
from src.common.models.person import Person
from src.common.person_actions import PersonActions
from src.common.request import Request
from src.common.response import Response
from src.components.server.controllers.controller import Controller
from src.components.server.repositories.person_repository import PersonRepository

@dataclass
class PersonController(Controller):
    def __init__(self):
        self.repository=PersonRepository()

    def receive_request(self, request: Request):
        action_map={
            Actions.CREATE: self.create,
            Actions.READ: self.read,
            Actions.UPDATE: self.update,
            Actions.DELETE: self.delete,
            PersonActions.READ_BY_CPF: self.find_by_cpf,
            PersonActions.UPDATE_BY_CPF: self.update_by_cpf 
        }
        request_handler=action_map[request.action]
        return request_handler(request)

    def update_by_cpf(self, request: Request) -> Person:
        payload=json.loads(request.payload)
        cpf = payload["cpf"]

        entity = self.repository.updateById(cpf, payload)

        response_payload={ "status": 200, "data": entity }

        return Response(
            payload=response_payload,
            request_id=request.id,
        )


    def find_by_cpf(self, request: Request) -> Person:
        payload=json.loads(request.payload)
        cpf = payload["cpf"]

        entity = self.repository.findByCpf(cpf)

        if entity is None:
            payload={ "status": 404, "data": None }
        else:
            payload={ "status": 200, "data": entity }

        return Response(
            payload=payload,
            request_id=request.id,
        )