from argparse import Action
from enum import Enum, unique

@unique
class Actions(str, Enum):
    CREATE='CREATE'
    READ='READ'
    UPDATE='UPDATE'
    DELETE='DELETE'


    def __dict__(self):
        return self.value