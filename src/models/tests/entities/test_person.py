from src.models.entities.person import Person

def test_person_default():
    person = Person(name='Test Name', age=21, height=171)
    
    assert person.person_id is None
    assert person.name == 'Test Name'
    assert person.age == 21
    assert person.height == 171
    assert person.person_type.value == 'undefined'
    assert person.person_act() == 'Person default action'
