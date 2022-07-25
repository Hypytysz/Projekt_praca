import pytest


def double_letters(text: str) -> bool:
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True
    return False

def test_if_is_double_letters():
    assert double_letters("ssiieemmaa") == True
    assert double_letters("ddrobne") == True
    assert double_letters("njee") == True
    assert double_letters("klucczowe") == True

def test_if_is_not_double_letters():
    assert double_letters("siema") == False
    assert double_letters("noelo") == False
    assert double_letters("nigdy") == False
    assert double_letters("nie ewa") == False
    assert double_letters("") == False

def test_if_text_is_int():
    with pytest.raises(TypeError):
        double_letters(312312)

