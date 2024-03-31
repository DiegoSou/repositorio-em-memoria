from src.main.constructors import find_person_route, register_person_route
from src.views import main_page


def start() -> None:
    while True:
        command = main_page()
        match command:
            case '1':
                register_person_route()
            case '2':
                find_person_route()
            case '5':
                exit()
            case _:
                print('\nComando não foi encontrado.\n\n')
