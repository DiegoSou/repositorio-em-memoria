from dataclasses import dataclass
from enum import Enum


class PersonType(Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNDEFINED = 'undefined'


@dataclass
class Person:
    name: str
    age: int
    height: int
    person_type: PersonType = PersonType('undefined')
    person_id: str = None

    def person_act(self, action_func: callable = None) -> any:
        return action_func(self) if (action_func is not None) else 'Person default action'
