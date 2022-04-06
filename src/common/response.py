from dataclasses import dataclass
import json
from uuid import UUID
from src.common.message import Message
from src.utils.polyfills import kwargs_only

@kwargs_only
@dataclass
class Response(Message):
    request_id: UUID = None

    def from_json(json_object: str) -> "Response":
      data=json.loads(json_object)

      return Response(
        id=data['id'],
        payload=data['payload'],
        request_id=data['request_id']
      )