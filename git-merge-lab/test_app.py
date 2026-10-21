# test_app.py
from app import add_numbers
from app import multiply_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_multiply_numbers():
    assert multiply_numbers(4, 3) == 12
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(5, 0) == 0
