# Funkcja zwracająca środkowy znak lub pusty napis jeżeli nie ma środka
import pytest


def mid(txt: str) -> str:
    if not isinstance(txt, str):
        raise ValueError("Input should be string")
    letters_quantity = len(txt)
    if letters_quantity % 2 == 0:
        return ""
    return txt[letters_quantity // 2]


def test_if_number_is_even():
    assert mid("siemaheniucotam") == "n"


def test_if_number_of_letter_is_odd():
    assert mid("hejtampodlasem") == ""


def test_if_input_is_empty():
    assert mid("") == ""


def test_if_input_is_int():
    with pytest.raises(ValueError):
        mid(213213)
