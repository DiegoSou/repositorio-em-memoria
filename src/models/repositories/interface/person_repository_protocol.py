from typing import Protocol
from src.models.entities.person import Person


class PersonRepository(Protocol):
    def register_new(self, person: Person) -> str:
        pass


    def find_by_name(self, name: str) -> list[Person]:
        pass
