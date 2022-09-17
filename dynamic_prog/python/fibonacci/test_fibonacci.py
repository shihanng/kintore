import pytest
from fibonacci import fib


@pytest.mark.parametrize(
    "n,expected",
    [
        (6, 8),
    ],
)
def test_fib(n, expected):
    actual = fib(n)
    assert expected == actual
