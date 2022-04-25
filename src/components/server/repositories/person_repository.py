import json
from typing import List
from src.common.models.person import Person
from src.components.server.repositories.repository import Repository

class PersonRepository(Repository):
  def __init__(self): 
    self.model = Person
    
  def findByCpf(self, cpf: str) -> Person:
    entity_list: List[Person] = self.storage.findAll(self.model.__name__)

    for entity in entity_list:
      if entity.cpf == cpf:
        return entity
    
def updateByCpf(self, payload):
    payload=json.loads(payload)
    cpf = payload["cpf"]

    entity = self.findByCpf(cpf)
    
    self.storage.updateById(entity.id, entity, self.model.__name__)