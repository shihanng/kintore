import pytest
from fibonacci import fib, fib_memo


@pytest.mark.parametrize(
    "n,expected",
    [
        (6, 8),
        (7, 13),
        (8, 21),
    ],
)
def test_fib(n, expected):
    actual = fib(n)
    assert expected == actual

    actual = fib_memo(n)
    assert expected == actual


@pytest.mark.parametrize(
    "n,expected",
    [
        (50, 12586269025),
    ],
)
def test_fib_memo(n, expected):
    actual = fib_memo(n)
    assert expected == actual
