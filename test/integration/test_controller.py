import sys,os
sys.path.append(os.getcwd())

from src.components.server.adapters.storage_adapter import StorageAdapter
from src.components.server.adapters.memory_storage_adapter import MemoryStorageAdapter
from src.components.server.controllers.controller import Controller
from src.components.server.repositories.repository import Repository
from src.common.actions import Actions
from src.common.models.model import Model
from src.common.request import Request
from src.components.server.request_router import RequestRouter
from uuid import UUID, uuid4 as Uuid


id=Uuid()

class MockModel(Model):
  def from_json(json_object: str) -> object:
    return MockModel(id)


MOCK_MODEL_ROUTE = "MockModel"
MOCK_MODEL = MockModel

def prepare_mock_repository(mock_model, storage: StorageAdapter) -> Repository:
    repository = Repository(mock_model)
    repository.storage = storage
    print(repository.storage)
    return repository

def prepare_mock_controller(mock_repository: Repository) -> Controller:
    controller = Controller(Model)
    controller.repository = mock_repository
    return controller

storage=MemoryStorageAdapter()
mock_repository = prepare_mock_repository(MOCK_MODEL, storage)
mock_controller = prepare_mock_controller(mock_repository)

test_context={
  "controllers": {
        MOCK_MODEL_ROUTE: mock_controller,
  },
  "repositories": {
      "mock_repository": mock_repository
  },
  "request_args": {
    "route": MOCK_MODEL_ROUTE,
    "payload": MOCK_MODEL(id),
    "action": Actions.CREATE
  }
}

class TestController:
    def test_create_mock_object(self):
        request = Request(**test_context["request_args"])

        request_router=RequestRouter()
        request_router.controllers = test_context['controllers']

        routed_controller = request_router.get_controller(request)

        routed_controller.receive_request(request)

        result = storage.findById(id, MockModel.__name__)

        assert result.id == id