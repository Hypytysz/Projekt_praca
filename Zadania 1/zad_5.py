# Anagramy
import pytest

def is_anagram(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)

def test_is_anagram():
    assert is_anagram("mesa", "asem") == True
    assert is_anagram("", "") == True
    assert is_anagram("Alice", "Bob") == False

def test_is_a_and_b_are_int():
    with pytest.raises(TypeError):
        is_anagram(12321, 21321)




