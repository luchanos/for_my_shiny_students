from gb.lesson_4.homework.hw_4_1 import salary
import pytest


@pytest.mark.parametrize("time, stavka, premia, expected", [(100, 20, 300, 2300),
                                                            (220, 10, 700, 2900),
                                                            (100, 40, 0, 4000)])
def test_first_task(time, stavka, premia, expected):
    assert expected == salary(time, stavka, premia)

