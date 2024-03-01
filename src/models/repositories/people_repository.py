from faker import Faker
from src.models.entities.people import People

faker_instance = Faker()

class __PeopleRepository:
    def __init__(self) -> None:
        self.__people = []
        self.__repository_id = '001'
    
    def register_new(self, people: People) -> int:
        people.id = (self.__repository_id + str(faker_instance.unique.random_int(min=111111, max=999999)))
        self.__people.append(people) 
        
        return people.id

    def find_by_name(self, name: str) -> list[People]:
        found_people = []
        
        for people_entity in self.__people:
            if people_entity.name == name:
                found_people.append(people_entity)
        
        return found_people

people_repository = __PeopleRepository()
