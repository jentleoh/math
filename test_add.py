# coding: utf8

"""
Let's suppose there exists a function object that returns sum of 2 numbers.
Then we can make following tests.
"""

import pytest
from lesson0 import add


def test_add():
    x = 1
    y = 2
    assert add(x, y) == 3


def test2_add():
    x = 3
    y = 4
    assert add(x, y) == 7


def test_not_number_value():

    x = 'hello'
    y = 3
    with pytest.raises(TypeError):
        add(x, y)

    assert add(x, y) == None
