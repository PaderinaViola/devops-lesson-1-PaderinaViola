from app.greet import greet, shout


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("Viola") == "Hello, Viola!"


def test_shout():
    assert shout("Viola") == "HELLO, VIOLA!"
