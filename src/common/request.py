import json
from src.common.actions import Actions
from src.common.message import Message
from dataclasses import dataclass
from src.utils.polyfills import kwargs_only
@kwargs_only
@dataclass
class Request(Message):
    action: Actions = None
    model_identifier: str = ''


    def __post_init__(self):
        if not self.model_identifier: 
          self.model_identifier = str(self.payload.__class__)

    def get_key_from_identifier(self) -> str:
        return self.model_identifier.split('.')[-1][:-2]

    def from_json(json_object: str) -> "Request":
      data=json.loads(json_object)

      return Request(
        id=data['id'],
        payload=json.dumps(data['payload']),
        action=Actions[data['action']],
        model_identifier=data['model_identifier']
      )
