# coding: utf8

import pytest
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


def test_non_number():
    """
    string 'a'와 숫자를 더하면 TypeError가 발생하고, 
    string 'a'와 string '4'를 더하면 Python은 두 string을 연결한 값을 
    return한다는 것을 알 수 있습니다.
    """
    x = 'a'
    y = 4
    with pytest.raises(TypeError):
        add(x, y)
    
    y = '4'
    assert add(x, y) == 'a4'


def test_non_integer():
    """
    x와 y에 정수가 아닌 다른 값들을 주면 결과가 어떻게 달라질까요?
    음수를 주면 어떻게 될까요?
    과제입니다.
    """
    pass

