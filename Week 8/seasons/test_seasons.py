from datetime import date
from seasons import minutes_past

def test_one():
    test_date = date.fromisoformat("2022-08-12")
    assert minutes_past(test_date) == 'Five hundred twenty-five thousand, six hundred minutes'

def test_two():
    test_date = date.fromisoformat("2021-08-12")
    assert minutes_past(test_date) == 'One million, fifty-one thousand, two hundred minutes'

