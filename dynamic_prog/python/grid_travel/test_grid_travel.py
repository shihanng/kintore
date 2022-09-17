import grid_travel
import pytest


@pytest.mark.parametrize(
    "m,n,expected",
    [
        (1, 1, 1),
        (2, 3, 3),
        (3, 2, 3),
        (3, 3, 6),
        (18, 18, 2333606220),
    ],
)
def test_fib(m, n, expected):
    actual = grid_travel.grid_travel(m, n)
    assert expected == actual
