from typing import Dict
from src.models.entities import Person
from src.models.repositories import PersonRepository


class FindPersonController:
    def __init__(self, person_repository: PersonRepository):
        self.__person_repository = person_repository

    
    def find(self, search_params: Dict):
        try:
            self.__validate_fields(search_params)
            
            # model
            persons_found = self.__person_repository.find_by_name(search_params["name"])

            if len(persons_found) == 0:
                raise Exception('Nenhum usuário com este nome foi encontrado.')

            response = self.__format_response(persons_found)

            return {
                "success": True,
                "message": response
            }

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }


    def __validate_fields(self, search_params: Dict) -> None:
        if not isinstance(search_params["name"], str):
            raise Exception('Campo nome inválido.')


    def __format_response(self, persons_found: list[Person]) -> Dict: 
        persons_data = []       

        for _,person in enumerate(persons_found):
            persons_data.append(
                {
                    "id": person.person_id,
                    "attributes": {
                        "name": person.name,
                        "age": person.age,
                        "height": person.height,
                    }
                }
            )

        return {
            "count": len(persons_data),
            "type": "Person",
            "info": persons_data
        }
