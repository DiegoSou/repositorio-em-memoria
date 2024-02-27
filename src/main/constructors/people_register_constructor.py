from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():
    # view
    people_register_view = PeopleRegisterView()
    people_register_info = people_register_view.registry_person_view()
    
    # controller
    people_register_controller = PeopleRegisterController()
    response = people_register_controller.register(people_register_info)
    
    if response["success"]:
        people_register_view.registry_person_success(response["message"])
    else:
        people_register_view.registry_person_error(response["error"])
