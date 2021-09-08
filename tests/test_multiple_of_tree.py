# https://www.codewars.com/kata/61123a6f2446320021db987d

import pytest


def prev_mult_of_three(n):
    while n % 3 != 0:
        n //= 10
        if n == 0:
            return
    return n


@pytest.mark.parametrize("inp, exp", [(3, 3),
                                      (10, None),
                                      (111, 111),
                                      (123, 123),
                                      (952406, 9),
                                      (1244, 12)])
def test_prev_mult_of_three(inp, exp):
    assert prev_mult_of_three(inp) == exp
