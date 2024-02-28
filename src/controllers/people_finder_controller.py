from typing import Dict

class PeopleFinderController:
    def find(self, people_finder_info: Dict):
        try:
            self.__validate_fields(people_finder_info)
            response = self.__format_response(people_finder_info)
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
    
    def __format_response(self, find_person_data: Dict) -> Dict:
        if find_person_data is None:
            return None
        
        return {
            "count": 1,
            "type": "Person",
            "infos": {
                "name": "meu nome de teste"
            }
        }
        
