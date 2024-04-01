from src.controllers.find_person_controller import FindPersonController
from src.models.entities.person import Person


class PersonRepositoryMock:
    def __init__(self, persons_found: list[Person]):
        self.__persons_found = persons_found


    def register_new(self, _: Person) -> str:        
        pass


    def find_by_name(self, _: str) -> list[Person]:
        return self.__persons_found


def test_find_success():
    person_repository = PersonRepositoryMock([
        Person('Test Person', 1, 1)
    ])
    
    find_person_controller = FindPersonController(person_repository)
    controller_response = find_person_controller.find({
        "name": 'Test Person'
    })
    
    assert controller_response["success"]
    assert controller_response["message"]["count"] == 1
    assert controller_response["message"]["info"][0]["attributes"]["name"] == 'Test Person'


def test_find_params_error():
    person_repository = PersonRepositoryMock([])
    
    find_person_controller = FindPersonController(person_repository)
    controller_response = find_person_controller.find({
        "name": 123
    })

    assert not controller_response["success"]
    assert controller_response["error"] == 'Campo nome inválido.'


def test_find_results_error():
    person_repository = PersonRepositoryMock([])
    
    find_person_controller = FindPersonController(person_repository)
    controller_response = find_person_controller.find({
        "name": 'Test Person'
    })

    assert not controller_response["success"]
    assert controller_response["error"] == 'Nenhum usuário com este nome foi encontrado.'
