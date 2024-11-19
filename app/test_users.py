import users

def test_get_users():
    numofusers = users.get_users()
    assert len(numofusers) > 10000

