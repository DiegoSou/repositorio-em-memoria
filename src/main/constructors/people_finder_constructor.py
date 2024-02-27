from src.views.people_finder_view import PeopleFinderView

def people_finder_constructor():
    # view
    people_finder_view = PeopleFinderView()
    
    # controller
    
    # manda para controller
    people_finder_info = people_finder_view.find_person_view()
    return people_finder_info
