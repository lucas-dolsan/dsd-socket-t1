from dataclasses import dataclass
from src.common.actions import Actions
from src.common.models.model import Model
from src.common.request import Request
from src.common.response import Response
from src.components.server.repositories.repository import Repository

@dataclass
class Controller:
    repository: Repository

    def receive_request(self, request: Request):
        action_map={
            Actions.CREATE: self.create,
            Actions.READ: self.read,
            Actions.UPDATE: self.update,
            Actions.DELETE: self.delete,
        }
        request_handler=action_map[request.action]
        return request_handler(request)

    def create(self, request: Request):
        entity = self.repository.model.from_json(request.payload)
        
        self.repository.create(entity)

        return Response(
            payload={ "status": 201 },
            request_id=request.id,
        )

    def read(self, request: Request) -> Model:
        id = request.payload["id"]
        entity = self.repository.findById(id)

        if entity is None:
            payload={ "status": 404, "data": None }
        else:
            payload={ "status": 200, "data": entity }

        return Response(
            payload=payload,
            request_id=request.id,
        )

    def update(self, request: Request):
        entity = self.repository.model.from_json(request.payload)
        self.repository.updateById(entity.id, request.payload)

        return Response(
            payload={ "status": 200 },
            request_id=request.id,
        )

    def delete(self, request: Request):
        id = request.payload["id"]
        self.repository.deleteById(id)

        return Response(
            payload={ "status": 201 },
            request_id=request.id,
        )
