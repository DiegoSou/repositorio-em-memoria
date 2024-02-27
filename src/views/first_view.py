def introduction_page():
    message = '''
        Sistema Cadastral
        
        * Cadastrar pessoa: 1
        * Buscar pessoa por nome: 2
        * Sair: 5
        
    '''

    print(message)
    command_input = input('Comando: ')
    return command_input
