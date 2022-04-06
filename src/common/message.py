from uuid import UUID, uuid4 as Uuid
from src.common.models.json_object import JsonObject
from dataclasses import dataclass

@dataclass
class Message(JsonObject):
    payload: any = None
    id: UUID = Uuid()

