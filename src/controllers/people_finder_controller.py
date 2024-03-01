from typing import Dict
from src.models.entities.people import People
from src.models.repositories.people_repository import people_repository

class PeopleFinderController:
    def find(self, people_finder_info: Dict):
        try:
            self.__validate_fields(people_finder_info)
            
            # model
            found_people = people_repository.find_by_name(people_finder_info["name"])

            if len(found_people) == 0:
                raise Exception('Nenhum usuário com este nome foi encontrado.')

            response = self.__format_response(found_people)
            return {
                "success": True,
                "message": response
            }

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }

    def __validate_fields(self, find_person_data: Dict) -> None:
        # name
        if not isinstance(find_person_data["name"], str):
            raise Exception('Campo nome inválido.')

    def __format_response(self, find_person_data: list[People]) -> Dict: 
        formatted_people = []       

        for _,person in enumerate(find_person_data):
            formatted_people.append(
                {
                    "id": person.id,
                    "attributes": {
                        "name": person.name,
                        "age": person.age,
                        "height": person.height,
                    }
                }
            )

        return {
            "count": len(find_person_data),
            "type": "Person",
            "info": formatted_people
        }
