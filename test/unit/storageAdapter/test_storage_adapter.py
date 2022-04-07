import sys,os
sys.path.append(os.getcwd())

from src.common.models.model import Model
from dataclasses import dataclass
from uuid import uuid4 as Uuid
from src.components.server.adapters.memory_storage_adapter import MemoryStorageAdapter

class SampleModel(Model):
  sample_field=''

test_context={
  "intial_storage_state": {
    SampleModel.__class__: {
      "1": SampleModel("1"),
      "2": SampleModel("2"),
    }
  }
}

storage=MemoryStorageAdapter()
model=SampleModel

storage._store = test_context["intial_storage_state"]

class TestStorageAdapter:
  def test_findAll(self):
    result = storage.findAll(model.__class__)
    assert len(result) == 2

  def test_findById(self):
    id="1"
    result = storage.findById(id, model.__class__)
    assert result.id == id

  def test_create(self):
    id=Uuid()
    data=SampleModel(id=id)
    storage.create(data, model.__class__)
    assert storage._store[model.__class__][id] is not None

  def test_deleteById(self):
    storage.deleteById("2", model.__class__)
    assert storage.findById(id, model.__class__) is None

  def test_updateById(self):
    id="1"
    newData=SampleModel(id)
    newData.sample_field="test"
    storage.updateById(id, newData, model.__class__)
    assert storage._store[model.__class__][id].sample_field == "test"
