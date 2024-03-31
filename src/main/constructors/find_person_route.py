from src.views import FindPersonView
from src.controllers import FindPersonController


def find_person_route():
    # view
    find_person_page = FindPersonView()
    person_information = find_person_page.find_person()
    
    # controller
    response = FindPersonController().find(person_information)
    
    # view
    if response["success"]:
        find_person_page.find_person_success(response["message"])
    else:
        find_person_page.find_person_error(response["error"])
