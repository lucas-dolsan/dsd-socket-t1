from dataclasses import dataclass
from uuid import UUID

from src.common.models.json_object import JsonObject

@dataclass
class Model(JsonObject):
  id: UUID
