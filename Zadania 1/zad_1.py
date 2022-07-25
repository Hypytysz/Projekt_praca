# Separator tysięcy
import pytest


def format_number(liczba: int) -> str:
    if liczba < 0:
        raise ValueError("Number should be positive")
    return f"{liczba:,}"


def test_format_number():
    assert format_number(1000) == "1,000"
    assert format_number(0) == "0"
    assert format_number(1000000000) == "1,000,000,000"


def test_format_number_when_input_is_negative():
    with pytest.raises(ValueError):
        format_number(-1000)


def test_format_number_when_input_is_not_number():
    with pytest.raises(TypeError):
        format_number("ala ma kota")
