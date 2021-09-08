# https://www.codewars.com/kata/515f51d438015969f7000013
import pytest


def pyramid(n):
    res = []
    for i in range(1, n + 1):
        res.append([1 for _ in range(i)])
    return res


@pytest.mark.parametrize("inp, exp", [(0, []),
                                      (1, [[1]]),
                                      (2, [[1], [1, 1]]),
                                      (3, [[1], [1, 1], [1, 1, 1]]),
                                      (4, [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]])])
def test_pyramid_array(inp, exp):
    assert pyramid(inp) == exp
