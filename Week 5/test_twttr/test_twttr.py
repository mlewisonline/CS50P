from twttr import shorten


def test_shorten_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_shorten_lowercase():
    assert shorten("hello world") == "hll wrld"

def test_shorten_numbers():
    assert shorten("12345") == "12345"

def test_shorten_punctuation():
    assert shorten("Hello, World!!!") == "Hll, Wrld!!!"
