import json
import six
import abc

@six.add_metaclass(abc.ABCMeta)
class JsonObject():
    def to_json(self):
        return json.dumps(
            self,
            default=lambda obj: obj.__dict__,
            sort_keys=True, indent=2
        )

    @abc.abstractmethod
    def from_json(json_object) -> object:
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return f'{self.__class__}{self.__str__()}'