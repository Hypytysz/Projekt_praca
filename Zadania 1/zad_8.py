# Suma wartosci listy, krotki, zbioru lub slownika
import pytest


def sum(elements):
    if hasattr(elements, "values"):
        elements = elements.values()
        print(elements)
    result = 0
    for el in elements:
        try:
            result += int(el)
        except ValueError:
            pass
    return result


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 2, 3, 4, 5], 15),
        ((1, 2, 5, 10), 18),
        ({10, 20, 30, 4}, 64),
        ({11, 2, 3}, 16),
        (["-10", 20, "-30"], -20),
        (["-10", -20, "-30"], -60),
        (["10", 20, "30"], 60)
    ],
)
def test_sum_list_tuple_set(input, expected):
    assert sum(input) == expected


def test_sum_dict():
    d = {"one": 1, "three": 3, "six": 6, "nine": 9}
    assert sum(d) == 19


def test_sum_not_iterable():
    with pytest.raises(TypeError):
        sum(11111)

