from dataclasses import dataclass
import json
from uuid import uuid4 as Uuid
from src.common.models.model import Model
from src.utils.polyfills import kwargs_only

@kwargs_only
@dataclass
class Person(Model):
    cpf: str
    name: str
    address: str

    def from_json(json_object: str) -> 'Person':
        data  = json.loads(json_object)
        return Person(
            id=data['id'] or Uuid(),
            cpf=data['cpf'],
            name=data['name'],
            address=data['address']
        )