import os
from typing import Dict


class RegisterPersonView:
    def register_person(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar nova pessoa \n\n')

        name = input('Determine o nome da pessoa: ')
        age = int(input('Determine a idade da pessoa: '))
        height = int(input('Determine a altura da pessoa: '))

        new_person_info = {
            "name": name,
            "age": age,
            "height": height
        }

        return new_person_info


    def register_person_success(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Usuário cadastrado com sucesso.
            
            Tipo: { message["type"] }
            Registros: { message["count"] }
            Atributos:
                Id: { message["info"]["id"] }
                Nome: { message["info"]["attributes"]["name"] }
                Idade: { message["info"]["attributes"]["age"] }
        '''

        print(success_message)


    def register_person_error(self, error: str) -> None:
        os.system('cls||clear')

        error_message = f'''
            Falha ao cadastrar usuário.

            Erro: { error }
        '''

        print(error_message)
