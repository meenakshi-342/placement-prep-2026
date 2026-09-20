from twttr import shorten
def test_lowercase():
    assert shorten("world") == "wrld"
    assert shorten("python") == "pythn"
def test_uppercase():
    assert shorten("MEENAKSHI") == "MNKSH"
    assert shorten("PINKY") == "PNKY"
def test_numbers():
    assert shorten("CS50P") == "CS50P"