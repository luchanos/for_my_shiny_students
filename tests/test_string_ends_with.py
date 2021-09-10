# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/

import pytest


def solution(string, ending):
    if ending == "":
        return True
    return string[-len(ending)::] == ending


@pytest.mark.parametrize("string, ending, expected", [("a", "a", True),
                                                      ("acbd", "cbd", True),
                                                      ("acacaca", "", True),
                                                      ('abcde', 'cde', True),
                                                      ('abcde', 'abc', False),
                                                      ('abcde', '', True)])
def test_solution(string, ending, expected):
    assert solution(string, ending) is expected
