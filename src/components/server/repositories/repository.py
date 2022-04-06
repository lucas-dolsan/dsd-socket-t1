from dataclasses import dataclass
from typing import List
from uuid import UUID
from src.common.models.model import Model
from src.components.server.adapters.storage_adapter import StorageAdapter
from dependencies import Storage

@dataclass
class Repository():
  model: Model
  storage=Storage

  def findAll(self) -> List[Model]:
    return self.storage.findAll(self.model.__class__)

  def findById(self, id: UUID) -> Model:
    return self.storage.findById(id, self.model.__class__)

  def create(self, data: Model):
    self.storage.create(data, self.model.__class__)

  def deleteById(self, id: UUID):
    self.deleteById(id, self.model.__class__)

  def updateById(self, id: UUID, newData: Model):
    self.updateById(id, newData, self.model.__class__)

