from dataclasses import dataclass

from src.common.actions import Actions
from src.common.models.person import Person
from src.common.request import Request
from src.components.server.controllers.controller import Controller
from src.components.server.repositories.person_repository import PersonRepository

@dataclass
class PersonController(Controller):
    def __init__(self):
        self.repository=PersonRepository
