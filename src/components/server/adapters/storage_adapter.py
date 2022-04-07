from uuid import UUID
from typing import List
from src.common.models.model import Model

class StorageAdapter:
  def findAll(self) -> List[Model]:
    raise NotImplementedError

  def findById(self, id: UUID) -> Model:
    raise NotImplementedError

  def create(self, data: Model):
    raise NotImplementedError
  
  def deleteById(self, id: UUID):
    raise NotImplementedError

  def updateById(self, id: UUID, newData: Model):
    raise NotImplementedError
    