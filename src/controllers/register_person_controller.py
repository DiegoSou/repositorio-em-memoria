from typing import Dict
from src.models.entities import Person
from src.models.repositories import PersonRepository


class RegisterPersonController:
    def __init__(self, person_repository: PersonRepository):
        self.__person_repository = person_repository


    def register(self, register_params: Dict) -> Dict:
        try:
            self.__validate_fields(register_params)
            
            person = Person(
                register_params["name"], 
                register_params["age"], 
                register_params["height"], 
            )

            # model
            person_id = self.__person_repository.register_new(person)

            response = self.__format_response(person_id, register_params)

            return {
                "success": True,
                "message": response
            }

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }


    def __validate_fields(self, register_params: Dict) -> None:
        if not isinstance(register_params["name"], str):
            raise Exception('Campo nome inválido')

        if not isinstance(register_params["age"], int):
            raise Exception('Campo idade inválido, utilize somente números.')

        if not isinstance(register_params["height"], int):
            raise Exception('Campo altura inválido, utilize somente números')


    def __format_response(self, person_id: str, person_information: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "info": {
                "id": person_id,
                "attributes": person_information
            }
        }
