import json
from uuid import uuid4 as uuid
from src.common.actions import Actions
from src.common.models.json_object import JsonObject

class Message(JsonObject):
    def __init__(self, action: Actions, payload: str):
        self.uid = uuid()
        self.action = action
        self.payload = payload

    def from_json(json_object) -> object:
        data = json.loads(json_object)

        return Message(
            action=Actions[data['action']],
            payload=json.dumps(data['payload'])
        )