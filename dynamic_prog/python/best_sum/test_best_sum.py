import best_sum
import pytest


@pytest.mark.parametrize(
    "target,numbers,expected",
    [
        (7, [5, 3, 4, 7], [7]),
        (8, [2, 3, 5], [3, 5]),
        (8, [1, 4, 5], [4, 4]),
        (7, [2, 4], None),
        (300, [7, 14], None),
        (100, [1, 2, 5, 25], [25, 25, 25, 25]),
    ],
)
def test_best_sum(target, numbers, expected):
    actual = best_sum.best_sum(target, numbers, memo={})
    assert expected == actual
