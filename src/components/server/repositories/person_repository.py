from dataclasses import dataclass
from src.common.models.person import Person
from src.components.server.repositories.repository import Repository

PersonRepository = Repository(Person)