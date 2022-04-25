import json
from src.common.actions import Actions
from src.common.message import Message
from dataclasses import dataclass
from src.utils.polyfills import kwargs_only
@kwargs_only
@dataclass
class Request(Message):
    action: Actions = None
    route: str = ''

    def from_json(json_object: str) -> "Request":
      data=json.loads(json_object)

      return Request(
        id=data['id'],
        payload=json.dumps(data['payload']),
        action=data['action'],
        route=data['route']
      )
