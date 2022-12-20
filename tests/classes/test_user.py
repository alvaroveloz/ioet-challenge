from classes.User import User

def test_user_instance():
    user = User('Alvaro')
    assert user.name == 'Alvaro'