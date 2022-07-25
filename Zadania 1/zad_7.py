# Najwieksza liczba z trzech


def max_of_two(x, y):
    if x >= y:
        return x
    return y


def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))


def test_max_of_three():
    assert max_of_three(1,2,3) == 3
    assert max_of_three(5,6,7) == 7
    assert max_of_three(1,0,0) == 1
