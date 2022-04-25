
from dataclasses import dataclass
from typing import List
from uuid import UUID
from src.common.models.model import Model
from src.components.server.adapters.storage_adapter import StorageAdapter

@dataclass
class MemoryStorageAdapter(StorageAdapter):
  _store={}

  def _get_model(self, model_class: str) -> dict:
    if model_class not in self._store:
        self._store[model_class] = {}
    return self._store[model_class]

  def findAll(self, model_class: str) -> List[Model]:
    return list(self._get_model(model_class).values())

  def findById(self, id: UUID, model_class: str) -> Model:
    try:
      model_store = self._get_model(model_class)
      result = model_store.get(id)
      return result
    except KeyError:
      return None

  def create(self, data: Model, model_class: str):
    self._get_model(model_class)[data.id] = data
      
  def deleteById(self, id: UUID, model_class: str):
    del self._get_model(model_class)[id]

  def updateById(self, id: UUID, newData: Model, model_class: str):
    self._get_model(model_class)[id] = newData
    return newData
    