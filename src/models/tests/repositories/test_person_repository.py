from pytest import raises

from src.models.entities import Person
from src.models.repositories.person_repository import person_repository
from src.models.repositories.interface import PersonRepository


class PersonProtocolTest(PersonRepository):
    pass


def test_person_repository_protocol():
    person_protocol = PersonProtocolTest()
    person_protocol.register_new(Person('Test Person', 21, 171))
    person_protocol.find_by_name('Test Person')


def test_register_new():
    person = Person('Test Person', 21, 171)
    person_id = person_repository.register_new(person)
    
    assert person_id is not None
    assert person.person_id is not None
    assert person_id.startswith('001')
    assert person_id == person.person_id


def test_error_register_new():
    person = Person('Test Person', 21, 171, person_id='1234')
    
    with raises(ValueError) as error_info:
        person_repository.register_new(person)
    
    assert 'You cannot create new records with "person_id" value filled' in str(error_info.value)


def test_find_by_name():
    person_repository.register_new(Person('Test Find Person by Name', 21, 171))
    persons_found = person_repository.find_by_name('Test Find Person by Name')
    
    assert len(persons_found) > 0
    assert persons_found[0].name == 'Test Find Person by Name'
