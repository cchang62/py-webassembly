from _wheel_poetry import greet

def test_greet():
    assert greet("World") == "Hello, World!"
