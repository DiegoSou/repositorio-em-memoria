from src.views.people_finder_view import PeopleFinderView
from src.controllers.people_finder_controller import PeopleFinderController

def people_finder_constructor():
    # view
    people_finder_view = PeopleFinderView()
    people_finder_info = people_finder_view.find_person_view()
    
    # controller
    people_finder_controller = PeopleFinderController()
    response = people_finder_controller.find(people_finder_info)
    
    if response["success"]:
        people_finder_view.find_person_success(response["message"])
    else:
        people_finder_view.find_person_error(response["error"])
