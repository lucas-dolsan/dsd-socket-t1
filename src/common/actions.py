from enum import Enum, unique

@unique
class Actions(str, Enum):
    CREATE='CREATE'
    READ='READ'
    UPDATE='UPDATE'
    DELETE='DELETE'
    LIST='LIST'

    def __dict__(self):
        return self.value

    def from_operation(op):
        operation_map={
            'c': Actions.CREATE,
            'r': Actions.READ,
            'u': Actions.UPDATE,
            'd': Actions.DELETE,
            'l': Actions.LIST
        }

        return operation_map[op]