from dataclasses import dataclass
from typing import List
from uuid import UUID
from src.common.models.model import Model
from src.components.server.dependencies import Storage
@dataclass
class Repository():
  model: Model
  storage=Storage

  def findAll(self) -> List[Model]:
    return self.storage.findAll(self.model.__name__)

  def findById(self, id: UUID) -> Model:
    return self.storage.findById(id, self.model.__name__)

  def create(self, data: Model):
    self.storage.create(data, self.model.__name__)

  def deleteById(self, id: UUID):
    self.storage.deleteById(id, self.model.__name__)

  def updateById(self, id: UUID, newData: Model):
    self.storage.updateById(id, newData, self.model.__name__)

