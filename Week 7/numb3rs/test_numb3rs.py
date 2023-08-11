from numb3rs import validate


def test_num_range():
    assert validate("-1.-1.-1.-1") == False
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False


def test_non_numbers():
    assert validate("aaa.aaa.aaa.aaa") == False
    assert validate("AAA.AAA.AAA.AAA") == False
    assert validate("AAA.250.BB.X") == False

def test_missing():
    assert validate("1..2.") == False
    assert validate(".1..2") == False
    assert validate(".1..2") == False

def test_length():
    assert validate("111.222.333.4444") == False
    assert validate("1234.0.0.0") == False
    assert validate("5.5555.555.5555") == False