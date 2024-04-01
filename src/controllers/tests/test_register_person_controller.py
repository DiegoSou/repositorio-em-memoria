from src.controllers.register_person_controller import RegisterPersonController
from src.models.entities.person import Person


class PersonRepositoryMock:
    def register_new(self, _: Person) -> str:        
        return '001'


    def find_by_name(self, _: str) -> list[Person]:
        pass


def test_register_success():
    person_repository = PersonRepositoryMock()

    register_person_controller = RegisterPersonController(person_repository)
    controller_response = register_person_controller.register({
        "name": 'Test Name',
        "age": 1,
        "height": 1
    })

    assert controller_response["success"]
    assert controller_response["message"]["count"] == 1
    assert controller_response["message"]["info"]["id"] == '001'


def test_register_params_name_error():
    person_repository = PersonRepositoryMock()
    
    register_person_controller = RegisterPersonController(person_repository)
    controller_response = register_person_controller.register({
        "name": 123
    })

    assert not controller_response["success"]
    assert controller_response["error"] == 'Campo nome inválido'


def test_register_params_age_error():
    person_repository = PersonRepositoryMock()

    register_person_controller = RegisterPersonController(person_repository)
    controller_response = register_person_controller.register({
        "name": 'Test Name',
        "age": 'Test age'
    })

    assert not controller_response["success"]
    assert controller_response["error"] == 'Campo idade inválido, utilize somente números.'


def test_register_params_height_error():
    person_repository = PersonRepositoryMock()

    register_person_controller = RegisterPersonController(person_repository)
    controller_response = register_person_controller.register({
        "name": 'Test Name',
        "age": 1,
        "height": 'Test height'
    })

    assert not controller_response["success"]
    assert controller_response["error"] == 'Campo altura inválido, utilize somente números'
