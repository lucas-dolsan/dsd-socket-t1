from enum import Enum, unique

@unique
class PersonActions(str, Enum):
    READ_BY_CPF='READ_BY_CPF'
    UPDATE_BY_CPF='UPDATE_BY_CPF'

    def __dict__(self):
        return self.value