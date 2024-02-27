from src.views.people_register_view import PeopleRegisterView

def people_register_constructor():
    # view
    people_register_view = PeopleRegisterView()
    
    # controller
    
    # manda para controller
    people_register_info = people_register_view.registry_person_view()
    return people_register_info
