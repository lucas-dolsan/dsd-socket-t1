import json
from src.common.models.json_object import JsonObject

class Person(JsonObject):
    def __init__(self, cpf=None, name=None, address=None):
        self.cpf = cpf
        self.name = name
        self.address = address

    def from_json(json_object) -> object:
        data  = json.loads(json_object)
        return Person(
            cpf=data['cpf'],
            name=data['name'],
            address=data['address']
        )