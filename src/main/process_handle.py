from .constructors.introduction import introduction

def start() -> None:
    while True:
        command = introduction()

        match command:
            case '1':
                print('Comando 1 foi acionado.')
            case '2':
                print('Comando 2 foi acionado.')
            case '5':
                exit()
            case _:
                print('\nComando não foi encontrado.\n\n')
