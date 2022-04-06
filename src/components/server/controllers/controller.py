from dataclasses import dataclass
from src.components.server.repositories.repository import Repository

@dataclass
class Controller:
    repository: Repository
