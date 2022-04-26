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
      
  def updateByCpf(self, cpf, payload):
      entity = self.findByCpf(cpf)

      person = Person.from_json(payload)

      return self.storage.updateById(entity.id, person, self.model.__name__)

  def deleteByCpf(self, cpf: str):
    entity = self.findByCpf(cpf)
    
    self.storage.deleteById(entity.id, self.model.__name__)