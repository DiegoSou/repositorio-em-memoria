import os
from typing import Dict

class PeopleRegisterView:
    def registry_person_view(self) -> Dict:
        os.system('cls||clear')
        
        print('Cadastrar Nova Pessoa \n\n')
        name = input('Determine o nome da pessoa: ')
        age = input('Determine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')
        
        new_person_info = {
            "name": name,
            "age": age,
            "heght": height
        }
        
        return new_person_info
