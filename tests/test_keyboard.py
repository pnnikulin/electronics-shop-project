from src.keyboard import KeyBoard

kb = KeyBoard('Dark Project KD87A', 9600, 5)
kb1 = KeyBoard('Logitech K270', 5000, 10)
def test_str_kb():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb1) == 'Logitech K270'
def test_str_language():
    assert str(kb.language) == "EN"
    assert str(kb1.language) == "EN"

def test_change_language():
    kb.change_lang()
    assert str(kb.language) == "RU"

def test_changes_language():
    kb.change_lang().change_lang()
    assert str(kb.language) == "EN"