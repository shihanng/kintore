import how_sum
import pytest


@pytest.mark.parametrize(
    "target,numbers,expected",
    [
        (7, [2, 3], [3, 2, 2]),
        (7, [5, 3, 4, 7], [4, 3]),
        (7, [2, 4], None),
        (8, [2, 3, 5], [2, 2, 2, 2]),
        (300, [7, 14], None),
    ],
)
def test_how_sum(target, numbers, expected):
    actual = how_sum.how_sum(target, numbers, memo={})
    assert expected == actual
