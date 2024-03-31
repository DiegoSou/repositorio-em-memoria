from faker import Faker
from src.models.entities.person import Person

faker_instance = Faker()

class __PersonRepository:
    def __init__(self) -> None:
        self.__persons = []
        self.__repository_id = '001'


    def register_new(self, person: Person) -> int:
        if person.person_id is not None:
            raise ValueError('You cannot create new records with "person_id" value filled')
        
        person.person_id = (self.__repository_id + str(faker_instance.unique.random_int(min=111111, max=999999)))
        self.__persons.append(person) 
        
        return person.person_id


    def find_by_name(self, name: str) -> list[Person]:
        persons_found = []
        for person in self.__persons:
            if person.name == name:
                persons_found.append(person)

        return persons_found


person_repository = __PersonRepository()
