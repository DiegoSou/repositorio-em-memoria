from src.views import RegisterPersonView
from src.controllers import RegisterPersonController


def register_person_route():
    # view
    register_person_page = RegisterPersonView()
    register_params = register_person_page.register_person()
    
    # controller
    response = RegisterPersonController().register(register_params)
    
    # view
    if response["success"]:
        register_person_page.register_person_success(response["message"])
    else:
        register_person_page.register_person_error(response["error"])
