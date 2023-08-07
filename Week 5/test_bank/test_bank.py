from bank import value



def test_greeting_lower():
    assert value("hello there") == 0
    assert value("hey there") == 20
def test_greeting_upper():
    assert value("HELLO THERE") == 0
    assert value("HEY THERE") == 20
def test_greeting():
    assert value("whats up") == 100
    assert value("well Hi there") == 100