# coding: utf8

from lesson0 import add

"""
Let's suppose there exists a function object that returns sum of 2 numbers.
Then we can make following test.
"""


def test_add():
    x = 1
    y = 2
    assert add(x, y) == 3


def test2_add():
    x = 3
    y = 4
    assert add(x, y) == 7
