import can_sum
import pytest


@pytest.mark.parametrize(
    "target,numbers,expected",
    [
        (7, [2, 3], True),
        (7, [5, 3, 4, 7], True),
        (7, [2, 4], False),
        (8, [2, 3, 5], True),
    ],
)
def test_can_sum(target, numbers, expected):
    actual = can_sum.can_sum_memo(target, numbers, memo={})
    assert expected == actual
