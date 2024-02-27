from .constructors.introduction import introduction
from .constructors.people_finder_constructor import people_finder_constructor
from .constructors.people_register_constructor import people_register_constructor

def start() -> None:
    while True:
        command = introduction()

        match command:
            case '1':
                people_register_constructor()
            case '2':
                people_finder_constructor()
            case '5':
                exit()
            case _:
                print('\nComando não foi encontrado.\n\n')
