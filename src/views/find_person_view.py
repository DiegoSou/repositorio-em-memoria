import os
from typing import Dict


class FindPersonView:
    def find_person(self) -> Dict: 
        os.system('cls||clear')
        
        print('Buscar pessoa \n\n')
        name = input('Determine o nome da pessoa para busca: ')

        person_finder_information = {
            "name": name
        }
        
        return person_finder_information


    def find_person_success(self, message: Dict) -> None:
        os.system('cls||clear')
        
        success_message = f'''
            Usuário(s) encontrado(s) com sucesso!
            
            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
        '''

        for person in message["info"]:
            success_message += f'''
                Id: { person["id"] }
                Name: { person["attributes"]["name"] }
                Age: { person["attributes"]["age"] }
                Height: { person["attributes"]["height"] }
            '''
        
        print(success_message)


    def find_person_error(self, error: str) -> None:
        os.system('cls||clear')
        
        error_message = f'''
            Erro ao encontrar o usuário.
            
            Erro: { error }
        '''

        print(error_message)
