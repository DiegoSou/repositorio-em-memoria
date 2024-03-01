from typing import Dict
from src.models.entities.people import People
from src.models.repositories.people_repository import people_repository

class PeopleRegisterController:
    def register(self, people_register_info: Dict) -> Dict:
        try:
            self.__validate_fields(people_register_info)
            
            # model
            person_id = people_repository.register_new(
                People(
                    people_register_info["name"], 
                    people_register_info["age"], 
                    people_register_info["height"], 
                )
            )
            
            response = self.__format_response(person_id, people_register_info)
            
            return {
                "success": True,
                "message": response
            }
        
        except Exception as exc:
            return {
                "success": False,
                "error": str(exc)
            }

    def __validate_fields(self, new_person_data: Dict) -> None:
        # name
        if not isinstance(new_person_data["name"], str):
            raise Exception('Campo nome inválido')

        # age
        try:
            int(new_person_data["age"])
        except: 
            raise Exception('Campo idade inválido, utilize somente números.')

        # height
        try:
            int(new_person_data["height"])
        except:
            raise Exception('Campo altura inválido, utilize somente números')

    def __format_response(self, person_id: str, person_info: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "info": {
                "id": person_id,
                "attributes": person_info
            }
        }
