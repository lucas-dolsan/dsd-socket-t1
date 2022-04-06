import json
from dataclasses import dataclass
from uuid import UUID
@dataclass
class JsonParser:
    def parse(object: any) -> dict:
        if type(object) is UUID:
            return str(object)

        if hasattr(object, '__dict__'):
            return object.__dict__

@dataclass
class JsonObject:
    def to_json(self) -> str:
        return json.dumps(self, default=JsonParser.parse)

    def from_json(json_object: str) -> object:
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return f'{self.__class__}{self.__str__()}'