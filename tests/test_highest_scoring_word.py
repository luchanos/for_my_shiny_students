# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
import pytest

ESTIMATOR_MAP = {chr(num): num - 96 for num in range(97, 123)}


def estimator_func(word):
    estimation = 0
    for char in word:
        estimation += ESTIMATOR_MAP[char]
    return estimation


def high(x):
    x_list = x.lower().split()
    res = list(zip(map(estimator_func, x_list), x_list))
    max_val_tup = (0, 0)
    for tup in res:
        if tup[0] > max_val_tup[0]:
            max_val_tup = tup
    return max_val_tup[1]


@pytest.mark.parametrize("x, expected", [("man i need a taxi up to ubud", "taxi"),
                                         ('what time are we climbing up the volcano', 'volcano'),
                                         ('take me to semynak', 'semynak'),
                                         ('aa b', 'aa'),
                                         ('b aa', 'b'),
                                         ('bb d', 'bb'),
                                         ('d bb', 'd'),
                                         ("aaa b", "aaa")])
def test_high(x, expected):
    assert high(x) == expected
