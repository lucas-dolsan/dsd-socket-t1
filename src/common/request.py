from argparse import Action
import json
from typing import Optional
from uuid import UUID
from src.common.actions import Actions
from src.common.message import Message
from dataclasses import dataclass

@dataclass
class Request(Message):
    action: Action = None
    model_identifier: str = ''


    def __post_init__(self):
        if not self.model_identifier: 
          self.model_identifier = str(self.payload.__class__)

    def from_json(json_object: str) -> "Request":
      data=json.loads(json_object)

      return Request(
        id=data['id'],
        payload=json.dumps(data['payload']),
        action=Actions[data['action']],
        model_identifier=data['model_identifier']
      )
